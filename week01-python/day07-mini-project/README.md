# Day 07 Mini Project

## Overview

This project demonstrates a basic ETL pipeline.

The pipeline reads employee data from a CSV file, applies salary transformations, generates summary statistics, and saves the results as both CSV and JSON outputs.

## Features

- Read CSV
- Transform data
- Generate statistics
- Save CSV
- Save JSON
- Unit tests

## Project Structure

```
week01-python/day07-mini-project/
├── README.md
├── data/
│   ├── input/
│   │   └── employees.csv
│   ├── employees_processed.csv
│   └── summary.json
├── notes/
│   └── notes.md
├── src/
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   ├── report.py
│   └── transform.py
└── tests/
    ├── test_load.py
    ├── test_main.py
    ├── test_report.py
    └── test_transform.py
```

## Running

```
python src/main.py
```

## Tests

```
pytest
```

## Code Quality

```
ruff check .
ruff format --check .
```

## Example Output

Sample report output:

```
Pipeline completed successfully.

Employees processed: 5

Output files:

employees_processed.csv

summary.json
```
