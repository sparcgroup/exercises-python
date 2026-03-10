import unittest
from datetime import date

from maintenance.report import resolved_within_target, summary_by_location, weekly_report
from maintenance.store import load_requests


class WeeklyReportTest(unittest.TestCase):
    def setUp(self):
        self.requests = load_requests()

    def test_full_week(self):
        report = weekly_report(self.requests, date(2026, 3, 2), date(2026, 3, 8))
        self.assertEqual(report["opened"], 7)
        self.assertEqual(report["still_active"], 4)
        self.assertEqual(report["resolved_within_target"], 2)

    def test_location_summary_is_busiest_first(self):
        report = weekly_report(self.requests, date(2026, 3, 2), date(2026, 3, 8))
        self.assertEqual(report["by_location"][0], ("Room 204", 3))

    def test_empty_week(self):
        report = weekly_report(self.requests, date(2026, 3, 14), date(2026, 3, 15))
        self.assertEqual(report["opened"], 0)
        self.assertEqual(report["by_location"], [])


class ResolvedWithinTargetTest(unittest.TestCase):
    def test_counts_business_days_only(self):
        resolved = resolved_within_target(load_requests())
        self.assertEqual(sorted(r.id for r in resolved), ["R-102", "R-106", "R-108"])


class SummaryByLocationTest(unittest.TestCase):
    def test_single_location(self):
        requests = [r for r in load_requests() if r.location == "Pantry"]
        self.assertEqual(summary_by_location(requests), [("Pantry", 2)])


if __name__ == "__main__":
    unittest.main()
