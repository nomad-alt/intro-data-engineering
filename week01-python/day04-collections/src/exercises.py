"""Exercises covering Python lists, tuples, sets, and dictionaries."""

# Exercise 1 — List operations
datasets = [
    "customers",
    "orders",
    "products",
]

datasets.append("payments")
datasets.insert(1, "employees")
datasets.remove("products")

print(f"Datasets: {datasets}")
print(f"Dataset count: {len(datasets)}")

# Exercise 2 — Dataset slicing
daily_row_counts = [
    1_200,
    1_350,
    1_100,
    1_500,
    1_425,
    1_600,
    1_550,
]

print(f"First three days: {daily_row_counts[:3]}")
print(f"Last three days: {daily_row_counts[-3:]}")
print(f"Every second day: {daily_row_counts[::2]}")
print(f"The maximum row count: {max(daily_row_counts)}")
print(f"The minimum row count: {min(daily_row_counts)}")

# Exercise 3 — Remove duplicates
customer_countries = [
    "Sweden",
    "Norway",
    "Sweden",
    "Denmark",
    "Norway",
    "Finland",
]

unique_countries = set(customer_countries)
print(f"Unique countries: {unique_countries}")
print(f"Number of unique countries: {len(unique_countries)}")


# Exercise 4 — Compare record IDs
source_ids = {1001, 1002, 1003, 1004, 1005}
target_ids = {1002, 1003, 1004, 1006}

matching_ids = source_ids & target_ids
print(f"Matching record IDs: {matching_ids}")

missing_from_target = source_ids - target_ids
print(f"IDs missing from target: {missing_from_target}")

only_in_target = target_ids - source_ids
print(f"IDs only in target: {only_in_target}")

all_unique_ids = source_ids | target_ids
print(f"All unique IDs: {all_unique_ids}")

# Exercise 5 — Dictionary access
order = {
    "order_id": 5001,
    "customer_id": 101,
    "amount": 799.0,
    "currency": "SEK",
}

print(f"Order ID: {order['order_id']}")
print(f"Amount: {order['amount']}")
print(f"Currency: {order['currency']}")
print(f"payment_method: {order.get('payment_method', 'Unknown')}")

# Exercise 6 — Update a dictionary
# Add status: pending
order["status"] = "pending"
# Change the status to "completed"
order["status"] = "completed"
# Remove the currency key
removed_currency = order.pop("currency")
print(f"Removed currency: {removed_currency}")

print(f"Updated order: {order}")


# Exercise 7 — Process nested records
orders = [
    {
        "order_id": 1,
        "amount": 100.0,
        "status": "completed",
    },
    {
        "order_id": 2,
        "amount": 250.0,
        "status": "pending",
    },
    {
        "order_id": 3,
        "amount": 75.0,
        "status": "completed",
    },
    {
        "order_id": 4,
        "amount": 125.0,
        "status": "cancelled",
    },
]

total_order_count = len(orders)
completed_order_count = sum(1 for order in orders if order["status"] == "completed")
total_completed_amount = sum(
    order["amount"] for order in orders if order["status"] == "completed"
)
non_completed_order_ids = [
    order["order_id"] for order in orders if order["status"] != "completed"
]


# Exercise 8 — List comprehension
order_ids = [order["order_id"] for order in orders]
print(f"Order IDs: {order_ids}")

completed_order_ids = [
    order["order_id"] for order in orders if order["status"] == "completed"
]
print(f"Completed order IDs: {completed_order_ids}")

high_value_orders = [order["amount"] for order in orders if order["amount"] > 100]
print(f"High value orders: {high_value_orders}")

increased_amounts = [order["amount"] * 1.25 for order in orders]
print(f"Increased amounts: {increased_amounts}")
