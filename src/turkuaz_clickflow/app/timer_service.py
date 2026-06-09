"""Elapsed time tracking for automation runs."""

from time import monotonic
from typing import Callable, Optional


class TimerService:
    """Tracks elapsed seconds for the current or latest run."""

    def __init__(self, clock: Callable[[], float] = monotonic) -> None:
        self._clock = clock
        self._started_at: Optional[float] = None
        self._elapsed_seconds = 0.0

    @property
    def is_running(self) -> bool:
        """Whether the timer is currently running."""
        return self._started_at is not None

    def start_new_run(self) -> None:
        """Reset elapsed time and start timing a new automation run."""
        self._elapsed_seconds = 0.0
        self._started_at = self._clock()

    def stop(self) -> None:
        """Freeze elapsed time for display after the run stops."""
        if self._started_at is None:
            return
        self._elapsed_seconds += self._clock() - self._started_at
        self._started_at = None

    def reset(self) -> None:
        """Clear elapsed time and stop the timer."""
        self._started_at = None
        self._elapsed_seconds = 0.0

    def elapsed_seconds(self) -> float:
        """Return elapsed seconds without stopping the timer."""
        if self._started_at is None:
            return self._elapsed_seconds
        return self._elapsed_seconds + (self._clock() - self._started_at)

