import json
from datetime import datetime
from pathlib import Path

from .models import Request

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "requests.json"


def _parse(value):
    return datetime.fromisoformat(value) if value else None


def load_requests(path=DATA_FILE):
    with open(path, encoding="utf-8") as f:
        rows = json.load(f)
    return [
        Request(
            id=row["id"],
            title=row["title"],
            location=row["location"],
            priority=row["priority"],
            status=row["status"],
            opened_at=_parse(row["opened_at"]),
            closed_at=_parse(row["closed_at"]),
        )
        for row in rows
    ]
