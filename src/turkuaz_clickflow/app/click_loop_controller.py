"""Coordinates the UI-safe repeated click loop."""

from dataclasses import dataclass
import logging
from typing import Callable, Optional, Protocol

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_runner import ClickRunner, ClickRunnerResult
from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import WindowQueryAdapter


logger = logging.getLogger(__name__)


class ClickLoopScheduler(Protocol):
    """Scheduler contract used by UI adapters."""

    def start(self, interval_ms: int, callback: Callable[[], None]) -> None:
        """Start periodic callback execution."""

    def stop(self) -> None:
        """Stop periodic callback execution."""


@dataclass(frozen=True)
class ClickLoopSyncResult:
    """Result of synchronizing runner state with automation state."""

    running: bool
    interval_ms: Optional[int] = None


class ClickLoopController:
    """Starts and stops ClickRunner without blocking the UI event loop."""

    def __init__(
        self,
        automation_service: AutomationService,
        click_runner: ClickRunner,
        scheduler: ClickLoopScheduler,
        feedback_service: FeedbackService,
        on_feedback: Optional[Callable[[FeedbackMessage], None]] = None,
        on_update: Optional[Callable[[], None]] = None,
        window_query: Optional[WindowQueryAdapter] = None,
    ) -> None:
        self._automation_service = automation_service
        self._click_runner = click_runner
        self._scheduler = scheduler
        self._feedback_service = feedback_service
        self._on_feedback = on_feedback
        self._on_update = on_update
        self._window_query = window_query
        self._running = False

    @property
    def is_running(self) -> bool:
        """Whether the scheduler is currently active."""
        return self._running

    def sync_with_automation(self) -> ClickLoopSyncResult:
        """Start or stop scheduled runner ticks based on automation state."""
        if self._automation_service.state is AutomationState.RUNNING:
            interval_ms = self._interval_ms()
            if not self._running:
                self._scheduler.start(interval_ms, self.tick)
                self._running = True
            return ClickLoopSyncResult(running=True, interval_ms=interval_ms)

        if self._running:
            self._scheduler.stop()
            self._running = False
        return ClickLoopSyncResult(running=False)

    def tick(self) -> ClickRunnerResult:
        """Run one click tick and update scheduler/feedback state."""
        guard_result = self._stop_if_window_guard_violated()
        if guard_result is not None:
            self._handle_runner_result(guard_result)
            return guard_result

        try:
            result = self._click_runner.run_once()
        except Exception as exc:
            logger.exception("Unhandled click runner exception: %s", exc)
            self._automation_service.stop(reason=StopReason.ERROR)
            result = ClickRunnerResult(
                attempted_clicks=0,
                successful_clicks=0,
                stopped=True,
                stop_reason=StopReason.ERROR,
                error_message=str(exc),
            )
        self._handle_runner_result(result)
        return result

    def _handle_runner_result(self, result: ClickRunnerResult) -> None:
        if result.error_message:
            logger.error("Click runner stopped with error: %s", result.error_message)
        if result.stopped:
            self._scheduler.stop()
            self._running = False
        if result.stop_reason is not None and self._on_feedback is not None:
            self._on_feedback(self._feedback_for_runner_result(result))
        if self._on_update is not None:
            self._on_update()

    def stop(self) -> None:
        """Stop scheduled runner ticks."""
        if self._running:
            self._scheduler.stop()
            self._running = False

    def _interval_ms(self) -> int:
        return max(1, int(round(self._click_runner.click_interval_seconds * 1000)))

    def _stop_if_window_guard_violated(self) -> Optional[ClickRunnerResult]:
        settings = self._automation_service.settings
        if not settings.window_guard_enabled:
            return None
        if self._window_query is None:
            return None

        if not settings.target_window_id:
            return self._stop_for_window_guard(StopReason.TARGET_WINDOW_MISSING)

        windows = self._window_query.list_windows()
        target_exists = any(window.id == settings.target_window_id for window in windows)
        if not target_exists:
            return self._stop_for_window_guard(StopReason.TARGET_WINDOW_MISSING)

        active_window = self._window_query.active_window()
        if active_window is None:
            return self._stop_for_window_guard(StopReason.TARGET_WINDOW_MISSING)
        if active_window.id != settings.target_window_id:
            return self._stop_for_window_guard(StopReason.WINDOW_CHANGED)
        return None

    def _stop_for_window_guard(self, reason: StopReason) -> ClickRunnerResult:
        stop_result = self._automation_service.stop(reason=reason)
        return ClickRunnerResult(
            attempted_clicks=0,
            successful_clicks=0,
            stopped=True,
            stop_reason=stop_result.stop_reason,
        )

    def _feedback_for_runner_result(
        self,
        result: ClickRunnerResult,
    ) -> FeedbackMessage:
        if result.stop_reason is StopReason.ERROR and result.error_message:
            return self._feedback_service.for_platform_error(
                result.error_message,
                operation="mouse",
            )
        return self._feedback_service.for_stop_reason(result.stop_reason)
