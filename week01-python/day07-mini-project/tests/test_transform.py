import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.transform import transform


def test_transform_adds_salary_projection_and_band() -> None:
    employees = [
        {
            "employee_id": "1",
            "name": "Alice",
            "department": "Engineering",
            "salary": "35000",
        }
    ]

    result = transform(employees)

    assert result == [
        {
            "employee_id": "1",
            "name": "Alice",
            "department": "Engineering",
            "salary": 35000.0,
            "new_salary": 38500.0,
            "salary_band": "Mid",
        }
    ]
