"""Calculate BMI using fixed weight and height values."""

weight_kg = float(input("Enter weight in kilograms: "))
height_m = float(input("Enter height in meters: "))

bmi = weight_kg / height_m**2

print(f"Weight: {weight_kg} kg")
print(f"Height: {height_m} m")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Healthy weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Category: {category}")

# TODO: Add input validation and error handling.
