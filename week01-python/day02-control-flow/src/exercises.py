weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI given weight and height."""
    return weight / height**2


calculate_bmi(weight, height)
print(f"Your BMI is: {calculate_bmi(weight, height):.2f}")

# Mini Data Engineering Exercise
temperatures = [12, 18, 25, 31, 28, 15]


def classify_temperature(temp: int) -> str:
    """Classify temperatures as 'Cold', 'Warm' and 'Hot'."""
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 24:
        return "Warm"
    else:
        return "Hot"


for temp in temperatures:
    classification = classify_temperature(temp)
    print(f"{temp} -> {classification}")


salaries = [32000, 45000, 60000, 75000, 90000]


def classify_salary(salary: int) -> str:
    """Classify salaries as 'Low', 'Medium' and 'High'."""
    if salary < 40000:
        return "Low"
    elif 40000 <= salary <= 70000:
        return "Medium"
    else:
        return "High"


for salary in salaries:
    classification = classify_salary(salary)
    print(f"{salary} -> {classification}")
