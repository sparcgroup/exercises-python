import unittest
from datetime import date

from maintenance.config import HOLIDAYS
from maintenance.workdays import business_days_between


class BusinessDaysTest(unittest.TestCase):
    def test_same_day_is_zero(self):
        self.assertEqual(business_days_between(date(2026, 3, 4), date(2026, 3, 4)), 0)

    def test_weekend_is_skipped(self):
        # Friday to Monday
        self.assertEqual(business_days_between(date(2026, 3, 6), date(2026, 3, 9)), 1)

    def test_full_week(self):
        self.assertEqual(business_days_between(date(2026, 3, 2), date(2026, 3, 9)), 5)

    def test_holidays_are_skipped(self):
        # Wednesday 1 April to Monday 6 April, with 2 and 3 April as holidays
        self.assertEqual(business_days_between(date(2026, 4, 1), date(2026, 4, 6), HOLIDAYS), 1)


if __name__ == "__main__":
    unittest.main()
