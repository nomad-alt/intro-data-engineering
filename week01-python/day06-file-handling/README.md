# Day 6 — Python File Handling

## Objective

Learn how to read and write files using `pathlib`, CSV, and JSON. Build a complete ETL (Extract, Transform, Load) pipeline from scratch.

## Topics Covered

- `pathlib` and `Path` for cross-platform file operations
- Context managers (`with` statement)
- Reading and writing text files
- CSV file operations with the `csv` module
- JSON serialization and deserialization
- Exception handling for file operations
- ETL pipeline architecture
- Type conversion for CSV data

## Files

- `src/etl_pipeline.py` — a complete ETL pipeline that reads employee data, transforms salaries, and writes results
- `tests/test_etl_pipeline.py` — unit tests for `increase_salary`, `transform`, and `extract`
- `data/input/employees.csv` — sample input data
- `data/output/employees_transformed.csv` — output written by the pipeline
- `notes/notes.md` — personal learning notes

## Running the Examples

From the repository root:

```bash
python week01-python/day06-file-handling/src/etl_pipeline.py
```

This runs the extraction, transformation, loading, and printing summary for the employee data.

## Running the Tests

From the repository root:

```bash
pytest week01-python/day06-file-handling/tests -v
```

## Code Quality

```bash
ruff check week01-python/day06-file-handling
ruff format --check week01-python/day06-file-handling
```

Format code automatically:

```bash
ruff format week01-python/day06-file-handling
```

## Data Engineering Relevance

**File handling is the foundation of almost every ETL pipeline.** Before data can be transformed or loaded into warehouses, data engineers must:

- Read raw files (CSV, JSON, Parquet, etc.)
- Parse and validate the content
- Convert data types and formats
- Handle errors and missing files gracefully
- Write results back to disk or load into databases

The ETL pipeline in this module demonstrates the core pattern:

1. **Extract**: `extract()` reads CSV using `pathlib` and `csv.DictReader`
2. **Transform**: `transform()` converts salary strings to floats and calculates new salaries
3. **Load**: `load()` writes the transformed data back to CSV

At scale, frameworks like Apache Airflow, dbt, Spark, and cloud services automate and orchestrate these steps. But the core concept — reading, processing, and writing data — remains the same.

### Why This Matters

- File I/O is the bottleneck in many data pipelines
- Correct type conversion prevents silent data corruption
- Proper error handling ensures pipelines don't fail silently
- Understanding CSV/JSON parsing helps debug data quality issues
- ETL patterns scale from local scripts to enterprise systems
