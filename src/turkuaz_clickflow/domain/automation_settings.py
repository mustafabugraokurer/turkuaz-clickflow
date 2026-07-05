"""Automation settings used by the domain and app layers."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.domain.cps_policy import CpsPolicy


@dataclass(frozen=True)
class AutomationSettings:
    """Settings for a single automation run."""

    cps: int = CpsPolicy().default
    hotkey: str = "F8"
    target_window_id: Optional[str] = None
    target_window: Optional[str] = None
    window_guard_enabled: bool = False

    def __post_init__(self) -> None:
        policy = CpsPolicy()
        policy.validate(self.cps)
        if not self.hotkey.strip():
            raise ValueError("hotkey must not be empty")

    @classmethod
    def defaults(cls) -> "AutomationSettings":
        """Create settings from Sprint-1 product defaults."""
        return cls()
