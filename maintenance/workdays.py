from datetime import date, timedelta


def business_days_between(start: date, end: date, holidays=frozenset()) -> int:
    """Count business days after start, up to and including end.

    Weekends and holidays are not counted. Returns 0 if end is not after start.
    """
    days = 0
    current = start + timedelta(days=1)
    while current <= end:
        if current.weekday() < 5 and current not in holidays:
            days += 1
        current += timedelta(days=1)
    return days
