from pathlib import Path

from src.extract import extract_csv


def test_extract_csv(tmp_path: Path) -> None:
    csv_file = tmp_path / "employees.csv"

    csv_file.write_text(
        ("employee_id,name\n1,Alice\n"),
        encoding="utf-8",
    )

    records = extract_csv(csv_file)

    assert len(records) == 1
    assert records[0]["name"] == "Alice"


import json

from src.extract import extract_json


def test_extract_json(tmp_path: Path) -> None:
    json_file = tmp_path / "departments.json"

    json_file.write_text(
        json.dumps(
            [
                {
                    "department_id": 1,
                    "department_name": "Engineering",
                }
            ]
        ),
        encoding="utf-8",
    )

    records = extract_json(json_file)

    assert len(records) == 1
    assert records[0]["department_name"] == "Engineering"
