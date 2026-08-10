"""Functions for extracting data."""

from __future__ import annotations

import csv
from pathlib import Path


def extract_csv(path: Path) -> list[dict[str, str]]:
    """Read records from a CSV file into a list of dictionaries."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def extract_employees(path: Path) -> list[dict[str, str]]:
    """Read employee records from a CSV file."""
    return extract_csv(path)


def extract_departments(path: Path) -> list[dict[str, str]]:
    """Read department records from CSV file."""
    return extract_csv(path)


def extract_customers(path: Path) -> list[dict[str, str]]:
    """Read customer records from CSV file."""
    return extract_csv(path)


def count_records(path: Path) -> int:
    """Count the number of records in a CSV file."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return sum(1 for _ in reader)


def file_exists(path: Path) -> bool:
    """Check if a file exists at the given path."""
    return path.exists()
