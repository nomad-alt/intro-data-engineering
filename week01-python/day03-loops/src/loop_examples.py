"""Examples of Python loops used in data processing."""

dataset_names = [
    "customers.csv",
    "orders.csv",
    "products.csv",
]

for dataset_name in dataset_names:
    print(f"Processing {dataset_name}")

# A string is iterable, meaning Python can process it one character at a time.
file_extension = "csv"

for character in file_extension:
    print(character)

# Using range()
for batch_number in range(5):
    print(f"Processing batch {batch_number}")


# To start at 1
for batch_number in range(1, 6):
    print(f"Processing batch {batch_number}")

# To use a step:
for row_number in range(0, 101, 20):
    print(row_number)

# Data engineering use
# range() can simulate batch numbers or retry attempts:
for attempt_number in range(1, 4):
    print(f"Connection attempt {attempt_number}")


# Using enumerate()
# You often need both the item and its position.
column_names = ["customer_id", "name", "email"]

for index, column_name in enumerate(column_names):
    print(f"{index}: {column_name}")

# For numbering starting at 1:
for position, column_name in enumerate(column_names, start=1):
    print(f"{position}: {column_name}")

# Prefer enumerate() over manually managing an index
# The manual version is more error-prone.
# index = 0
# for column_name in column_names:
#    print(index, column_name)
#    index += 1

# Looping through dictionaries
customer = {
    "customer_id": 101,
    "name": "Amina",
    "country": "Sweden",
}

for key in customer:
    print(key)

for value in customer.values():
    print(value)

for key, value in customer.items():
    print(f"{key}: {value}")

# In data engineering, dictionaries frequently represent JSON records:
order = {
    "order_id": 5001,
    "customer_id": 101,
    "amount": 799.0,
}

# Accumulator pattern
# An accumulator stores a running result.
record_counts = [120, 85, 210, 95]

total_records = 0

for record_count in record_counts:
    total_records += record_count

print(f"Total records: {total_records}")

valid_record_counts = [100, 95, 0, 80]

total_valid_records = 0

for record_count in valid_record_counts:
    if record_count > 0:
        total_valid_records += record_count

print(f"Total valid records: {total_valid_records}")

# Counting records
validation_results = [True, True, False, True, False]

valid_count = 0
invalid_count = 0

for is_valid in validation_results:
    if is_valid:
        valid_count += 1
    else:
        invalid_count += 1

print(f"Valid records: {valid_count}")
print(f"Invalid records: {invalid_count}")

# continue skips the current iteration and moves to the next one.
# The missing values are ignored.
# Data pipelines commonly use this pattern to skip invalid or incomplete records.
row_values = [120, None, 85, None, 200]

for row_value in row_values:
    if row_value is None:
        continue

    print(f"Processing value: {row_value}")

# break ends the loop completely.
file_names = [
    "customers.csv",
    "orders.csv",
    "corrupted.csv",
    "products.csv",
]

for file_name in file_names:
    if file_name == "corrupted.csv":
        print("Corrupted file detected. Stopping pipeline.")
        break
    print(f"Processed {file_name}")

# A while loop continues while a condition remains true.
remaining_records = 450
batch_size = 100
batch_number = 1

while remaining_records > 0:
    records_in_batch = min(batch_size, remaining_records)

    print(f"Batch {batch_number}: processing {records_in_batch} records")

    remaining_records -= records_in_batch
    batch_number += 1

# Common mistake: infinite loops
# This never stops:
# remaining_records = 450
# while remaining_records > 0:
# print(remaining_records)

# A nested loop is a loop inside another loop.
datasets = {
    "customers": ["customer_id", "name", "email"],
    "orders": ["order_id", "customer_id", "amount"],
}

for dataset_name, columns in datasets.items():
    print(f"Dataset: {dataset_name}")

    for column_name in columns:
        print(f"  - {column_name}")

# Use nested loops carefully. For large datasets, they may cause performance problems.

# For example, looping through 10,000 customers and 10,000 orders produces up to:
# 10,000 × 10,000 = 100,000,000 comparisons
# In production, database joins, dictionaries, sets, Pandas, Polars, or Spark are often better choices.
