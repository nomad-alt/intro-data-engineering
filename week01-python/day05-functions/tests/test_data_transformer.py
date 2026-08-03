import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIRECTORY = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIRECTORY))

from data_transformer import (
    average_salary,
    highest_salary,
    increase_salary,
)


def test_increase_salary() -> None:
    """Test salary increase calculation."""
    assert increase_salary(1000, 10) == 1100


def test_average_salary() -> None:
    """Test average salary calculation."""
    employees = [
        {"salary": 100},
        {"salary": 200},
    ]
    assert average_salary(employees) == 150


def test_highest_salary() -> None:
    """Test highest salary lookup."""
    employees = [
        {"salary": 100},
        {"salary": 300},
    ]
    assert highest_salary(employees) == 300
