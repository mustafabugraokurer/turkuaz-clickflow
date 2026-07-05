"""View model for the MVP main window."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.app.hotkey_service import HotkeyResult, HotkeyService
from turkuaz_clickflow.domain.automation_settings import AutomationSettings
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.cps_policy import CpsPolicy
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import WindowInfo, WindowQueryAdapter


@dataclass(frozen=True)
class MainWindowSnapshot:
    """Display values for the main window."""

    title: str
    status: str
    cps: int
    hotkey: str
    click_count: int
    elapsed_time: str
    available_target_windows: tuple[WindowInfo, ...]
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
        window_query: Optional[WindowQueryAdapter] = None,
    ) -> None:
        self._automation_service = automation_service
        self._feedback_service = feedback_service
        self._hotkey_service = hotkey_service or HotkeyService(automation_service)
        self._window_query = window_query
        self._last_feedback: Optional[FeedbackMessage] = None
        self._selected_cps = automation_service.settings.cps
        self._selected_target_window_id = automation_service.settings.target_window_id
        self._selected_target_window_title = automation_service.settings.target_window
        self._window_guard_enabled = automation_service.settings.window_guard_enabled
        self._available_target_windows: tuple[WindowInfo, ...] = ()
        self.refresh_available_windows()

    @property
    def selected_cps(self) -> int:
        """CPS value selected by the user for the next run."""
        return self._selected_cps

    def set_cps(self, cps: int) -> MainWindowSnapshot:
        """Store the user's CPS selection without starting automation."""
        CpsPolicy().validate(cps)
        self._selected_cps = cps
        return self.snapshot()

    def select_target_window(self, window_id: Optional[str]) -> MainWindowSnapshot:
        """Store the target window selection for the next run."""
        self.refresh_available_windows()
        if not window_id:
            self._selected_target_window_id = None
            self._selected_target_window_title = None
            return self.snapshot()

        selected = next(
            (
                window
                for window in self._available_target_windows
                if window.id == window_id
            ),
            None,
        )
        if selected is None:
            self._selected_target_window_id = None
            self._selected_target_window_title = None
            return self.snapshot()

        self._selected_target_window_id = selected.id
        self._selected_target_window_title = selected.title
        return self.snapshot()

    def set_window_guard_enabled(self, enabled: bool) -> MainWindowSnapshot:
        """Store the window-guard toggle for the next run."""
        self._window_guard_enabled = enabled
        return self.snapshot()

    def start(self, cps: int) -> MainWindowSnapshot:
        """Start automation through the app service and return refreshed UI state."""
        try:
            settings = self._build_settings(cps)
        except ValueError:
            result = self._automation_service.start(cps=cps)
            self._last_feedback = self._feedback_service.for_automation_result(result)
            return self.snapshot()

        result = self._automation_service.start(settings=settings)
        if result.accepted:
            self._selected_cps = self._automation_service.settings.cps
            self._selected_target_window_id = (
                self._automation_service.settings.target_window_id
            )
            self._selected_target_window_title = (
                self._automation_service.settings.target_window
            )
            self._window_guard_enabled = (
                self._automation_service.settings.window_guard_enabled
            )
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
        self.refresh_available_windows()
        settings = self._automation_service.settings
        feedback = self._resolve_feedback()
        state = self._automation_service.state
        displayed_cps = (
            settings.cps if state is AutomationState.RUNNING else self._selected_cps
        )
        displayed_target_window = (
            settings.target_window
            if state is AutomationState.RUNNING
            else self._selected_target_window_title
        )
        displayed_window_guard = (
            settings.window_guard_enabled
            if state is AutomationState.RUNNING
            else self._window_guard_enabled
        )
        return MainWindowSnapshot(
            title="Turkuaz ClickFlow",
            status=state.value,
            cps=displayed_cps,
            hotkey=settings.hotkey,
            click_count=self._automation_service.counter.value,
            elapsed_time=self._format_elapsed(self._automation_service.elapsed_seconds),
            available_target_windows=self._available_target_windows,
            target_window=displayed_target_window or "Seçilmedi",
            window_guard_enabled=displayed_window_guard,
            message=feedback.text,
            message_level=feedback.level,
            start_enabled=state.can_start,
            stop_enabled=state.can_stop,
        )

    def refresh_available_windows(self) -> tuple[WindowInfo, ...]:
        """Refresh user-selectable windows from the platform adapter."""
        if self._window_query is None:
            self._available_target_windows = ()
            return self._available_target_windows

        self._available_target_windows = tuple(self._window_query.list_windows())
        if self._selected_target_window_id is None:
            return self._available_target_windows

        selected = next(
            (
                window
                for window in self._available_target_windows
                if window.id == self._selected_target_window_id
            ),
            None,
        )
        if selected is None:
            self._selected_target_window_id = None
            self._selected_target_window_title = None
        else:
            self._selected_target_window_title = selected.title
        return self._available_target_windows

    def _build_settings(self, cps: int) -> AutomationSettings:
        return AutomationSettings(
            cps=cps,
            hotkey=self._automation_service.settings.hotkey,
            target_window_id=self._selected_target_window_id,
            target_window=self._selected_target_window_title,
            window_guard_enabled=self._window_guard_enabled,
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
