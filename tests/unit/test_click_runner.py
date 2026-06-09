import unittest
from typing import Optional

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_runner import ClickRunner
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import PlatformOperationError


class FakeMouse:
    def __init__(self) -> None:
        self.clicks = 0

    def left_click(self) -> None:
        self.clicks += 1


class FailingMouse:
    def left_click(self) -> None:
        raise PlatformOperationError("click failed")


class RecordingSleeper:
    def __init__(self, automation: Optional[AutomationService] = None) -> None:
        self.calls: list[float] = []
        self._automation = automation

    def __call__(self, seconds: float) -> None:
        self.calls.append(seconds)


class StoppingSleeper:
    def __init__(self, automation: AutomationService) -> None:
        self.calls: list[float] = []
        self._automation = automation

    def __call__(self, seconds: float) -> None:
        self.calls.append(seconds)
        self._automation.stop()


class ClickRunnerTest(unittest.TestCase):
    def test_does_not_click_when_automation_is_not_running(self) -> None:
        automation = AutomationService()
        mouse = FakeMouse()
        runner = ClickRunner(automation, mouse)

        result = runner.run_steps(max_clicks=3)

        self.assertEqual(result.attempted_clicks, 0)
        self.assertEqual(result.successful_clicks, 0)
        self.assertEqual(mouse.clicks, 0)
        self.assertEqual(automation.counter.value, 0)

    def test_clicks_and_increments_counter_when_running(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        mouse = FakeMouse()
        runner = ClickRunner(automation, mouse, sleeper=lambda seconds: None)

        result = runner.run_steps(max_clicks=3)

        self.assertEqual(result.attempted_clicks, 3)
        self.assertEqual(result.successful_clicks, 3)
        self.assertEqual(mouse.clicks, 3)
        self.assertEqual(automation.counter.value, 3)
        self.assertEqual(automation.state, AutomationState.RUNNING)

    def test_uses_cps_interval_between_clicks(self) -> None:
        automation = AutomationService()
        automation.start(cps=20)
        sleeper = RecordingSleeper()
        runner = ClickRunner(automation, FakeMouse(), sleeper=sleeper)

        runner.run_steps(max_clicks=3)

        self.assertEqual(sleeper.calls, [0.05, 0.05])

    def test_stop_during_wait_prevents_next_click(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        mouse = FakeMouse()
        sleeper = StoppingSleeper(automation)
        runner = ClickRunner(automation, mouse, sleeper=sleeper)

        result = runner.run_steps(max_clicks=3)

        self.assertEqual(result.attempted_clicks, 1)
        self.assertEqual(result.successful_clicks, 1)
        self.assertEqual(mouse.clicks, 1)
        self.assertEqual(automation.counter.value, 1)
        self.assertEqual(automation.state, AutomationState.STOPPED)

    def test_adapter_error_stops_automation_safely(self) -> None:
        automation = AutomationService()
        automation.start(cps=10)
        runner = ClickRunner(automation, FailingMouse())

        result = runner.run_once()

        self.assertEqual(result.attempted_clicks, 1)
        self.assertEqual(result.successful_clicks, 0)
        self.assertTrue(result.stopped)
        self.assertEqual(result.stop_reason, StopReason.ERROR)
        self.assertEqual(automation.stop_reason, StopReason.ERROR)
        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(automation.counter.value, 0)

    def test_negative_max_clicks_is_rejected(self) -> None:
        automation = AutomationService()
        runner = ClickRunner(automation, FakeMouse())

        with self.assertRaises(ValueError):
            runner.run_steps(max_clicks=-1)


if __name__ == "__main__":
    unittest.main()
