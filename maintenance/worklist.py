"""The facilities team's work list: what to fix next."""
from datetime import datetime

PRIORITY_RANK = {"urgent": 0, "normal": 1, "low": 2}


def work_queue(requests, now: datetime):
    """Active requests in the order the team should work on them.

    Urgent first, then normal, then low. Within a priority, oldest first.
    """
    active = [r for r in requests if r.status in ("open", "in_progress")]
    active.sort(key=lambda r: (PRIORITY_RANK[r.priority], r.opened_at))
    return [
        {
            "id": r.id,
            "title": r.title,
            "location": r.location,
            "priority": r.priority,
            "age_hours": int((now - r.opened_at).total_seconds() // 3600),
        }
        for r in active
    ]
