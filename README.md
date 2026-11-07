# Daily Expense Tracker

A lightweight command-line app for logging daily spending and reviewing it by day, month and category. Pure Python 3 (standard library only), data stored in a local JSON file.

## Features

- Add expenses with amount, category, note and optional date
- List by day, month or category, with totals
- Category summary with percentages and daily average
- Delete entries by ID
- Export everything to CSV
- Money handled with `Decimal`, so no floating-point rounding errors

## Usage

```bash
python expense_tracker.py add 250 --category food --note "Lunch"
python expense_tracker.py add 1200 -c travel -n "Train ticket" -d 2026-11-05
python expense_tracker.py list --date 2026-11-07
python expense_tracker.py list --month 2026-11 --category food
python expense_tracker.py summary                # current month
python expense_tracker.py summary --month 2026-10
python expense_tracker.py delete 3
python expense_tracker.py export expenses.csv
```

Options: `--file PATH` selects a different data file. Environment variables `EXPENSE_FILE` and `EXPENSE_CURRENCY` set the default file and currency label.

## Tests

```bash
pip install pytest
pytest
```

## Project layout

```
expense_tracker.py        # app + CLI
test_expense_tracker.py   # tests
README.md
.gitignore
```

## License

MIT
