import unittest
from datetime import datetime

from maintenance.store import load_requests
from maintenance.worklist import work_queue

NOW = datetime(2026, 3, 9, 10, 0)


class WorkQueueTest(unittest.TestCase):
    def setUp(self):
        self.rows = work_queue(load_requests(), NOW)

    def test_only_active_requests(self):
        self.assertEqual(len(self.rows), 5)

    def test_urgent_first_then_oldest(self):
        self.assertEqual([r["id"] for r in self.rows], ["R-104", "R-101", "R-105", "R-107", "R-109"])

    def test_row_contents(self):
        self.assertEqual(
            self.rows[0],
            {
                "id": "R-104",
                "title": "Card reader offline at main door",
                "location": "Lobby",
                "priority": "urgent",
                "age_hours": 66,
            },
        )


if __name__ == "__main__":
    unittest.main()
