"""App-level binding between OS hotkey adapters and HotkeyService."""

from dataclasses import dataclass
from typing import Callable, Optional

from turkuaz_clickflow.app.feedback_service import FeedbackMessage, FeedbackService
from turkuaz_clickflow.app.hotkey_service import HotkeyResult, HotkeyService
from turkuaz_clickflow.platform.interfaces import (
    GlobalHotkeyAdapter,
    PlatformOperationError,
)


@dataclass(frozen=True)
class GlobalHotkeyRegistrationResult:
    """Result returned by OS hotkey registration actions."""

    accepted: bool
    hotkey: str
    message: FeedbackMessage
    error_message: str = ""


class GlobalHotkeyController:
    """Registers OS hotkeys and routes callbacks to HotkeyService."""

    def __init__(
        self,
        adapter: GlobalHotkeyAdapter,
        hotkey_service: HotkeyService,
        feedback_service: FeedbackService,
        on_trigger: Optional[Callable[[HotkeyResult], None]] = None,
    ) -> None:
        self._adapter = adapter
        self._hotkey_service = hotkey_service
        self._feedback_service = feedback_service
        self._on_trigger = on_trigger
        self._registered_hotkey: Optional[str] = None
        self._last_hotkey_result: Optional[HotkeyResult] = None

    @property
    def last_hotkey_result(self) -> Optional[HotkeyResult]:
        """Most recent HotkeyService result triggered by the OS adapter."""
        return self._last_hotkey_result

    def register(self, hotkey: Optional[str] = None) -> GlobalHotkeyRegistrationResult:
        """Register the configured hotkey with the OS adapter."""
        target_hotkey = hotkey or self._hotkey_service.hotkey
        try:
            self._adapter.register(target_hotkey, self._handle_hotkey)
        except PlatformOperationError as exc:
            rejected = HotkeyResult(
                accepted=False,
                hotkey=target_hotkey,
                action="register_failed",
                message=str(exc),
            )
            return GlobalHotkeyRegistrationResult(
                accepted=False,
                hotkey=target_hotkey,
                message=self._feedback_service.for_hotkey_result(rejected),
                error_message=str(exc),
            )

        self._registered_hotkey = target_hotkey
        return GlobalHotkeyRegistrationResult(
            accepted=True,
            hotkey=target_hotkey,
            message=FeedbackMessage(
                level="info",
                text=f"Kısayol hazır: {target_hotkey}",
            ),
        )

    def unregister(self) -> None:
        """Unregister the active OS hotkey, if one exists."""
        if self._registered_hotkey is None:
            return
        self._adapter.unregister(self._registered_hotkey)
        self._registered_hotkey = None

    def _handle_hotkey(self) -> None:
        self._last_hotkey_result = self._hotkey_service.trigger(
            self._hotkey_service.hotkey
        )
        if self._on_trigger is not None:
            self._on_trigger(self._last_hotkey_result)
