import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.report import generate_summary


def test_generate_summary_returns_expected_aggregates() -> None:
    employees = [
        {
            "employee_id": "1",
            "name": "Alice",
            "department": "Engineering",
            "salary": 35000.0,
            "new_salary": 38500.0,
            "salary_band": "Mid",
        },
        {
            "employee_id": "2",
            "name": "Bob",
            "department": "Engineering",
            "salary": 45000.0,
            "new_salary": 49500.0,
            "salary_band": "Senior",
        },
        {
            "employee_id": "3",
            "name": "Cara",
            "department": "Sales",
            "salary": 28000.0,
            "new_salary": 30800.0,
            "salary_band": "Junior",
        },
        {
            "employee_id": "4",
            "name": "Drew",
            "department": "Sales",
            "salary": 40000.0,
            "new_salary": 44000.0,
            "salary_band": "Senior",
        },
        {
            "employee_id": "5",
            "name": "Eli",
            "department": "Marketing",
            "salary": 32000.0,
            "new_salary": 35200.0,
            "salary_band": "Junior",
        },
    ]

    summary = generate_summary(employees)

    assert summary["employee_count"] == 5
    assert summary["average_salary"] == 36000.0
    assert summary["average_new_salary"] == 39600.0
    assert summary["highest_salary"] == 45000.0
    assert summary["lowest_salary"] == 28000.0
    assert summary["departments"] == {
        "Engineering": 2,
        "Sales": 2,
        "Marketing": 1,
    }
