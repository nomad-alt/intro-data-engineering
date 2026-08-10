# Week 03 ETL Pipeline

## Project Overview

This project demonstrates a simple ETL workflow for processing employee data. It reads employee records from a CSV file, transforms them into a cleaner format, and writes the results to output files. The pipeline is designed as a small, learn-by-building example of how data engineering projects are structured.

## ETL Architecture

The pipeline follows a simple extract, transform, and load flow:

1. Extract: read employee data from supported input files.
2. Transform: clean and enrich the records.
3. Load: save the transformed data to CSV and JSON outputs.

The main modules are:

- src/extract.py: reads raw input data.
- src/transform.py: applies business rules to the data.
- src/load.py: writes results to files.
- src/pipeline.py: runs the complete workflow.

## Folder Structure

```text
week03-etl/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_pipeline.py
├── data/
│   └── employees.csv
└── README.md
```

## Supported Input Formats

The extractor supports:

- CSV files with the .csv extension
- JSON files with the .json extension

The dispatching logic in src/extract.py routes files to the appropriate parser automatically.

## CSV Extraction

CSV files are read with csv.DictReader and returned as a list of dictionaries. This makes the data easy to transform and process in later pipeline stages.

## JSON Extraction

JSON files are parsed with json.load and returned as structured Python objects. This is useful for source files that are already organized as arrays of records.

## Error Handling

The extraction layer raises clear errors for common issues:

- FileNotError for missing files
- RuntimeError for unreadable CSV or JSON files
- ValueError for unsupported file types

These messages make debugging easier while preserving the underlying cause.

## Logging

The pipeline uses Python logging to report progress during extraction. Logging is more suitable for production-style systems than print statements because it provides structured, configurable output.

## How to Install Dependencies

From the repository root, create and activate a virtual environment if needed, then install the project requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r week03-etl/requirements.txt
```

## How to Run the Pipeline

Run the ETL pipeline from the repository root:

```bash
python week03-etl/src/pipeline.py
```

This will read the employee CSV, transform the records, and create the output files.

## How to Run Tests

Run the test suite from the repository root:

```bash
pytest week03-etl/tests
```
