import unittest

from turkuaz_clickflow.app.timer_service import TimerService


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


class TimerServiceTest(unittest.TestCase):
    def test_timer_starts_at_zero(self) -> None:
        timer = TimerService()

        self.assertEqual(timer.elapsed_seconds(), 0.0)
        self.assertFalse(timer.is_running)

    def test_start_new_run_resets_and_tracks_elapsed_time(self) -> None:
        clock = FakeClock()
        timer = TimerService(clock=clock)

        timer.start_new_run()
        clock.advance(2.5)

        self.assertTrue(timer.is_running)
        self.assertEqual(timer.elapsed_seconds(), 2.5)

    def test_stop_freezes_elapsed_time(self) -> None:
        clock = FakeClock()
        timer = TimerService(clock=clock)
        timer.start_new_run()
        clock.advance(3.0)

        timer.stop()
        clock.advance(10.0)

        self.assertFalse(timer.is_running)
        self.assertEqual(timer.elapsed_seconds(), 3.0)

    def test_new_run_resets_previous_elapsed_time(self) -> None:
        clock = FakeClock()
        timer = TimerService(clock=clock)
        timer.start_new_run()
        clock.advance(4.0)
        timer.stop()

        timer.start_new_run()

        self.assertTrue(timer.is_running)
        self.assertEqual(timer.elapsed_seconds(), 0.0)

    def test_reset_clears_elapsed_time(self) -> None:
        clock = FakeClock()
        timer = TimerService(clock=clock)
        timer.start_new_run()
        clock.advance(4.0)

        timer.reset()

        self.assertFalse(timer.is_running)
        self.assertEqual(timer.elapsed_seconds(), 0.0)


if __name__ == "__main__":
    unittest.main()

