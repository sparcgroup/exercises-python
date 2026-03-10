"""Weekly summary of maintenance requests for the facilities team."""
from collections import Counter
from datetime import date, datetime, time

from .config import HOLIDAYS, TARGET_BUSINESS_DAYS
from .workdays import business_days_between

ACTIVE_STATUSES = ("open", "in_progress")


def opened_between(requests, start: date, end: date):
    start_at = datetime.combine(start, time.min)
    end_at = datetime.combine(end, time.min)
    return [r for r in requests if start_at <= r.opened_at < end_at]


def summary_by_location(requests):
    """Count requests per location, busiest first, ties in alphabetical order."""
    counts = Counter(r.location for r in requests)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def resolved_within_target(requests):
    """Closed requests that were resolved within the service target."""
    return [
        r for r in requests
        if r.status == "closed"
        and business_days_between(r.opened_at.date(), r.closed_at.date(), HOLIDAYS)
        <= TARGET_BUSINESS_DAYS
    ]


def weekly_report(requests, start: date, end: date):
    week = opened_between(requests, start, end)
    return {
        "opened": len(week),
        "still_active": len([r for r in week if r.status in ACTIVE_STATUSES]),
        "resolved_within_target": len(resolved_within_target(week)),
        "by_location": summary_by_location(week),
    }
