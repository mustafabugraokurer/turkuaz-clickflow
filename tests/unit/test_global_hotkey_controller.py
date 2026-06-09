import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.app.global_hotkey_controller import GlobalHotkeyController
from turkuaz_clickflow.app.hotkey_service import HotkeyService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import PlatformOperationError


class FakeHotkeyAdapter:
    def __init__(self) -> None:
        self.registered_hotkey = ""
        self.callback = None
        self.unregistered_hotkey = ""

    def register(self, hotkey: str, callback) -> None:
        self.registered_hotkey = hotkey
        self.callback = callback

    def unregister(self, hotkey: str) -> None:
        self.unregistered_hotkey = hotkey

    def trigger(self) -> None:
        self.callback()


class FailingHotkeyAdapter:
    def register(self, hotkey: str, callback) -> None:
        raise PlatformOperationError("hotkey unavailable")

    def unregister(self, hotkey: str) -> None:
        raise PlatformOperationError("hotkey unavailable")


class GlobalHotkeyControllerTest(unittest.TestCase):
    def test_register_binds_adapter_callback_to_hotkey_service(self) -> None:
        automation = AutomationService()
        adapter = FakeHotkeyAdapter()
        trigger_actions = []
        controller = GlobalHotkeyController(
            adapter=adapter,
            hotkey_service=HotkeyService(automation),
            feedback_service=FeedbackService(),
            on_trigger=lambda result: trigger_actions.append(result.action),
        )

        result = controller.register()
        adapter.trigger()

        self.assertTrue(result.accepted)
        self.assertEqual(adapter.registered_hotkey, "F8")
        self.assertEqual(automation.state, AutomationState.RUNNING)
        self.assertIsNotNone(controller.last_hotkey_result)
        self.assertEqual(controller.last_hotkey_result.action, "start")
        self.assertEqual(trigger_actions, ["start"])

    def test_second_callback_stops_with_hotkey_reason(self) -> None:
        automation = AutomationService()
        adapter = FakeHotkeyAdapter()
        controller = GlobalHotkeyController(
            adapter=adapter,
            hotkey_service=HotkeyService(automation),
            feedback_service=FeedbackService(),
        )
        controller.register()

        adapter.trigger()
        adapter.trigger()

        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(automation.stop_reason, StopReason.HOTKEY_STOPPED)

    def test_register_failure_returns_user_facing_warning(self) -> None:
        automation = AutomationService()
        controller = GlobalHotkeyController(
            adapter=FailingHotkeyAdapter(),
            hotkey_service=HotkeyService(automation),
            feedback_service=FeedbackService(),
        )

        result = controller.register()

        self.assertFalse(result.accepted)
        self.assertEqual(result.message.level, "warning")
        self.assertIn("Kısayol kullanılamıyor", result.message.text)
        self.assertEqual(automation.state, AutomationState.READY)

    def test_unregister_removes_registered_hotkey(self) -> None:
        automation = AutomationService()
        adapter = FakeHotkeyAdapter()
        controller = GlobalHotkeyController(
            adapter=adapter,
            hotkey_service=HotkeyService(automation),
            feedback_service=FeedbackService(),
        )
        controller.register()

        controller.unregister()

        self.assertEqual(adapter.unregistered_hotkey, "F8")


if __name__ == "__main__":
    unittest.main()
