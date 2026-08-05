import csv
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIRECTORY = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIRECTORY))

from etl_pipeline import extract, increase_salary, transform


def test_increase_salary() -> None:
    assert increase_salary(1000, 10) == pytest.approx(1100)
    assert increase_salary(42000, 10) == pytest.approx(46200)


def test_transform() -> None:
    employees = [
        {"employee_id": "1", "name": "Alice", "salary": "35000"},
        {"employee_id": "2", "name": "Bob", "salary": "42000"},
    ]

    transformed = transform(employees)

    assert len(transformed) == 2
    assert transformed[0]["employee_id"] == "1"
    assert transformed[0]["name"] == "Alice"
    assert transformed[0]["salary"] == 35000.0
    assert transformed[0]["new_salary"] == pytest.approx(38500)

    assert transformed[1]["employee_id"] == "2"
    assert transformed[1]["name"] == "Bob"
    assert transformed[1]["salary"] == 42000.0
    assert transformed[1]["new_salary"] == pytest.approx(46200)


def test_extract(tmp_path: Path) -> None:
    input_file = tmp_path / "employees.csv"
    rows = [
        ["employee_id", "name", "salary"],
        ["1", "Alice", "35000"],
        ["2", "Bob", "42000"],
    ]

    with input_file.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

    extracted = extract(input_file)

    assert extracted == [
        {"employee_id": "1", "name": "Alice", "salary": "35000"},
        {"employee_id": "2", "name": "Bob", "salary": "42000"},
    ]
