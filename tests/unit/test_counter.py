import unittest

from turkuaz_clickflow.domain.counter import ClickCounter


class ClickCounterTest(unittest.TestCase):
    def test_counter_starts_at_zero(self) -> None:
        self.assertEqual(ClickCounter().value, 0)

    def test_counter_increments_successful_clicks(self) -> None:
        counter = ClickCounter()

        self.assertEqual(counter.increment(), 1)
        self.assertEqual(counter.increment(), 2)

    def test_counter_can_increment_by_amount(self) -> None:
        counter = ClickCounter()

        self.assertEqual(counter.increment(5), 5)

    def test_counter_resets_for_new_run(self) -> None:
        counter = ClickCounter()
        counter.increment(3)

        counter.reset_for_new_run()

        self.assertEqual(counter.value, 0)

    def test_counter_rejects_negative_initial_value(self) -> None:
        with self.assertRaises(ValueError):
            ClickCounter(value=-1)

    def test_counter_rejects_non_positive_increment(self) -> None:
        counter = ClickCounter()

        with self.assertRaises(ValueError):
            counter.increment(0)


if __name__ == "__main__":
    unittest.main()
