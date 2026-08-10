"""Functions for extracting data."""

from __future__ import annotations

import csv
import json
from pathlib import Path


def extract_csv(path: Path) -> list[dict[str, str]]:
    """
    Read records from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        List of dictionaries.
    """
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:
            reader = csv.DictReader(file)
            return list(reader)
    except OSError as error:
        raise RuntimeError(f"Unable to read CSV file: {path}") from error


def extract_json(path: Path) -> list[dict]:
    """
    Read records from a JSON file.

    Args:
        path: Path to JSON file.

    Returns:
        Parsed JSON data.
    """
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Unable to read JSON file: {path}") from error


try:
    from .config import (
        DEPARTMENT_JSON,
        EMPLOYEE_CSV,
    )
except ImportError:  # pragma: no cover - fallback for direct script execution
    from config import (
        DEPARTMENT_JSON,
        EMPLOYEE_CSV,
    )


def extract_employees() -> list[dict[str, str]]:
    """Extract employee data."""
    return extract_csv(EMPLOYEE_CSV)


def extract_departments() -> list[dict]:
    """Extract department data."""
    return extract_json(DEPARTMENT_JSON)


def extract_customers(path: Path) -> list[dict[str, str]]:
    """Read customer records from CSV file."""
    return extract_csv(path)


def count_records(records: list[dict]) -> int:
    """Return the number of extracted records."""
    return len(records)


def extract_text(path: Path) -> str:
    """Read a text file."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return file.read()
    except OSError as error:
        raise RuntimeError(f"Unable to read text file: {path}") from error


def supported_extension(path: Path) -> bool:
    """Return True only for supported file extensions."""
    return path.suffix.lower() in {".csv", ".json"}


def extract_file(path: Path) -> list[dict]:
    """Dispatch extraction based on the file extension."""
    if not supported_extension(path):
        raise ValueError(f"Unsupported file type: {path.suffix}")

    if path.suffix.lower() == ".csv":
        return extract_csv(path)

    return extract_json(path)


def file_exists(path: Path) -> bool:
    """Check if a file exists at the given path."""
    return path.exists()
