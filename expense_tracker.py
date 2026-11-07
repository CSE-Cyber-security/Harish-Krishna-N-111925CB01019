#!/usr/bin/env python3
"""Daily Expense Tracker - a small command-line app to record and review spending.

Data is stored in a local JSON file (default: expenses.json).

Examples:
    python expense_tracker.py add 250 --category food --note "Lunch"
    python expense_tracker.py list --date 2026-11-07
    python expense_tracker.py summary --month 2026-11
    python expense_tracker.py delete 3
    python expense_tracker.py export expenses.csv
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

DEFAULT_FILE = os.environ.get("EXPENSE_FILE", "expenses.json")
CURRENCY = os.environ.get("EXPENSE_CURRENCY", "Rs.")


# ---------- storage ----------

def load_expenses(path=DEFAULT_FILE):
    """Return the list of expense dicts stored at `path` (empty if none)."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise SystemExit(f"Error: {path} is not valid JSON.")
    return data if isinstance(data, list) else []


def save_expenses(expenses, path=DEFAULT_FILE):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)
    os.replace(tmp, path)


# ---------- validation ----------

def parse_amount(text):
    try:
        amount = Decimal(str(text))
    except InvalidOperation:
        raise ValueError(f"Invalid amount: {text!r}")
    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    return amount.quantize(Decimal("0.01"))


def parse_date(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Invalid date {text!r}; use YYYY-MM-DD.")


def parse_month(text):
    try:
        return datetime.strptime(text, "%Y-%m").strftime("%Y-%m")
    except ValueError:
        raise ValueError(f"Invalid month {text!r}; use YYYY-MM.")


# ---------- core operations ----------

def add_expense(expenses, amount, category="general", note="", when=None):
    """Append a new expense and return it. IDs are never reused."""
    next_id = max((e["id"] for e in expenses), default=0) + 1
    expense = {
        "id": next_id,
        "date": (when or date.today()).isoformat(),
        "amount": str(parse_amount(amount)),
        "category": category.strip().lower() or "general",
        "note": note.strip(),
    }
    expenses.append(expense)
    return expense


def delete_expense(expenses, expense_id):
    """Remove an expense by id. Returns True if something was removed."""
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            del expenses[i]
            return True
    return False


def filter_expenses(expenses, on_date=None, month=None, category=None):
    result = expenses
    if on_date:
        result = [e for e in result if e["date"] == on_date.isoformat()]
    if month:
        result = [e for e in result if e["date"].startswith(month)]
    if category:
        result = [e for e in result if e["category"] == category.strip().lower()]
    return sorted(result, key=lambda e: (e["date"], e["id"]))


def total(expenses):
    return sum((Decimal(e["amount"]) for e in expenses), Decimal("0.00"))


def summarize_by_category(expenses):
    sums = defaultdict(lambda: Decimal("0.00"))
    for e in expenses:
        sums[e["category"]] += Decimal(e["amount"])
    return sorted(sums.items(), key=lambda kv: kv[1], reverse=True)


def export_csv(expenses, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "date", "amount", "category", "note"])
        writer.writeheader()
        writer.writerows(sorted(expenses, key=lambda e: (e["date"], e["id"])))


# ---------- display ----------

def money(value):
    return f"{CURRENCY} {value:,.2f}"


def print_table(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':>4}  {'Date':<10}  {'Amount':>12}  {'Category':<12}  Note")
    print("-" * 60)
    for e in expenses:
        print(f"{e['id']:>4}  {e['date']:<10}  {Decimal(e['amount']):>12,.2f}  "
              f"{e['category']:<12}  {e['note']}")
    print("-" * 60)
    print(f"{'Total':>18}  {total(expenses):>12,.2f}")


def print_summary(expenses, label):
    if not expenses:
        print(f"No expenses for {label}.")
        return
    grand = total(expenses)
    print(f"Summary for {label}")
    print("-" * 44)
    for category, amount in summarize_by_category(expenses):
        pct = (amount / grand * 100) if grand else Decimal(0)
        print(f"{category:<14} {money(amount):>16}  {pct:5.1f}%")
    print("-" * 44)
    print(f"{'Total':<14} {money(grand):>16}")
    days = {e["date"] for e in expenses}
    print(f"Days with spending: {len(days)}  |  Daily average: {money(grand / len(days))}")


# ---------- CLI ----------

def build_parser():
    p = argparse.ArgumentParser(description="Daily Expense Tracker")
    p.add_argument("--file", default=DEFAULT_FILE, help="data file (default: %(default)s)")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("add", help="add an expense")
    a.add_argument("amount")
    a.add_argument("--category", "-c", default="general")
    a.add_argument("--note", "-n", default="")
    a.add_argument("--date", "-d", help="YYYY-MM-DD (default: today)")

    l = sub.add_parser("list", help="list expenses")
    l.add_argument("--date", "-d", help="only this day (YYYY-MM-DD)")
    l.add_argument("--month", "-m", help="only this month (YYYY-MM)")
    l.add_argument("--category", "-c")

    s = sub.add_parser("summary", help="category breakdown")
    s.add_argument("--date", "-d", help="a single day (YYYY-MM-DD)")
    s.add_argument("--month", "-m", help="a month (YYYY-MM); default: current month")

    d = sub.add_parser("delete", help="delete an expense by id")
    d.add_argument("id", type=int)

    e = sub.add_parser("export", help="export all expenses to CSV")
    e.add_argument("output")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    expenses = load_expenses(args.file)

    try:
        if args.command == "add":
            when = parse_date(args.date) if args.date else None
            exp = add_expense(expenses, args.amount, args.category, args.note, when)
            save_expenses(expenses, args.file)
            print(f"Added #{exp['id']}: {money(Decimal(exp['amount']))} "
                  f"[{exp['category']}] on {exp['date']}")

        elif args.command == "list":
            on_date = parse_date(args.date) if args.date else None
            month = parse_month(args.month) if args.month else None
            print_table(filter_expenses(expenses, on_date, month, args.category))

        elif args.command == "summary":
            if args.date:
                on_date = parse_date(args.date)
                print_summary(filter_expenses(expenses, on_date=on_date), args.date)
            else:
                month = parse_month(args.month) if args.month else date.today().strftime("%Y-%m")
                print_summary(filter_expenses(expenses, month=month), month)

        elif args.command == "delete":
            if delete_expense(expenses, args.id):
                save_expenses(expenses, args.file)
                print(f"Deleted expense #{args.id}.")
            else:
                print(f"No expense with id {args.id}.", file=sys.stderr)
                return 1

        elif args.command == "export":
            export_csv(expenses, args.output)
            print(f"Exported {len(expenses)} expenses to {args.output}")
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
