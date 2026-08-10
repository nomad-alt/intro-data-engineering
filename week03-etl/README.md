# Week 03 ETL Pipeline

## Project Overview

This project demonstrates a simple ETL workflow for processing employee data. It reads employee records from a CSV file, transforms them into a cleaner format, and writes the results to output files. The pipeline is designed as a small, learn-by-building example of how data engineering projects are structured.

## ETL Architecture

The pipeline follows a simple extract, transform, and load flow:

1. Extract: read employee data from a CSV file.
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
