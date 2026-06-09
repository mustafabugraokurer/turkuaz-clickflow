import unittest

from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


class AutomationStateTest(unittest.TestCase):
    def test_automation_states_are_defined(self) -> None:
        self.assertEqual(
            {state.value for state in AutomationState},
            {
                "ready",
                "running",
                "stopping",
                "stopped",
                "error",
            },
        )

    def test_start_is_allowed_only_from_ready_or_stopped(self) -> None:
        self.assertTrue(AutomationState.READY.can_start)
        self.assertTrue(AutomationState.STOPPED.can_start)
        self.assertFalse(AutomationState.RUNNING.can_start)
        self.assertFalse(AutomationState.STOPPING.can_start)
        self.assertFalse(AutomationState.ERROR.can_start)

    def test_stop_is_allowed_only_while_running(self) -> None:
        self.assertTrue(AutomationState.RUNNING.can_stop)
        self.assertFalse(AutomationState.READY.can_stop)
        self.assertFalse(AutomationState.STOPPING.can_stop)
        self.assertFalse(AutomationState.STOPPED.can_stop)
        self.assertFalse(AutomationState.ERROR.can_stop)

    def test_terminal_states_are_defined(self) -> None:
        self.assertTrue(AutomationState.STOPPED.is_terminal)
        self.assertTrue(AutomationState.ERROR.is_terminal)
        self.assertFalse(AutomationState.READY.is_terminal)
        self.assertFalse(AutomationState.RUNNING.is_terminal)
        self.assertFalse(AutomationState.STOPPING.is_terminal)

    def test_stop_reasons_are_defined(self) -> None:
        self.assertEqual(
            {reason.value for reason in StopReason},
            {
                "user_stopped",
                "hotkey_stopped",
                "invalid_settings",
                "window_changed",
                "target_window_missing",
                "error",
            },
        )


if __name__ == "__main__":
    unittest.main()
