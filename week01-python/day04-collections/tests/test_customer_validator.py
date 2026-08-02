"""Tests for customer-record validation."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIRECTORY = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIRECTORY))

from customer_validator import validate_customers


def test_validate_valid_customers() -> None:
    """Valid customer records should pass validation."""
    customers = [
        {
            "customer_id": 1,
            "name": "Amina",
            "email": "amina@example.com",
            "country": "Sweden",
        },
        {
            "customer_id": 2,
            "name": "Yusuf",
            "email": "yusuf@example.com",
            "country": "Norway",
        },
    ]

    summary = validate_customers(customers)

    assert summary["total_count"] == 2
    assert summary["valid_count"] == 2
    assert summary["invalid_count"] == 0
    assert summary["unique_country_count"] == 2
    assert summary["invalid_customer_ids"] == []


def test_validate_customer_with_missing_email() -> None:
    """A customer with no email should be invalid."""
    customers = [
        {
            "customer_id": 1,
            "name": "Amina",
            "email": None,
            "country": "Sweden",
        }
    ]

    summary = validate_customers(customers)

    assert summary["valid_count"] == 0
    assert summary["invalid_count"] == 1
    assert summary["invalid_customer_ids"] == [1]


def test_validate_duplicate_customer_ids() -> None:
    """A repeated customer ID should be invalid."""
    customers = [
        {
            "customer_id": 1,
            "name": "Amina",
            "email": "amina@example.com",
            "country": "Sweden",
        },
        {
            "customer_id": 1,
            "name": "Sara",
            "email": "sara@example.com",
            "country": "Norway",
        },
    ]

    summary = validate_customers(customers)

    assert summary["valid_count"] == 1
    assert summary["invalid_count"] == 1
    assert summary["invalid_customer_ids"] == [1]


def test_validate_empty_customer_list() -> None:
    """An empty collection should return zero counts."""
    summary = validate_customers([])

    assert summary["total_count"] == 0
    assert summary["valid_count"] == 0
    assert summary["invalid_count"] == 0
    assert summary["unique_country_count"] == 0
    assert summary["invalid_customer_ids"] == []
