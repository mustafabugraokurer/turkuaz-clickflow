"""Coordinates the UI-safe repeated click loop."""

from dataclasses import dataclass
from typing import Callable, Optional, Protocol

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_runner import ClickRunner, ClickRunnerResult
from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.domain.automation_state import AutomationState


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
        result = self._click_runner.run_once()
        if result.stopped:
            self._scheduler.stop()
            self._running = False
        if result.stop_reason is not None and self._on_feedback is not None:
            self._on_feedback(self._feedback_service.for_stop_reason(result.stop_reason))
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
