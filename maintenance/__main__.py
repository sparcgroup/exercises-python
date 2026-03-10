"""Command line entry point.

    python -m maintenance list [--now 2026-03-09T10:00]
    python -m maintenance report 2026-03-02 2026-03-06
"""
import argparse
from datetime import date, datetime

from .report import weekly_report
from .store import load_requests
from .worklist import work_queue


def print_list(now):
    rows = work_queue(load_requests(), now)
    for row in rows:
        print(f"{row['id']:<7}{row['priority']:<8}{row['age_hours']:>5}h  {row['location']:<10}{row['title']}")


def print_report(start, end):
    report = weekly_report(load_requests(), start, end)
    print(f"Week {start} to {end}")
    print(f"  Opened:                 {report['opened']}")
    print(f"  Still active:           {report['still_active']}")
    print(f"  Resolved within target: {report['resolved_within_target']}")
    print("  By location:")
    for location, count in report["by_location"]:
        print(f"    {location:<10}{count}")


def main():
    parser = argparse.ArgumentParser(prog="maintenance")
    sub = parser.add_subparsers(dest="command", required=True)
    list_cmd = sub.add_parser("list", help="show the work list")
    list_cmd.add_argument("--now", type=datetime.fromisoformat, default=None)
    report_cmd = sub.add_parser("report", help="weekly summary")
    report_cmd.add_argument("start", type=date.fromisoformat)
    report_cmd.add_argument("end", type=date.fromisoformat)
    args = parser.parse_args()

    if args.command == "list":
        print_list(args.now or datetime.now())
    else:
        print_report(args.start, args.end)


if __name__ == "__main__":
    main()
