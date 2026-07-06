"""Persistence for user-selected automation settings."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Protocol

from turkuaz_clickflow.domain.automation_settings import AutomationSettings


class SettingsRepository(Protocol):
    """Contract for loading and saving user settings."""

    def load(self) -> AutomationSettings:
        """Load persisted settings or defaults."""

    def save(self, settings: AutomationSettings) -> None:
        """Persist settings for future app launches."""


class NullSettingsRepository:
    """Settings repository used when persistence is not needed."""

    def load(self) -> AutomationSettings:
        return AutomationSettings.defaults()

    def save(self, settings: AutomationSettings) -> None:
        del settings


class JsonSettingsRepository:
    """JSON-backed settings repository."""

    VERSION = 1

    def __init__(self, path: Path) -> None:
        self._path = path

    @property
    def path(self) -> Path:
        """Config file path."""
        return self._path

    def load(self) -> AutomationSettings:
        """Load settings, falling back to defaults on missing or invalid config."""
        try:
            raw = json.loads(self._path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                return AutomationSettings.defaults()
            return self._settings_from_dict(raw)
        except (OSError, json.JSONDecodeError, TypeError, ValueError, AttributeError):
            return AutomationSettings.defaults()

    def save(self, settings: AutomationSettings) -> None:
        """Persist settings as stable JSON."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        payload = self._settings_to_dict(settings)
        self._path.write_text(
            json.dumps(payload, indent=2, sort_keys=True),
            encoding="utf-8",
        )

    @classmethod
    def _settings_from_dict(cls, raw: Dict[str, Any]) -> AutomationSettings:
        return AutomationSettings(
            cps=raw.get("cps", AutomationSettings.defaults().cps),
            hotkey=cls._str_or_default(
                raw.get("hotkey"),
                AutomationSettings.defaults().hotkey,
            ),
            target_window_id=cls._optional_str(raw.get("target_window_id")),
            target_window=cls._optional_str(raw.get("target_window")),
            window_guard_enabled=cls._bool_or_default(
                raw.get("window_guard_enabled"),
                False,
            ),
        )

    @classmethod
    def _settings_to_dict(cls, settings: AutomationSettings) -> Dict[str, Any]:
        return {
            "version": cls.VERSION,
            "cps": settings.cps,
            "hotkey": settings.hotkey,
            "target_window_id": settings.target_window_id,
            "target_window": settings.target_window,
            "window_guard_enabled": settings.window_guard_enabled,
        }

    @staticmethod
    def _optional_str(value: Any) -> Optional[str]:
        if value in (None, ""):
            return None
        return str(value)

    @staticmethod
    def _str_or_default(value: Any, default: str) -> str:
        if not isinstance(value, str):
            return default
        return value

    @staticmethod
    def _bool_or_default(value: Any, default: bool) -> bool:
        if not isinstance(value, bool):
            return default
        return value


def default_settings_path(
    system_platform: str = sys.platform,
    home: Optional[Path] = None,
) -> Path:
    """Return a platform-appropriate user config path."""
    base_home = home or Path.home()
    if system_platform.startswith("win"):
        app_data = os.environ.get("APPDATA")
        base = Path(app_data) if app_data else base_home / "AppData" / "Roaming"
        return base / "Turkuaz" / "ClickFlow" / "settings.json"
    if system_platform == "darwin":
        return (
            base_home
            / "Library"
            / "Application Support"
            / "Turkuaz"
            / "ClickFlow"
            / "settings.json"
        )
    return base_home / ".config" / "turkuaz-clickflow" / "settings.json"


def create_settings_repository() -> SettingsRepository:
    """Create the default settings repository for the current user."""
    return JsonSettingsRepository(default_settings_path())
