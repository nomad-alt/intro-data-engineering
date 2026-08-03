"""Examples of Python functions."""


def greet() -> None:
    """Print a greeting."""
    print("Hello, Data Engineer!")


greet()


# Functions with Parameters
def greet(name: str) -> None:
    """Print a personalized greeting."""
    print(f"Hello, {name}!")


greet("Emil")
greet("Roua")


# Returning Values
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    return weight_kg / height_m**2


bmi = calculate_bmi(80, 1.82)

print(f"BMI: {bmi:.2f}")


# Type Hints
def square(number: int) -> int:
    return number * number


def add(a: int, b: int) -> int:
    return a + b


def total(values: list[int]) -> int:
    return sum(values)


def get_customer_name(customer: dict[str, str]) -> str:
    return customer["name"]


# Default Arguments
def connect(
    host: str,
    port: int = 5432,
) -> None:
    print(host, port)


connect("localhost")
connect("db.company.com", 5433)


# Keyword Arguments
connect(
    host="localhost",
    port=5432,
)


# Variable Scope
# Variables inside a function exist only inside that function.
def calculate() -> None:
    total = 100
    print(total)


calculate()


# Docstrings
def calculate_average(values: list[float]) -> float:
    """Calculate the arithmetic mean."""
    # Good docstrings explain what the function does, not every implementation detail.
