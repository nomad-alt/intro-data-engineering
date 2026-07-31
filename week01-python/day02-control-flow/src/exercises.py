weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI given weight and height."""
    return weight / height**2


calculate_bmi(weight, height)
print(f"Your BMI is: {calculate_bmi(weight, height):.2f}")
