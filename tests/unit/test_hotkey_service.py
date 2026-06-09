import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.hotkey_service import HotkeyService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


class HotkeyServiceTest(unittest.TestCase):
    def test_f8_starts_when_stopped(self) -> None:
        automation = AutomationService()
        hotkeys = HotkeyService(automation)

        result = hotkeys.trigger("F8")

        self.assertTrue(result.accepted)
        self.assertEqual(result.action, "start")
        self.assertIsNotNone(result.automation_result)
        self.assertTrue(result.automation_result.started)  # type: ignore[union-attr]
        self.assertEqual(automation.state, AutomationState.RUNNING)

    def test_f8_stops_when_running(self) -> None:
        automation = AutomationService()
        hotkeys = HotkeyService(automation)
        hotkeys.trigger("F8")

        result = hotkeys.trigger("F8")

        self.assertTrue(result.accepted)
        self.assertEqual(result.action, "stop")
        self.assertIsNotNone(result.automation_result)
        self.assertTrue(result.automation_result.stopped)  # type: ignore[union-attr]
        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(automation.stop_reason, StopReason.HOTKEY_STOPPED)

    def test_invalid_hotkey_is_rejected(self) -> None:
        automation = AutomationService()
        hotkeys = HotkeyService(automation)

        result = hotkeys.trigger("F7")

        self.assertFalse(result.accepted)
        self.assertEqual(result.action, "rejected")
        self.assertIsNone(result.automation_result)
        self.assertEqual(automation.state, AutomationState.READY)

    def test_hotkey_behavior_matches_start_stop_commands(self) -> None:
        manual = AutomationService()
        manual_start = manual.start()
        manual_stop = manual.stop(reason=StopReason.HOTKEY_STOPPED)

        via_hotkey = AutomationService()
        hotkeys = HotkeyService(via_hotkey)
        hotkey_start = hotkeys.trigger("F8").automation_result
        hotkey_stop = hotkeys.trigger("F8").automation_result

        self.assertIsNotNone(hotkey_start)
        self.assertIsNotNone(hotkey_stop)
        self.assertEqual(hotkey_start.state, manual_start.state)  # type: ignore[union-attr]
        self.assertEqual(hotkey_stop.state, manual_stop.state)  # type: ignore[union-attr]
        self.assertEqual(hotkey_stop.stop_reason, manual_stop.stop_reason)  # type: ignore[union-attr]

    def test_hotkey_normalization_accepts_lowercase_f8(self) -> None:
        automation = AutomationService()
        hotkeys = HotkeyService(automation)

        result = hotkeys.trigger(" f8 ")

        self.assertTrue(result.accepted)
        self.assertEqual(result.hotkey, "F8")
        self.assertEqual(automation.state, AutomationState.RUNNING)

    def test_empty_configured_hotkey_is_invalid(self) -> None:
        with self.assertRaises(ValueError):
            HotkeyService(AutomationService(), hotkey=" ")


if __name__ == "__main__":
    unittest.main()

