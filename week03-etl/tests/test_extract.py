from pathlib import Path

from src.extract import extract_employees


def test_extract_employees(tmp_path: Path) -> None:
    csv_file = tmp_path / "employees.csv"

    csv_file.write_text(
        (
            "employee_id,name,department,salary,hire_date\n"
            "1,Alice,Engineering,35000,2022-01-10\n"
        ),
        encoding="utf-8",
    )

    employees = extract_employees(csv_file)

    assert len(employees) == 1
    assert employees[0]["name"] == "Alice"
