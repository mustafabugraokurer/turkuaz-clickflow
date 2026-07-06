import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_loop_controller import ClickLoopController
from turkuaz_clickflow.app.click_runner import ClickRunner
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.domain.automation_settings import AutomationSettings
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import PlatformOperationError, WindowInfo


class FakeScheduler:
    def __init__(self) -> None:
        self.started = False
        self.stopped = False
        self.interval_ms = 0
        self.callback = None

    def start(self, interval_ms: int, callback) -> None:
        self.started = True
        self.stopped = False
        self.interval_ms = interval_ms
        self.callback = callback

    def stop(self) -> None:
        self.stopped = True
        self.started = False

    def trigger(self) -> None:
        self.callback()


class FakeMouse:
    def __init__(self) -> None:
        self.clicks = 0

    def left_click(self) -> None:
        self.clicks += 1


class FailingMouse:
    def __init__(self, message: str = "click failed") -> None:
        self._message = message

    def left_click(self) -> None:
        raise PlatformOperationError(self._message)


class FakeWindowQuery:
    def __init__(self, windows=None, active=None) -> None:
        self._windows = list(windows or [])
        self._active = active

    def list_windows(self):
        return list(self._windows)

    def active_window(self):
        return self._active

    def set_windows(self, windows) -> None:
        self._windows = list(windows)

    def set_active(self, active) -> None:
        self._active = active


class BrokenRunner:
    def run_once(self):
        raise RuntimeError("runner exploded")

    @property
    def click_interval_seconds(self) -> float:
        return 0.1


class ClickLoopControllerTest(unittest.TestCase):
    def test_sync_starts_scheduler_when_automation_is_running(self) -> None:
        automation = AutomationService()
        automation.start(cps=20)
        scheduler = FakeScheduler()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, FakeMouse()),
            scheduler=scheduler,
            feedback_service=FeedbackService(),
        )

        result = controller.sync_with_automation()

        self.assertTrue(result.running)
        self.assertEqual(result.interval_ms, 50)
        self.assertTrue(scheduler.started)
        self.assertTrue(controller.is_running)

    def test_tick_runs_one_click_and_calls_update(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        mouse = FakeMouse()
        updates = []
        scheduler = FakeScheduler()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, mouse),
            scheduler=scheduler,
            feedback_service=FeedbackService(),
            on_update=lambda: updates.append("updated"),
        )
        controller.sync_with_automation()

        scheduler.trigger()

        self.assertEqual(mouse.clicks, 1)
        self.assertEqual(automation.counter.value, 1)
        self.assertEqual(updates, ["updated"])
        self.assertEqual(automation.state, AutomationState.RUNNING)

    def test_window_guard_allows_click_when_target_is_active(self) -> None:
        target = WindowInfo(id="1", title="Target")
        automation = AutomationService()
        automation.start(
            settings=AutomationSettings(
                cps=10,
                target_window_id="1",
                target_window="Target",
                window_guard_enabled=True,
            )
        )
        mouse = FakeMouse()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, mouse),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            window_query=FakeWindowQuery(windows=[target], active=target),
        )

        result = controller.tick()

        self.assertFalse(result.stopped)
        self.assertEqual(mouse.clicks, 1)
        self.assertEqual(automation.state, AutomationState.RUNNING)

    def test_window_guard_stops_before_click_when_active_window_changes(self) -> None:
        target = WindowInfo(id="1", title="Target")
        other = WindowInfo(id="2", title="Other")
        automation = AutomationService()
        automation.start(
            settings=AutomationSettings(
                cps=10,
                target_window_id="1",
                target_window="Target",
                window_guard_enabled=True,
            )
        )
        mouse = FakeMouse()
        feedback_messages = []
        scheduler = FakeScheduler()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, mouse),
            scheduler=scheduler,
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
            window_query=FakeWindowQuery(windows=[target, other], active=other),
        )
        controller.sync_with_automation()

        result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.WINDOW_CHANGED)
        self.assertEqual(mouse.clicks, 0)
        self.assertTrue(scheduler.stopped)
        self.assertEqual(
            feedback_messages,
            ["Durdu. Son durma sebebi: Pencere değişti."],
        )

    def test_window_guard_stops_when_target_window_is_missing(self) -> None:
        other = WindowInfo(id="2", title="Other")
        automation = AutomationService()
        automation.start(
            settings=AutomationSettings(
                cps=10,
                target_window_id="1",
                target_window="Target",
                window_guard_enabled=True,
            )
        )
        mouse = FakeMouse()
        feedback_messages = []
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, mouse),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
            window_query=FakeWindowQuery(windows=[other], active=other),
        )

        result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.TARGET_WINDOW_MISSING)
        self.assertEqual(mouse.clicks, 0)
        self.assertEqual(
            feedback_messages,
            ["Durdu. Son durma sebebi: Hedef pencere bulunamadı."],
        )

    def test_window_guard_stops_when_enabled_without_target_window(self) -> None:
        automation = AutomationService()
        automation.start(
            settings=AutomationSettings(
                cps=10,
                window_guard_enabled=True,
            )
        )
        mouse = FakeMouse()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, mouse),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            window_query=FakeWindowQuery(),
        )

        result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.TARGET_WINDOW_MISSING)
        self.assertEqual(mouse.clicks, 0)

    def test_sync_stops_scheduler_when_automation_stops(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        scheduler = FakeScheduler()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, FakeMouse()),
            scheduler=scheduler,
            feedback_service=FeedbackService(),
        )
        controller.sync_with_automation()

        automation.stop()
        result = controller.sync_with_automation()

        self.assertFalse(result.running)
        self.assertTrue(scheduler.stopped)
        self.assertFalse(controller.is_running)

    def test_runner_error_stops_scheduler_and_emits_feedback(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        feedback_messages = []
        scheduler = FakeScheduler()
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(automation, FailingMouse()),
            scheduler=scheduler,
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
        )
        controller.sync_with_automation()

        with self.assertLogs(
            "turkuaz_clickflow.app.click_loop_controller",
            level="ERROR",
        ) as logs:
            result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.ERROR)
        self.assertTrue(scheduler.stopped)
        self.assertFalse(controller.is_running)
        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(
            feedback_messages,
            ["İşlem başlatılamadı: click failed"],
        )
        self.assertIn("Click runner stopped with error: click failed", logs.output[0])

    def test_runner_permission_error_emits_macos_permission_message(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        feedback_messages = []
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(
                automation,
                FailingMouse("macOS Accessibility or Input Monitoring permission is required"),
            ),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
        )

        with self.assertLogs(
            "turkuaz_clickflow.app.click_loop_controller",
            level="ERROR",
        ):
            controller.tick()

        self.assertEqual(
            feedback_messages,
            [
                "macOS Accessibility izni gerekli olabilir. Sistem "
                "Ayarları > Gizlilik ve Güvenlik > Accessibility "
                "bölümünden uygulamaya izin verin."
            ],
        )
        self.assertEqual(automation.counter.value, 0)

    def test_runner_unavailable_backend_emits_platform_message(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        feedback_messages = []
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=ClickRunner(
                automation,
                FailingMouse("macOS mouse API is not available"),
            ),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
        )

        with self.assertLogs(
            "turkuaz_clickflow.app.click_loop_controller",
            level="ERROR",
        ):
            controller.tick()

        self.assertEqual(
            feedback_messages,
            ["Bu platformda otomasyon backend'i kullanılamıyor."],
        )
        self.assertEqual(automation.counter.value, 0)

    def test_unhandled_runner_exception_is_logged_and_stops_safely(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        feedback_messages = []
        controller = ClickLoopController(
            automation_service=automation,
            click_runner=BrokenRunner(),
            scheduler=FakeScheduler(),
            feedback_service=FeedbackService(),
            on_feedback=lambda message: feedback_messages.append(message.text),
        )

        with self.assertLogs(
            "turkuaz_clickflow.app.click_loop_controller",
            level="ERROR",
        ) as logs:
            result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.successful_clicks, 0)
        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(automation.counter.value, 0)
        self.assertEqual(
            feedback_messages,
            ["İşlem başlatılamadı: runner exploded"],
        )
        self.assertIn("Unhandled click runner exception: runner exploded", logs.output[0])


if __name__ == "__main__":
    unittest.main()
