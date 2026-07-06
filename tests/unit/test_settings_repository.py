import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from turkuaz_clickflow.config.settings_repository import (
    JsonSettingsRepository,
    default_settings_path,
)
from turkuaz_clickflow.domain.automation_settings import AutomationSettings


class SettingsRepositoryTest(unittest.TestCase):
    def test_missing_config_loads_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repository = JsonSettingsRepository(Path(tmpdir) / "settings.json")

            settings = repository.load()

        self.assertEqual(settings, AutomationSettings.defaults())

    def test_save_and_load_roundtrip_preserves_settings(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repository = JsonSettingsRepository(Path(tmpdir) / "settings.json")
            original = AutomationSettings(
                cps=25,
                hotkey="F8",
                target_window_id="window-1",
                target_window="Example",
                window_guard_enabled=True,
            )

            repository.save(original)
            loaded = repository.load()

        self.assertEqual(loaded, original)

    def test_invalid_json_loads_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "settings.json"
            path.write_text("{broken", encoding="utf-8")
            repository = JsonSettingsRepository(path)

            settings = repository.load()

        self.assertEqual(settings, AutomationSettings.defaults())

    def test_invalid_settings_values_load_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "settings.json"
            path.write_text(json.dumps({"cps": 101, "hotkey": "F8"}), encoding="utf-8")
            repository = JsonSettingsRepository(path)

            settings = repository.load()

        self.assertEqual(settings, AutomationSettings.defaults())

    def test_invalid_hotkey_type_loads_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "settings.json"
            path.write_text(json.dumps({"cps": 10, "hotkey": 8}), encoding="utf-8")
            repository = JsonSettingsRepository(path)

            settings = repository.load()

        self.assertEqual(settings, AutomationSettings.defaults())

    def test_windows_default_settings_path_uses_appdata(self) -> None:
        with patch.dict(os.environ, {"APPDATA": r"C:\Users\Ada\AppData\Roaming"}):
            path = default_settings_path("win32", home=Path("/ignored"))

        self.assertEqual(
            str(path),
            r"C:\Users\Ada\AppData\Roaming/Turkuaz/ClickFlow/settings.json",
        )

    def test_macos_default_settings_path_uses_application_support(self) -> None:
        path = default_settings_path("darwin", home=Path("/Users/ada"))

        self.assertEqual(
            path,
            Path("/Users/ada/Library/Application Support/Turkuaz/ClickFlow/settings.json"),
        )

    def test_linux_default_settings_path_uses_config_dir(self) -> None:
        path = default_settings_path("linux", home=Path("/home/ada"))

        self.assertEqual(path, Path("/home/ada/.config/turkuaz-clickflow/settings.json"))


if __name__ == "__main__":
    unittest.main()
