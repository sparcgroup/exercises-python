from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Request:
    id: str
    title: str
    location: str
    priority: str  # "urgent", "normal" or "low"
    status: str  # "open", "in_progress" or "closed"
    opened_at: datetime
    closed_at: Optional[datetime] = None
