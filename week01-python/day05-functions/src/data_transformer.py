employees = [
    {
        "employee_id": 1,
        "name": "Alice",
        "salary": 35000,
    },
    {
        "employee_id": 2,
        "name": "Bob",
        "salary": 42000,
    },
    {
        "employee_id": 3,
        "name": "John",
        "salary": 28000,
    },
]


def increase_salary(
    salary: float,
    percentage: float,
) -> float:
    """Increase salary by a given percentage."""
    return salary * (1 + percentage / 100)


increase_salary(1000, 10)


def transform_employee(
    employee: dict[str, object],
) -> dict[str, object]:
    """Transform employee data by increasing salary."""
    salary = employee.get("salary")
    if isinstance(salary, (int, float)):
        salary_value = float(salary)
        new_salary_value = increase_salary(salary_value, 10)
        new_salary = (
            int(new_salary_value) if isinstance(salary, int) else new_salary_value
        )
    else:
        new_salary = None

    return {
        "employee_id": employee.get("employee_id"),
        "name": employee.get("name"),
        "salary": salary,
        "new_salary": new_salary,
    }


def transform_employees(
    employees: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Transform a list of employee records without modifying the original list."""
    transformed_employees = []
    for employee in employees:
        transformed_employees.append(transform_employee(employee))
    return transformed_employees


def average_salary(
    employees: list[dict[str, object]],
) -> float:
    """Calculate the average salary of employees."""
    total_salary = 0.0
    count = 0
    for employee in employees:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)):
            total_salary += float(salary)
            count += 1
    return total_salary / count if count > 0 else 0.0


def highest_salary(
    employees: list[dict[str, object]],
) -> float:
    """Find the highest salary among employees."""
    max_salary = float("-inf")
    for employee in employees:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)):
            max_salary = max(max_salary, float(salary))
    return max_salary if max_salary != float("-inf") else 0.0


def print_summary(
    employees: list[dict[str, object]],
) -> None:
    """Print a summary of employee salaries."""
    avg_salary = average_salary(employees)
    max_salary = highest_salary(employees)
    print(f"Employees: {len(employees)}")
    print(f"Average salary: {avg_salary:.0f}")
    print(f"Highest salary: {max_salary:.0f}")


def main() -> None:
    """Run the complete transformation workflow."""
    transformed_employees = transform_employees(employees)
    print_summary(transformed_employees)


if __name__ == "__main__":
    main()
