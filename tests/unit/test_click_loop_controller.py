import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_loop_controller import ClickLoopController
from turkuaz_clickflow.app.click_runner import ClickRunner
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import PlatformOperationError


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
    def left_click(self) -> None:
        raise PlatformOperationError("click failed")


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

        result = controller.tick()

        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.ERROR)
        self.assertTrue(scheduler.stopped)
        self.assertFalse(controller.is_running)
        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(
            feedback_messages,
            ["Hata nedeniyle durdu. Lütfen tekrar deneyin."],
        )


if __name__ == "__main__":
    unittest.main()
