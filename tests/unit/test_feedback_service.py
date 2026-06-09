import unittest

from turkuaz_clickflow.app.automation_service import AutomationCommandResult, AutomationService
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.app.hotkey_service import HotkeyResult
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


class FeedbackServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.feedback = FeedbackService()

    def test_ready_message_is_action_oriented(self) -> None:
        message = self.feedback.for_state(AutomationState.READY)

        self.assertEqual(message.level, "info")
        self.assertEqual(
            message.text,
            "Hazır. Başlatmak için Start'a basın veya F8 kullanın.",
        )

    def test_running_message_mentions_stop_controls(self) -> None:
        message = self.feedback.for_state(AutomationState.RUNNING)

        self.assertEqual(message.level, "info")
        self.assertIn("Stop", message.text)
        self.assertIn("F8", message.text)

    def test_stop_reason_messages_are_user_facing(self) -> None:
        self.assertEqual(
            self.feedback.for_stop_reason(StopReason.USER_STOPPED).text,
            "Durdu. Son durma sebebi: Kullanıcı durdurdu.",
        )
        self.assertEqual(
            self.feedback.for_stop_reason(StopReason.HOTKEY_STOPPED).text,
            "Durdu. Son durma sebebi: F8 ile durduruldu.",
        )

    def test_invalid_settings_message_tells_user_what_to_fix(self) -> None:
        message = self.feedback.for_stop_reason(StopReason.INVALID_SETTINGS)

        self.assertEqual(message.level, "warning")
        self.assertEqual(message.text, "CPS değeri 1 ile 100 arasında olmalıdır.")

    def test_error_message_avoids_technical_detail(self) -> None:
        message = self.feedback.for_stop_reason(StopReason.ERROR)

        self.assertEqual(message.level, "error")
        self.assertEqual(message.text, "Hata nedeniyle durdu. Lütfen tekrar deneyin.")

    def test_automation_result_prefers_stop_reason(self) -> None:
        result = AutomationCommandResult(
            accepted=False,
            state=AutomationState.ERROR,
            stop_reason=StopReason.INVALID_SETTINGS,
            message="CPS must be between 1 and 100",
        )

        message = self.feedback.for_automation_result(result)

        self.assertEqual(message.text, "CPS değeri 1 ile 100 arasında olmalıdır.")

    def test_automation_start_result_returns_running_message(self) -> None:
        result = AutomationService().start(cps=10)

        message = self.feedback.for_automation_result(result)

        self.assertEqual(
            message.text,
            "Çalışıyor. Durdurmak için Stop'a basın veya F8 kullanın.",
        )

    def test_hotkey_rejection_returns_hotkey_warning(self) -> None:
        result = HotkeyResult(
            accepted=False,
            hotkey="F7",
            action="rejected",
            message="Unsupported hotkey: F7",
        )

        message = self.feedback.for_hotkey_result(result)

        self.assertEqual(message.level, "warning")
        self.assertEqual(
            message.text,
            "Kısayol kullanılamıyor. F8 başka bir uygulama tarafından kullanılıyor olabilir.",
        )

    def test_current_message_prefers_stop_reason(self) -> None:
        message = self.feedback.current_message(
            AutomationState.STOPPED,
            StopReason.WINDOW_CHANGED,
        )

        self.assertEqual(
            message.text,
            "Durdu. Son durma sebebi: Pencere değişti.",
        )


if __name__ == "__main__":
    unittest.main()

