"""Automation lifecycle states."""

from enum import Enum


class AutomationState(str, Enum):
    """States shown by the UI and used by the app layer."""

    READY = "ready"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"

    @property
    def can_start(self) -> bool:
        """Whether a Start command may be accepted in this state."""
        return self in {AutomationState.READY, AutomationState.STOPPED}

    @property
    def can_stop(self) -> bool:
        """Whether a Stop command may be accepted in this state."""
        return self is AutomationState.RUNNING

    @property
    def is_terminal(self) -> bool:
        """Whether the state represents a non-running end state."""
        return self in {AutomationState.STOPPED, AutomationState.ERROR}
