import csv
from pathlib import Path


def increase_salary(salary: float, percentage: float) -> float:
    """Increase salary by a given percentage."""
    return salary * (1 + percentage / 100)


def extract(path: Path) -> list[dict[str, str]]:
    """Read employee records from a CSV file."""
    with path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def transform(
    employees: list[dict[str, str]],
) -> list[dict[str, object]]:
    """Convert salaries and calculate a new salary for each employee."""
    transformed_employees: list[dict[str, object]] = []
    for employee in employees:
        salary = float(employee["salary"])
        new_salary = increase_salary(salary, 10)
        transformed_employees.append(
            {
                "employee_id": employee["employee_id"],
                "name": employee["name"],
                "salary": salary,
                "new_salary": int(new_salary)
                if new_salary.is_integer()
                else new_salary,
            }
        )
    return transformed_employees


def load(
    employees: list[dict[str, object]],
    path: Path,
) -> None:
    """Write transformed employee records back to a CSV file."""
    fieldnames = ["employee_id", "name", "salary", "new_salary"]
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow(
                {
                    "employee_id": employee["employee_id"],
                    "name": employee["name"],
                    "salary": _format_csv_value(employee["salary"]),
                    "new_salary": _format_csv_value(employee["new_salary"]),
                }
            )


def print_summary(
    employees: list[dict[str, object]],
) -> None:
    """Print a summary of the processed employee records."""
    count = len(employees)
    average_salary = _average(employees, "salary")
    average_new_salary = _average(employees, "new_salary")

    print(f"Employees processed: {count}")
    print(f"Average salary: {average_salary:.0f}")
    print(f"Average new salary: {average_new_salary:.0f}")


def _average(
    employees: list[dict[str, object]],
    key: str,
) -> float:
    total = 0.0
    count = 0
    for employee in employees:
        value = employee.get(key)
        if isinstance(value, (int, float)):
            total += float(value)
            count += 1
    return total / count if count > 0 else 0.0


def _format_csv_value(value: object) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main() -> None:
    """Run the ETL pipeline."""
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "input" / "employees.csv"
    output_path = base_dir / "data" / "output" / "employees_transformed.csv"

    employees = extract(input_path)
    transformed_employees = transform(employees)
    load(transformed_employees, output_path)
    print_summary(transformed_employees)


if __name__ == "__main__":
    main()
