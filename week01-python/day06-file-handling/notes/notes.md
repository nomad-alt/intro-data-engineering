# Day 6 Notes — Python File Handling

## pathlib

The `pathlib` module provides an object-oriented way to work with file paths. It is more readable and cross-platform than string-based path manipulation.

```python
from pathlib import Path

# Create a path
p = Path("data/input/employees.csv")

# Get the file name
print(p.name)  # "employees.csv"

# Get the parent directory
print(p.parent)  # data/input

# Check if a file exists
if p.exists():
    print("File found")
```

## Path

A `Path` object represents a file or directory.

```python
# Absolute path
p = Path("/Users/alice/data.csv")

# Relative path
p = Path("data/input/employees.csv")

# Build paths by joining
base = Path("data")
input_file = base / "input" / "employees.csv"

# Get the current script's directory
script_dir = Path(__file__).resolve().parent
```

## Context Managers

A **context manager** (using `with`) automatically handles setup and cleanup. Files are opened and closed safely.

```python
# Without context manager (risky — file may not close)
f = open("data.csv", "r")
content = f.read()
# If an error occurs before this line, the file leaks:
f.close()

# With context manager (safe — file always closes)
with open("data.csv", "r") as f:
    content = f.read()
# File is automatically closed, even if an error occurs
```

## Reading Text

Read an entire file into a string:

```python
from pathlib import Path

p = Path("data.txt")
with p.open("r", encoding="utf-8") as f:
    content = f.read()

# Or read line by line
with p.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## Writing Text

Write strings to a file:

```python
p = Path("output.txt")
with p.open("w", encoding="utf-8") as f:
    f.write("Hello, World\n")
    f.write("Line 2\n")
```

## Reading CSV

Use the `csv` module to read CSV files correctly (handles quotes, escapes, etc.):

```python
import csv
from pathlib import Path

p = Path("employees.csv")
with p.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # row is a dictionary
```

## Writing CSV

Write dictionaries back to CSV:

```python
import csv
from pathlib import Path

employees = [
    {"employee_id": 1, "name": "Alice", "salary": 35000},
    {"employee_id": 2, "name": "Bob", "salary": 42000},
]

p = Path("output.csv")
fieldnames = ["employee_id", "name", "salary"]
with p.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)
```

## Reading JSON

Parse JSON into Python objects:

```python
import json
from pathlib import Path

p = Path("data.json")
with p.open("r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)  # Python dict or list
```

## Writing JSON

Serialize Python objects to JSON:

```python
import json
from pathlib import Path

data = {
    "employee_id": 1,
    "name": "Alice",
    "salary": 35000,
}

p = Path("output.json")
with p.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

## Exception Handling

Handle file errors gracefully:

```python
from pathlib import Path

p = Path("data.csv")

try:
    with p.open("r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: {p} not found")
except PermissionError:
    print(f"Error: No permission to read {p}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Why CSV Values Are Strings and Must Be Converted

When reading CSV files, **all values are strings**. This is because CSV is a text format — it has no data types.

```python
# Raw CSV data
# employee_id,name,salary
# 1,Alice,35000

# After reading with csv.DictReader:
row = {"employee_id": "1", "name": "Alice", "salary": "35000"}
#      ^ still strings!

# You must convert
employee_id = int(row["employee_id"])      # "1" → 1
salary = float(row["salary"])              # "35000" → 35000.0
```

Why? Because:
- CSV has no schema or type information
- Everything is text until you explicitly convert
- This is the same for JSON loaded from files (values start as strings)

Always validate and convert CSV values before using them for calculations or storage.

## ETL Overview

**ETL** stands for Extract, Transform, Load:

### Extract
Read data from a source (CSV, JSON, database, API).

```python
def extract(path: Path) -> list[dict]:
    with path.open("r") as f:
        reader = csv.DictReader(f)
        return list(reader)
```

### Transform
Clean, validate, and restructure the data. Convert types, merge, filter, etc.

```python
def transform(rows: list[dict]) -> list[dict]:
    transformed = []
    for row in rows:
        row["salary"] = float(row["salary"])  # Convert type
        row["new_salary"] = row["salary"] * 1.1  # Calculate
        transformed.append(row)
    return transformed
```

### Load
Write the processed data to a destination (CSV, database, data warehouse).

```python
def load(rows: list[dict], path: Path) -> None:
    with path.open("w") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
```

### Full Pipeline

```python
def main():
    data = extract(Path("input.csv"))
    transformed = transform(data)
    load(transformed, Path("output.csv"))
```

ETL pipelines are fundamental to data engineering. Production systems use frameworks like Apache Airflow, dbt, or Spark to orchestrate ETL at scale.
