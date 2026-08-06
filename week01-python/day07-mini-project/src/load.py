import csv
import json
from pathlib import Path


def save_csv(
    employees: list[dict[str, object]], output_path: Path | None = None
) -> Path:
    """Write transformed employees to a CSV file."""
    if output_path is None:
        output_path = (
            Path(__file__).resolve().parent.parent / "data" / "employees_processed.csv"
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "employee_id",
        "name",
        "department",
        "salary",
        "new_salary",
        "salary_band",
    ]

    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow({field: employee.get(field, "") for field in fieldnames})

    return output_path


def save_json(
    employees: list[dict[str, object]], output_path: Path | None = None
) -> Path:
    """Write a summary JSON file with the transformed employees."""
    if output_path is None:
        output_path = Path(__file__).resolve().parent.parent / "data" / "summary.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(employees, file, indent=2)

    return output_path
