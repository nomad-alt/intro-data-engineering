import csv
from pathlib import Path


def extract(path: Path) -> list[dict[str, str]]:
    """Read employees from a CSV file."""
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
