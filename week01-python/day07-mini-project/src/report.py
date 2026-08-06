def generate_summary(employees: list[dict[str, object]]) -> dict[str, object]:
    """Generate a summary of employee salary data."""
    employee_count = 0
    total_salary = 0.0
    total_new_salary = 0.0
    highest_salary = 0.0
    lowest_salary = 0.0
    departments: dict[str, int] = {}

    for employee in employees:
        employee_count += 1
        salary = float(employee["salary"])
        new_salary = float(employee["new_salary"])
        department = str(employee["department"])

        total_salary += salary
        total_new_salary += new_salary

        if employee_count == 1:
            highest_salary = salary
            lowest_salary = salary
        else:
            highest_salary = max(highest_salary, salary)
            lowest_salary = min(lowest_salary, salary)

        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1

    average_salary = total_salary / employee_count if employee_count else 0
    average_new_salary = total_new_salary / employee_count if employee_count else 0

    return {
        "employee_count": employee_count,
        "average_salary": average_salary,
        "average_new_salary": average_new_salary,
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary,
        "departments": departments,
    }
