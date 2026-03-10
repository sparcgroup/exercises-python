# Maintenance requests

A small tool used by the facilities team at Riverside Learning Centre to track maintenance requests.
It produces a weekly summary report and a work list of what to fix next.

Requires Python 3.10 or later. There is nothing to install.

## Layout

```
maintenance/        application code
  __main__.py       command line entry point
  report.py         weekly summary report
  worklist.py       work list for the facilities team
  workdays.py       business day calculations
  config.py         service target and holidays
  store.py          loads data/requests.json
  models.py         the Request type
data/requests.json  sample requests
tests/              unit tests
sql/                SQL exercise
```

## Run

```
python -m unittest                                  # run the tests
python -m maintenance report 2026-03-02 2026-03-06  # weekly report
python -m maintenance list --now 2026-03-09T10:00   # work list as of a given time
python sql/run.py sql/query.sql                     # run your SQL query
```

On some systems the command is `python3` rather than `python`.
