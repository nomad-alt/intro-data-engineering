def kilograms_to_pounds(weight_kg: float) -> float:
    """Convert kilograms to pounds."""
    return weight_kg * 2.20462


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def count_valid_records(records: list[bool]) -> int:
    """Count the number of valid records in a list."""
    return sum(1 for record in records if record)


def unique_countries(customers: list[dict]) -> set[str]:
    """Return set of unique countries from a list of customer records."""
    return {
        customer["country"]
        for customer in customers
        if "country" in customer and isinstance(customer["country"], str)
    }


def full_name(
    first_name: str,
    last_name: str,
) -> str:
    """Return the full name of a person."""
    return f"{first_name} {last_name}"


def is_valid_email(email: str) -> bool:
    """Check if an email address is valid."""
    return "@" in email and "." in email
