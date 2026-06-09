import unittest

from turkuaz_clickflow.domain.automation_settings import AutomationSettings
from turkuaz_clickflow.domain.cps_policy import CpsPolicy, InvalidCpsError


class CpsPolicyTest(unittest.TestCase):
    def test_default_cps_is_10(self) -> None:
        self.assertEqual(CpsPolicy().default_value(), 10)
        self.assertEqual(AutomationSettings.defaults().cps, 10)

    def test_valid_cps_values_are_accepted(self) -> None:
        for value in (1, 10, 100):
            with self.subTest(value=value):
                self.assertEqual(CpsPolicy().validate(value), value)

    def test_invalid_cps_values_raise(self) -> None:
        for value in (0, -1, 101):
            with self.subTest(value=value):
                with self.assertRaises(InvalidCpsError):
                    CpsPolicy().validate(value)

    def test_non_integer_cps_raises(self) -> None:
        with self.assertRaises(InvalidCpsError):
            CpsPolicy().validate(10.5)  # type: ignore[arg-type]

    def test_settings_validate_cps(self) -> None:
        with self.assertRaises(InvalidCpsError):
            AutomationSettings(cps=101)


if __name__ == "__main__":
    unittest.main()
