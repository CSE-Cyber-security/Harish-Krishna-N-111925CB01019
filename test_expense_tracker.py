import csv
from datetime import date
from decimal import Decimal

import pytest

import expense_tracker as et


def test_add_and_ids_not_reused():
    items = []
    a = et.add_expense(items, "100", "Food", "lunch", date(2026, 11, 7))
    b = et.add_expense(items, "50.5", "travel", "", date(2026, 11, 7))
    assert (a["id"], b["id"]) == (1, 2)
    assert a["category"] == "food" and b["amount"] == "50.50"
    et.delete_expense(items, 1)
    c = et.add_expense(items, "10")
    assert c["id"] == 3


@pytest.mark.parametrize("bad", ["0", "-5", "abc", "nan", "inf"])
def test_invalid_amounts(bad):
    with pytest.raises(ValueError):
        et.parse_amount(bad)


def test_filter_total_summary():
    items = []
    et.add_expense(items, "100", "food", when=date(2026, 11, 7))
    et.add_expense(items, "40", "food", when=date(2026, 11, 8))
    et.add_expense(items, "300", "rent", when=date(2026, 10, 1))
    nov = et.filter_expenses(items, month="2026-11")
    assert len(nov) == 2 and et.total(nov) == Decimal("140.00")
    assert et.summarize_by_category(items)[0] == ("rent", Decimal("300.00"))
    assert len(et.filter_expenses(items, on_date=date(2026, 11, 7))) == 1


def test_delete_missing():
    assert et.delete_expense([], 1) is False


def test_cli_roundtrip_and_export(tmp_path, capsys):
    data = str(tmp_path / "e.json")
    assert et.main(["--file", data, "add", "75", "-c", "snacks", "-d", "2026-11-07"]) == 0
    assert et.main(["--file", data, "add", "bad"]) == 1
    assert et.main(["--file", data, "list", "--date", "2026-11-07"]) == 0
    assert "snacks" in capsys.readouterr().out
    out = tmp_path / "out.csv"
    assert et.main(["--file", data, "export", str(out)]) == 0
    rows = list(csv.DictReader(open(out, encoding="utf-8")))
    assert rows[0]["amount"] == "75.00"
    assert et.main(["--file", data, "delete", "1"]) == 0
    assert et.main(["--file", data, "delete", "1"]) == 1
