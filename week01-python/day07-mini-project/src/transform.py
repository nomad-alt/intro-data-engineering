def transform(
    employees: list[dict[str, str]],
) -> list[dict[str, object]]:
    """Transform employees data."""
    transformed_employees: list[dict[str, object]] = []

    for employee in employees:
        salary = float(employee["salary"])
        new_salary = salary * 1.10

        if salary < 35000:
            salary_band = "Junior"
        elif salary < 40000:
            salary_band = "Mid"
        else:
            salary_band = "Senior"

        transformed_employees.append(
            {
                "employee_id": employee["employee_id"],
                "name": employee["name"],
                "department": employee["department"],
                "salary": salary,
                "new_salary": new_salary,
                "salary_band": salary_band,
            }
        )

    return transformed_employees
