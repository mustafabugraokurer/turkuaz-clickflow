"""Hotkey command routing for automation control."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.app.automation_service import (
    AutomationCommandResult,
    AutomationService,
)
from turkuaz_clickflow.domain.automation_settings import AutomationSettings
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


@dataclass(frozen=True)
class HotkeyResult:
    """Result returned after a hotkey trigger is processed."""

    accepted: bool
    hotkey: str
    action: str
    automation_result: Optional[AutomationCommandResult] = None
    message: str = ""


class HotkeyService:
    """Maps hotkey triggers to AutomationService commands.

    This class does not register OS-level global shortcuts. Platform adapters will
    call this service after they detect a supported hotkey event.
    """

    def __init__(
        self,
        automation_service: AutomationService,
        hotkey: str = AutomationSettings.defaults().hotkey,
    ) -> None:
        normalized = self._normalize(hotkey)
        if not normalized:
            raise ValueError("hotkey must not be empty")
        self._automation_service = automation_service
        self._hotkey = normalized

    @property
    def hotkey(self) -> str:
        """Configured hotkey label."""
        return self._hotkey

    def trigger(self, hotkey: str) -> HotkeyResult:
        """Handle a hotkey trigger with start/stop toggle behavior."""
        normalized = self._normalize(hotkey)
        if normalized != self._hotkey:
            return HotkeyResult(
                accepted=False,
                hotkey=normalized,
                action="rejected",
                message=f"Unsupported hotkey: {hotkey}",
            )

        if self._automation_service.state is AutomationState.RUNNING:
            result = self._automation_service.stop(reason=StopReason.HOTKEY_STOPPED)
            return HotkeyResult(
                accepted=True,
                hotkey=normalized,
                action="stop",
                automation_result=result,
                message="Hotkey stopped automation",
            )

        result = self._automation_service.start()
        return HotkeyResult(
            accepted=result.accepted,
            hotkey=normalized,
            action="start",
            automation_result=result,
            message="Hotkey started automation" if result.accepted else result.message,
        )

    @staticmethod
    def _normalize(hotkey: str) -> str:
        return hotkey.strip().upper()

