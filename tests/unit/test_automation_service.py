import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.timer_service import TimerService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


class AutomationServiceTest(unittest.TestCase):
    def test_initial_state_is_ready(self) -> None:
        service = AutomationService()

        self.assertEqual(service.state, AutomationState.READY)
        self.assertIsNone(service.stop_reason)

    def test_start_with_valid_settings_transitions_to_running(self) -> None:
        service = AutomationService()

        result = service.start(cps=10)

        self.assertTrue(result.accepted)
        self.assertTrue(result.started)
        self.assertEqual(result.state, AutomationState.RUNNING)
        self.assertEqual(service.state, AutomationState.RUNNING)
        self.assertEqual(service.settings.cps, 10)

    def test_start_resets_counter_for_new_run(self) -> None:
        service = AutomationService()
        service.counter.increment(3)

        service.start(cps=10)

        self.assertEqual(service.counter.value, 0)

    def test_record_successful_click_increments_counter(self) -> None:
        service = AutomationService()
        service.start(cps=10)

        self.assertEqual(service.record_successful_click(), 1)
        self.assertEqual(service.record_successful_click(2), 3)
        self.assertEqual(service.counter.value, 3)

    def test_record_successful_click_requires_running_state(self) -> None:
        service = AutomationService()

        with self.assertRaises(RuntimeError):
            service.record_successful_click()

    def test_start_resets_elapsed_time_for_new_run(self) -> None:
        clock = FakeClock()
        service = AutomationService(timer=TimerService(clock=clock))
        service.start(cps=10)
        clock.advance(5.0)
        service.stop()

        service.start(cps=10)

        self.assertEqual(service.elapsed_seconds, 0.0)

    def test_elapsed_time_updates_while_running_and_freezes_after_stop(self) -> None:
        clock = FakeClock()
        service = AutomationService(timer=TimerService(clock=clock))
        service.start(cps=10)
        clock.advance(2.0)

        self.assertEqual(service.elapsed_seconds, 2.0)

        service.stop()
        clock.advance(10.0)

        self.assertEqual(service.elapsed_seconds, 2.0)

    def test_repeated_start_does_not_create_second_run(self) -> None:
        service = AutomationService()
        first = service.start(cps=10)
        second = service.start(cps=20)

        self.assertTrue(first.started)
        self.assertTrue(second.accepted)
        self.assertFalse(second.started)
        self.assertEqual(service.state, AutomationState.RUNNING)
        self.assertEqual(service.run_count, 1)
        self.assertEqual(service.settings.cps, 10)

    def test_stop_while_running_stops_automation(self) -> None:
        service = AutomationService()
        service.start(cps=10)

        result = service.stop()

        self.assertTrue(result.accepted)
        self.assertTrue(result.stopped)
        self.assertEqual(result.state, AutomationState.STOPPED)
        self.assertEqual(service.state, AutomationState.STOPPED)

    def test_stop_command_is_safely_accepted_when_not_running(self) -> None:
        service = AutomationService()

        result = service.stop()

        self.assertTrue(result.accepted)
        self.assertFalse(result.stopped)
        self.assertEqual(service.state, AutomationState.STOPPED)

    def test_invalid_cps_start_fails_with_error_state(self) -> None:
        service = AutomationService()

        result = service.start(cps=101)

        self.assertFalse(result.accepted)
        self.assertFalse(result.started)
        self.assertEqual(result.state, AutomationState.ERROR)
        self.assertEqual(service.state, AutomationState.ERROR)
        self.assertEqual(result.stop_reason, StopReason.INVALID_SETTINGS)
        self.assertEqual(service.stop_reason, StopReason.INVALID_SETTINGS)

    def test_stop_reason_is_user_stopped_by_default(self) -> None:
        service = AutomationService()
        service.start(cps=10)

        result = service.stop()

        self.assertEqual(result.stop_reason, StopReason.USER_STOPPED)
        self.assertEqual(service.stop_reason, StopReason.USER_STOPPED)

    def test_stop_reason_can_be_hotkey_stopped(self) -> None:
        service = AutomationService()
        service.start(cps=10)

        result = service.stop(reason=StopReason.HOTKEY_STOPPED)

        self.assertEqual(result.stop_reason, StopReason.HOTKEY_STOPPED)
        self.assertEqual(service.stop_reason, StopReason.HOTKEY_STOPPED)


if __name__ == "__main__":
    unittest.main()
