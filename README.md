# Introduction to Data Engineering

A hands-on introduction to the core skills and concepts used in **Data Engineering**.

This repository documents my first three weeks of practical Data Engineering study, focusing on building a strong foundation in **Python, SQL, and ETL pipelines**.

The goal is not only to learn individual technologies, but to understand how data moves through a real system:

**Raw Data → Extract → Transform → Validate → Load → Query**

## What I've Covered

### Week 1 — Python Foundations

Focused on Python fundamentals used in Data Engineering.

Topics include:

* Variables and data types
* Conditionals
* Loops
* Functions
* Lists and dictionaries
* File handling
* Error handling
* Writing reusable functions
* Basic testing with `pytest`

The focus was on writing clean, readable Python rather than only solving isolated exercises.

---

### Week 2 — SQL Foundations

Focused on querying and working with relational data.

Topics include:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `GROUP BY`
* Aggregate functions
* `JOIN`
* Subqueries
* Common Table Expressions (CTEs)
* Window functions
* Basic database design

The goal was to become comfortable using SQL to explore, transform, and analyze structured data.

---

### Week 3 — ETL Pipelines

Combined Python and data-processing concepts to build simple ETL workflows.

Topics include:

* Extracting data from CSV and JSON
* Transforming datasets
* Cleaning missing and invalid values
* Converting data types
* Data validation
* Loading transformed data
* Structuring ETL code into reusable functions
* Logging and error handling
* Testing pipeline logic

Example pipeline:

```text
CSV / JSON
    ↓
Extract
    ↓
Validate
    ↓
Transform
    ↓
Load
    ↓
Clean Dataset
```

## Technologies

* Python
* SQL
* PostgreSQL
* SQLite
* Pandas
* pytest
* Git
* GitHub
* VS Code

## Repository Structure

```text
intro-to-data-engineering/
│
├── week01-python/
├── week02-sql/
├── week03-etl/
│
├── datasets/
├── docs/
│
├── .gitignore
├── LICENSE
└── README.md
```

Each week contains exercises, notes, and small projects focused on applying the concepts in practice.

## What I Learned

After completing these three weeks, I have a better understanding of how the main Data Engineering fundamentals connect.

Python provides the programming foundation.

SQL provides the ability to work efficiently with structured data.

ETL brings those skills together by extracting data from a source, validating and transforming it, and loading the result into another system.

The biggest takeaway is that Data Engineering is not only about moving data. A good pipeline should also be:

* Reliable
* Maintainable
* Testable
* Reproducible
* Easy to understand

## Next Steps

This repository represents my **Introduction to Data Engineering** phase.

The next stage is to build on these foundations with technologies and concepts such as:

* PostgreSQL
* Data modelling
* Docker
* Apache Airflow
* dbt
* Apache Spark
* Parquet
* Azure
* Data warehouses
* Production-style data pipelines

## Goal

The long-term goal is to progress from small learning exercises toward production-style Data Engineering projects that demonstrate:

* Clean architecture
* Automated pipelines
* Data quality checks
* Testing
* Database design
* Orchestration
* Cloud integration
* Professional documentation

This repository serves as the foundation for that journey.
