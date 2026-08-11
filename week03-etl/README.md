# CSV to Parquet ETL Pipeline

## Overview

A small ETL pipeline that extracts sales data from CSV,
validates and transforms the records, and writes the cleaned
dataset to Parquet.

## Pipeline

CSV → Extract → Transform → Parquet

## Transformations

- Remove records with missing required fields
- Remove quantities <= 0
- Standardize country names
- Calculate total order amount

## Tech Stack

- Python
- Pandas
- PyArrow
- pytest

## Run

```bash
pip install -r requirements.txt
python -m src.pipeline
```

## Test

```bash
pytest -v
```
