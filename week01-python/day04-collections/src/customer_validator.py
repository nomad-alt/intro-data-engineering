"""Validate and summarize customer records."""

customers = [
    {
        "customer_id": 101,
        "name": "Amina Hassan",
        "email": "amina@example.com",
        "country": "Sweden",
    },
    {
        "customer_id": 102,
        "name": "",
        "email": "yusuf@example.com",
        "country": "Norway",
    },
    {
        "customer_id": 103,
        "name": "Sara Ali",
        "email": None,
        "country": "Sweden",
    },
    {
        "customer_id": 101,
        "name": "Duplicate Customer",
        "email": "duplicate@example.com",
        "country": "Denmark",
    },
    {
        "customer_id": 104,
        "name": "Omar Ibrahim",
        "country": "Finland",
    },
]


def validate_customers(
    customers: list[dict[str, object]],
) -> dict[str, object]:
    """Validate customer records and return a summary."""
    seen_customer_ids: set[int] = set()
    invalid_customer_ids: list[int] = []
    unique_countries: set[str] = set()
    validation_errors: list[dict[str, object]] = []

    valid_count = 0
    invalid_count = 0

    for customer in customers:
        customer_id = customer.get("customer_id")
        name = customer.get("name")
        email = customer.get("email")
        country = customer.get("country")

        errors: list[str] = []

        # Check for missing ID first
        if not isinstance(customer_id, int):
            errors.append("missing customer ID")

        # Field-level validation
        if not (isinstance(name, str) and bool(name.strip())):
            errors.append("missing name")
        if not (isinstance(email, str) and bool(email.strip())):
            errors.append("missing email")
        if not (isinstance(country, str) and bool(country.strip())):
            errors.append("missing country")

        # Duplicate check (only meaningful when an int ID exists)
        if isinstance(customer_id, int) and customer_id in seen_customer_ids:
            errors.append("duplicate customer ID")

        if errors:
            invalid_count += 1
            if isinstance(customer_id, int):
                invalid_customer_ids.append(customer_id)
            validation_errors.append(
                {
                    "customer_id": customer_id,
                    "errors": errors,
                }
            )
        else:
            valid_count += 1
            if isinstance(country, str):
                unique_countries.add(country.strip())

        # Record the ID so future records can be detected as duplicates
        if isinstance(customer_id, int):
            seen_customer_ids.add(customer_id)

    return {
        "total_count": len(customers),
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "unique_country_count": len(unique_countries),
        "invalid_customer_ids": invalid_customer_ids,
        "validation_errors": validation_errors,
    }


def print_summary(summary: dict[str, object]) -> None:
    """Print a formatted customer-validation summary."""
    print(f"Total customers: {summary['total_count']}")
    print(f"Valid customers: {summary['valid_count']}")
    print(f"Invalid customers: {summary['invalid_count']}")
    print(f"Unique countries: {summary['unique_country_count']}")
    print(f"Invalid customer IDs: {summary['invalid_customer_ids']}")


def main() -> None:
    """Run the customer validator."""
    summary = validate_customers(customers)
    print_summary(summary)


if __name__ == "__main__":
    main()
