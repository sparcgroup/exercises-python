"""Run a query against the tenants and leases tables.

    python sql/run.py sql/query.sql
"""
import sqlite3
import sys
from pathlib import Path

SCHEMA = Path(__file__).resolve().parent / "schema.sql"

query = Path(sys.argv[1] if len(sys.argv) > 1 else SCHEMA.parent / "query.sql").read_text(encoding="utf-8")
db = sqlite3.connect(":memory:")
db.executescript(SCHEMA.read_text(encoding="utf-8"))
cursor = db.execute(query)
columns = [c[0] for c in cursor.description or []]
rows = cursor.fetchall()
print(" | ".join(columns))
for row in rows:
    print(" | ".join(str(v) for v in row))
print(f"({len(rows)} rows)")
