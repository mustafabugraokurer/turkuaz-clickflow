"""Start/stop orchestration for click automation."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.domain.automation_settings import AutomationSettings
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.counter import ClickCounter
from turkuaz_clickflow.domain.cps_policy import InvalidCpsError
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.app.timer_service import TimerService


@dataclass(frozen=True)
class AutomationCommandResult:
    """Result returned by start/stop commands."""

    accepted: bool
    state: AutomationState
    started: bool = False
    stopped: bool = False
    stop_reason: Optional[StopReason] = None
    message: str = ""


class AutomationService:
    """Coordinates automation lifecycle state without performing OS actions."""

    def __init__(
        self,
        counter: Optional[ClickCounter] = None,
        timer: Optional[TimerService] = None,
    ) -> None:
        self._state = AutomationState.READY
        self._counter = counter or ClickCounter()
        self._timer = timer or TimerService()
        self._settings = AutomationSettings.defaults()
        self._stop_reason: Optional[StopReason] = None
        self._run_count = 0

    @property
    def state(self) -> AutomationState:
        """Current automation lifecycle state."""
        return self._state

    @property
    def counter(self) -> ClickCounter:
        """Click counter owned by the service."""
        return self._counter

    @property
    def elapsed_seconds(self) -> float:
        """Elapsed seconds for the current or latest run."""
        return self._timer.elapsed_seconds()

    @property
    def settings(self) -> AutomationSettings:
        """Settings for the current or latest run."""
        return self._settings

    @property
    def stop_reason(self) -> Optional[StopReason]:
        """Latest stop reason, if any."""
        return self._stop_reason

    @property
    def run_count(self) -> int:
        """Number of accepted starts that created a new run."""
        return self._run_count

    def start(
        self,
        settings: Optional[AutomationSettings] = None,
        *,
        cps: Optional[int] = None,
    ) -> AutomationCommandResult:
        """Start automation if the current state and settings allow it."""
        if self._state is AutomationState.RUNNING:
            return AutomationCommandResult(
                accepted=True,
                state=self._state,
                started=False,
                message="Automation is already running",
            )

        try:
            next_settings = self._resolve_settings(settings=settings, cps=cps)
        except (InvalidCpsError, ValueError) as exc:
            self._state = AutomationState.ERROR
            self._stop_reason = StopReason.INVALID_SETTINGS
            return AutomationCommandResult(
                accepted=False,
                state=self._state,
                started=False,
                stop_reason=self._stop_reason,
                message=str(exc),
            )

        if not self._state.can_start:
            return AutomationCommandResult(
                accepted=False,
                state=self._state,
                started=False,
                stop_reason=self._stop_reason,
                message=f"Cannot start from {self._state.value} state",
            )

        self._settings = next_settings
        self._counter.reset_for_new_run()
        self._timer.start_new_run()
        self._stop_reason = None
        self._state = AutomationState.RUNNING
        self._run_count += 1
        return AutomationCommandResult(
            accepted=True,
            state=self._state,
            started=True,
            message="Automation started",
        )

    def stop(
        self, reason: StopReason = StopReason.USER_STOPPED
    ) -> AutomationCommandResult:
        """Safely accept a stop command in any lifecycle state."""
        if self._state is AutomationState.RUNNING:
            self._state = AutomationState.STOPPING
            self._stop_reason = reason
            self._timer.stop()
            self._state = AutomationState.STOPPED
            return AutomationCommandResult(
                accepted=True,
                state=self._state,
                stopped=True,
                stop_reason=self._stop_reason,
                message="Automation stopped",
            )

        if self._state is AutomationState.ERROR and self._stop_reason is not None:
            return AutomationCommandResult(
                accepted=True,
                state=self._state,
                stopped=False,
                stop_reason=self._stop_reason,
                message="Automation is not running",
            )

        self._stop_reason = reason
        if self._state in {AutomationState.READY, AutomationState.STOPPING}:
            self._state = AutomationState.STOPPED
        return AutomationCommandResult(
            accepted=True,
            state=self._state,
            stopped=False,
            stop_reason=self._stop_reason,
            message="Automation is not running",
        )

    def record_successful_click(self, amount: int = 1) -> int:
        """Record successful clicks reported by a future click runner."""
        if self._state is not AutomationState.RUNNING:
            raise RuntimeError("cannot record clicks while automation is not running")
        return self._counter.increment(amount)

    def _resolve_settings(
        self,
        settings: Optional[AutomationSettings],
        cps: Optional[int],
    ) -> AutomationSettings:
        if settings is not None and cps is not None:
            raise ValueError("settings and cps cannot be provided together")
        if settings is not None:
            return settings
        if cps is not None:
            return AutomationSettings(cps=cps)
        return AutomationSettings.defaults()
