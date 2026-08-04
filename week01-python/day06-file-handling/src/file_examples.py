"""Examples of reading and writing files."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"

text_file = INPUT_DIR / "example.txt"

with text_file.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Reading line by line
with text_file.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# Writing Text Files
output_file = BASE_DIR / "data" / "output" / "output.txt"

with output_file.open("w", encoding="utf-8") as file:
    file.write("Hello Data Engineering!\n")


# Reading CSV Files

import csv

csv_file = INPUT_DIR / "employees.csv"

with csv_file.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

salary = float(row["salary"])
print(f"Employee {row['name']} has a salary of {salary:.2f}")


# Writing CSV Files
output_csv = BASE_DIR / "data" / "output" / "employees_new.csv"

rows = [
    {
        "employee_id": 1,
        "salary": 38500,
    }
]

with output_csv.open(
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["employee_id", "salary"],
    )

    writer.writeheader()
    writer.writerows(rows)

# Reading JSON Files
import json

json_file = INPUT_DIR / "customer.json"

with json_file.open(
    "r",
    encoding="utf-8",
) as file:
    customer = json.load(file)

print(customer)

# Writing JSON Files
output_json = BASE_DIR / "data" / "output" / "customer_new.json"

with output_json.open(
    "w",
    encoding="utf-8",
) as file:
    json.dump(customer, file, indent=4)


# Exception Handling
# In ETL pipelines, missing files are common.
try:
    with Path("missing.csv").open() as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
