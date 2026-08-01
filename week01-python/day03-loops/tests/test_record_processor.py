"""Tests for the transaction record processor."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIRECTORY = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIRECTORY))

from record_processor import summarize_transactions


def test_summarize_transactions() -> None:
    """A transaction summary should contain correct statistics."""
    transactions = [
        {"transaction_id": 1, "amount": 100.0, "status": "valid"},
        {"transaction_id": 2, "amount": 50.0, "status": "valid"},
        {"transaction_id": 3, "amount": None, "status": "invalid"},
    ]

    summary = summarize_transactions(transactions)

    assert summary["total_count"] == 3
    assert summary["valid_count"] == 2
    assert summary["invalid_count"] == 1
    assert summary["total_valid_amount"] == 150.0
    assert summary["average_valid_amount"] == 75.0
    assert summary["invalid_transaction_ids"] == [3]


def test_summarize_empty_transactions() -> None:
    """An empty transaction list should produce zero values."""
    summary = summarize_transactions([])

    assert summary["total_count"] == 0
    assert summary["valid_count"] == 0
    assert summary["invalid_count"] == 0
    assert summary["total_valid_amount"] == 0.0
    assert summary["average_valid_amount"] == 0.0
    assert summary["invalid_transaction_ids"] == []
