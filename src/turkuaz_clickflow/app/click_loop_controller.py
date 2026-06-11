"""Coordinates the UI-safe repeated click loop."""

from dataclasses import dataclass
import logging
from typing import Callable, Optional, Protocol

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_runner import ClickRunner, ClickRunnerResult
from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


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
    ) -> None:
        self._automation_service = automation_service
        self._click_runner = click_runner
        self._scheduler = scheduler
        self._feedback_service = feedback_service
        self._on_feedback = on_feedback
        self._on_update = on_update
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
        if result.error_message:
            logger.error("Click runner stopped with error: %s", result.error_message)
        if result.stopped:
            self._scheduler.stop()
            self._running = False
        if result.stop_reason is not None and self._on_feedback is not None:
            self._on_feedback(self._feedback_for_runner_result(result))
        if self._on_update is not None:
            self._on_update()
        return result

    def stop(self) -> None:
        """Stop scheduled runner ticks."""
        if self._running:
            self._scheduler.stop()
            self._running = False

    def _interval_ms(self) -> int:
        return max(1, int(round(self._click_runner.click_interval_seconds * 1000)))

    def _feedback_for_runner_result(
        self,
        result: ClickRunnerResult,
    ) -> FeedbackMessage:
        if result.stop_reason is StopReason.ERROR and result.error_message:
            return FeedbackMessage(
                level="error",
                text=self._human_error_message(result.error_message),
            )
        return self._feedback_service.for_stop_reason(result.stop_reason)

    @staticmethod
    def _human_error_message(error_message: str) -> str:
        normalized = error_message.lower()
        if (
            "accessibility" in normalized
            or "input monitoring" in normalized
            or "permission" in normalized
            or "izin" in normalized
        ):
            return "macOS erişilebilirlik izni gerekli olabilir."
        if (
            "not available" in normalized
            or "not implemented" in normalized
            or "unavailable" in normalized
            or "api is not available" in normalized
            or "backend" in normalized and "kullanılamıyor" in normalized
        ):
            return "Bu platformda tıklama backend'i kullanılamıyor."
        return f"Tıklama başlatılamadı: {error_message}"
