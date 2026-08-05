from pathlib import Path


def count_lines(path: Path) -> int:
    """Count the number of lines in a file."""
    with open(path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def read_employee_csv(path: Path) -> list[dict[str, str]]:
    """Read employee data from CSV file and return a list of dictionaries."""
    import csv

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def total_salary(
    employees: list[dict[str, str]],
) -> float:
    """Calculate the total salary of employees."""
    total = 0.0
    for employee in employees:
        salary = employee.get("salary")
        if salary is not None:
            total += float(salary)
    return total


def average_salary(
    employees: list[dict[str, str]],
) -> float:
    """Calculate the average salary of employees."""
    total = total_salary(employees)
    count = len(employees)
    return total / count if count > 0 else 0.0


def load_customer(path: Path) -> dict:
    """Load customer data from a JSON file."""
    import json

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_customer(
    customer: dict,
    path: Path,
) -> None:
    """Save customer data to a JSON file."""
    import json

    with open(path, "w", encoding="utf-8") as file:
        json.dump(customer, file, indent=4)
