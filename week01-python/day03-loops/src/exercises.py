"""Day 3 exercises for practising Python loops."""

# Exercise 1 — Print dataset names
dataset_names = [
    "customers",
    "orders",
    "products",
    "payments",
]

for dataset_name in dataset_names:
    print(f"Processing dataset: {dataset_name}")

# Exercise 2 — Calculate total rows
row_counts = [1_200, 950, 1_500, 875]

total_rows = 0

for row_count in row_counts:
    total_rows += row_count

print(f"Total rows: {total_rows}")

# Exercise 3 — Count valid and invalid rows
row_statuses = [
    "valid",
    "valid",
    "invalid",
    "valid",
    "invalid",
    "valid",
]

valid_rows = 0
invalid_rows = 0

for row_status in row_statuses:
    if row_status == "valid":
        valid_rows += 1
    else:
        invalid_rows += 1

print(f"Valid rows: {valid_rows}")
print(f"Invalid rows: {invalid_rows}")

# Exercise 4 — Skip missing values
# Calculate the total of the remaining amounts.
transaction_amounts = [120.5, None, 75.0, 200.0, None, 49.5]
total_amount = 0

for amount in transaction_amounts:
    if amount is not None:
        total_amount += amount

print(f"Total transaction amount: {total_amount}")

# Exercise 5 — Find the first failed job
# Use enumerate(..., start=1).
job_statuses = [
    "success",
    "success",
    "failed",
    "success",
]

for index, job_status in enumerate(job_statuses, start=1):
    if job_status == "failed":
        print(f"Failed job detected at position: {index}")
        break

# Exercise 6 — Data quality percentage
records = [
    {"id": 1, "is_valid": True},
    {"id": 2, "is_valid": False},
    {"id": 3, "is_valid": True},
    {"id": 4, "is_valid": True},
    {"id": 5, "is_valid": False},
]

valid_records = 0
invalid_records = 0
valid_percentage = 0.0

for total_records, record in enumerate(records, start=1):
    if record["is_valid"]:
        valid_records += 1
    else:
        invalid_records += 1

valid_percentage = (valid_records / total_records) * 100

print(f"Total records: {total_records}")
print(f"Valid records: {valid_records}")
print(f"Invalid records: {invalid_records}")
print(f"Percentage of valid records: {valid_percentage:.2f}%")

# Exercise 7 — Batch processing
total_records = 1_050
batch_size = 200

batch_number = 1

while total_records > 0:
    records_in_batch = min(batch_size, total_records)
    print(f"Batch {batch_number}: {records_in_batch} records")

    total_records -= records_in_batch
    batch_number += 1
