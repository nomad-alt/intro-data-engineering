import csv
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.load import save_csv, save_json


def test_save_csv_and_save_json_write_expected_files(tmp_path: Path) -> None:
    employees = [
        {
            "employee_id": "1",
            "name": "Alice",
            "department": "Engineering",
            "salary": 35000.0,
            "new_salary": 38500.0,
            "salary_band": "Mid",
        }
    ]

    csv_path = save_csv(employees, tmp_path / "employees_processed.csv")
    json_path = save_json(employees, tmp_path / "summary.json")

    assert csv_path.exists()
    assert json_path.exists()

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert rows[0]["employee_id"] == "1"
    assert rows[0]["new_salary"] == "38500.0"
    assert rows[0]["salary_band"] == "Mid"

    with json_path.open("r", encoding="utf-8") as file:
        content = json.load(file)

    assert content[0]["name"] == "Alice"
