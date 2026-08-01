"""Process and summarize transaction records."""

transactions = [
    {"transaction_id": 1001, "amount": 150.0, "status": "valid"},
    {"transaction_id": 1002, "amount": 75.5, "status": "valid"},
    {"transaction_id": 1003, "amount": None, "status": "invalid"},
    {"transaction_id": 1004, "amount": 220.0, "status": "valid"},
    {"transaction_id": 1005, "amount": -50.0, "status": "invalid"},
]


def summarize_transactions(
    transactions: list[dict[str, object]],
) -> dict[str, object]:
    """Calculate summary statistics for transactions."""
    valid_count = 0
    invalid_count = 0
    total_valid_amount = 0.0
    invalid_transaction_ids: list[int] = []

    for transaction in transactions:
        if transaction["status"] == "valid":
            valid_count += 1
            total_valid_amount += float(transaction["amount"])
        else:
            invalid_count += 1
            invalid_transaction_ids.append(int(transaction["transaction_id"]))
            continue

    average_amount = total_valid_amount / valid_count if valid_count > 0 else 0.0

    return {
        "total_count": len(transactions),
        "valid_count": valid_count,
        "invalid_count": invalid_count,
        "total_valid_amount": total_valid_amount,
        "average_valid_amount": average_amount,
        "invalid_transaction_ids": invalid_transaction_ids,
    }


def print_summary(summary: dict[str, object]) -> None:
    """Print a formatted transaction summary."""
    print(f"Total transactions: {summary['total_count']}")
    print(f"Valid transactions: {summary['valid_count']}")
    print(f"Invalid transactions: {summary['invalid_count']}")
    print(f"Total valid amount: ${summary['total_valid_amount']:.2f}")
    print(
        f"Average amount per valid transaction: ${summary['average_valid_amount']:.2f}"
    )
    print(f"Invalid transaction IDs: {summary['invalid_transaction_ids']}")


def main() -> None:
    """Run the transaction processor."""
    summary = summarize_transactions(transactions)
    print_summary(summary)


if __name__ == "__main__":
    main()
