"""View model for the MVP main window."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.app.hotkey_service import HotkeyResult, HotkeyService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


@dataclass(frozen=True)
class MainWindowSnapshot:
    """Display values for the main window."""

    title: str
    status: str
    cps: int
    hotkey: str
    click_count: int
    elapsed_time: str
    target_window: str
    window_guard_enabled: bool
    message: str
    message_level: str
    start_enabled: bool
    stop_enabled: bool


class MainWindowViewModel:
    """Builds UI-ready values without containing UI widgets."""

    def __init__(
        self,
        automation_service: AutomationService,
        feedback_service: FeedbackService,
        hotkey_service: Optional[HotkeyService] = None,
    ) -> None:
        self._automation_service = automation_service
        self._feedback_service = feedback_service
        self._hotkey_service = hotkey_service or HotkeyService(automation_service)
        self._last_feedback: Optional[FeedbackMessage] = None

    def start(self, cps: int) -> MainWindowSnapshot:
        """Start automation through the app service and return refreshed UI state."""
        result = self._automation_service.start(cps=cps)
        self._last_feedback = self._feedback_service.for_automation_result(result)
        return self.snapshot()

    def stop(self) -> MainWindowSnapshot:
        """Stop automation through the app service and return refreshed UI state."""
        result = self._automation_service.stop(reason=StopReason.USER_STOPPED)
        self._last_feedback = self._feedback_service.for_automation_result(result)
        return self.snapshot()

    def trigger_hotkey(self, hotkey: Optional[str] = None) -> MainWindowSnapshot:
        """Route a detected hotkey event through HotkeyService."""
        result = self._hotkey_service.trigger(hotkey or self._hotkey_service.hotkey)
        self._last_feedback = self._feedback_service.for_hotkey_result(result)
        return self.snapshot()

    def show_feedback(self, feedback: FeedbackMessage) -> MainWindowSnapshot:
        """Expose app-level feedback in the next UI snapshot."""
        self._last_feedback = feedback
        return self.snapshot()

    def show_hotkey_result(self, result: HotkeyResult) -> MainWindowSnapshot:
        """Expose a HotkeyService result in the next UI snapshot."""
        self._last_feedback = self._feedback_service.for_hotkey_result(result)
        return self.snapshot()

    def snapshot(self) -> MainWindowSnapshot:
        """Return current display values for the main window."""
        settings = self._automation_service.settings
        feedback = self._resolve_feedback()
        state = self._automation_service.state
        return MainWindowSnapshot(
            title="Turkuaz ClickFlow",
            status=state.value,
            cps=settings.cps,
            hotkey=settings.hotkey,
            click_count=self._automation_service.counter.value,
            elapsed_time=self._format_elapsed(self._automation_service.elapsed_seconds),
            target_window=settings.target_window or "Seçilmedi",
            window_guard_enabled=settings.window_guard_enabled,
            message=feedback.text,
            message_level=feedback.level,
            start_enabled=state.can_start,
            stop_enabled=state.can_stop,
        )

    def _resolve_feedback(self) -> FeedbackMessage:
        state = self._automation_service.state
        if self._last_feedback is not None:
            if state is AutomationState.RUNNING:
                return self._last_feedback
            if self._automation_service.stop_reason is not None:
                return self._last_feedback
        return self._feedback_service.current_message(
            state,
            self._automation_service.stop_reason,
        )

    @staticmethod
    def _format_elapsed(elapsed_seconds: float) -> str:
        total_seconds = max(0, int(elapsed_seconds))
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
