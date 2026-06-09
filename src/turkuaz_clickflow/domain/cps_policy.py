"""CPS validation rules for the MVP click automation domain."""

from dataclasses import dataclass


class InvalidCpsError(ValueError):
    """Raised when a CPS value is outside the supported MVP range."""


@dataclass(frozen=True)
class CpsPolicy:
    """Defines the supported clicks-per-second range."""

    minimum: int = 1
    maximum: int = 100
    default: int = 10

    def __post_init__(self) -> None:
        if self.minimum <= 0:
            raise ValueError("minimum CPS must be greater than 0")
        if self.maximum < self.minimum:
            raise ValueError("maximum CPS must be greater than or equal to minimum CPS")
        if not self.minimum <= self.default <= self.maximum:
            raise ValueError("default CPS must be within the supported range")

    def validate(self, cps: int) -> int:
        """Return a valid CPS value or raise InvalidCpsError."""
        if not isinstance(cps, int):
            raise InvalidCpsError("CPS must be an integer")
        if cps < self.minimum or cps > self.maximum:
            raise InvalidCpsError(
                f"CPS must be between {self.minimum} and {self.maximum}"
            )
        return cps

    def default_value(self) -> int:
        """Return the configured default CPS value."""
        return self.default
