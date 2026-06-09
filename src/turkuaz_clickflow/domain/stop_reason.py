"""Reasons why automation can stop."""

from enum import Enum


class StopReason(str, Enum):
    """User-visible stop reason identifiers."""

    USER_STOPPED = "user_stopped"
    HOTKEY_STOPPED = "hotkey_stopped"
    INVALID_SETTINGS = "invalid_settings"
    WINDOW_CHANGED = "window_changed"
    TARGET_WINDOW_MISSING = "target_window_missing"
    ERROR = "error"
