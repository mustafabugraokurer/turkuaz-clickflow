"""CPS-driven click loop orchestration."""

from dataclasses import dataclass
from time import sleep
from typing import Callable, Optional

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import (
    MouseClickAdapter,
    PlatformOperationError,
)


Sleeper = Callable[[float], None]


@dataclass(frozen=True)
class ClickRunnerResult:
    """Result of a bounded click runner execution."""

    attempted_clicks: int
    successful_clicks: int
    stopped: bool
    stop_reason: Optional[StopReason] = None
    error_message: str = ""


class ClickRunner:
    """Runs left clicks while automation remains in running state."""

    def __init__(
        self,
        automation_service: AutomationService,
        mouse: MouseClickAdapter,
        sleeper: Sleeper = sleep,
    ) -> None:
        self._automation_service = automation_service
        self._mouse = mouse
        self._sleeper = sleeper

    @property
    def click_interval_seconds(self) -> float:
        """Delay between clicks derived from current CPS settings."""
        return 1.0 / self._automation_service.settings.cps

    def run_once(self) -> ClickRunnerResult:
        """Attempt a single click if automation is running."""
        return self.run_steps(max_clicks=1)

    def run_steps(self, max_clicks: int) -> ClickRunnerResult:
        """Run at most ``max_clicks`` clicks.

        The method is intentionally bounded so unit tests and future UI wiring
        can control scheduling without starting an uncontrolled infinite loop.
        """
        if max_clicks < 0:
            raise ValueError("max_clicks cannot be negative")

        attempted = 0
        successful = 0

        for index in range(max_clicks):
            if self._automation_service.state is not AutomationState.RUNNING:
                break

            if index > 0:
                self._sleeper(self.click_interval_seconds)
                if self._automation_service.state is not AutomationState.RUNNING:
                    break

            attempted += 1
            try:
                self._mouse.left_click()
                self._automation_service.record_successful_click()
            except (PlatformOperationError, RuntimeError) as exc:
                stop_result = self._automation_service.stop(reason=StopReason.ERROR)
                return ClickRunnerResult(
                    attempted_clicks=attempted,
                    successful_clicks=successful,
                    stopped=True,
                    stop_reason=stop_result.stop_reason,
                    error_message=str(exc),
                )

            successful += 1

        return ClickRunnerResult(
            attempted_clicks=attempted,
            successful_clicks=successful,
            stopped=self._automation_service.state is not AutomationState.RUNNING,
            stop_reason=self._automation_service.stop_reason,
        )
