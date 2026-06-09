"""Click counter domain model."""

from dataclasses import dataclass


@dataclass
class ClickCounter:
    """Tracks successful clicks for the current automation run."""

    value: int = 0

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("counter value cannot be negative")

    def increment(self, amount: int = 1) -> int:
        """Increase the counter and return the new value."""
        if amount <= 0:
            raise ValueError("increment amount must be greater than 0")
        self.value += amount
        return self.value

    def reset_for_new_run(self) -> None:
        """Reset the counter when a new automation run starts."""
        self.value = 0
