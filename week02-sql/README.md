# Week 02 SQL

## Objective

Build hands-on SQL fundamentals by designing a small relational database, loading sample business data, and writing progressively more advanced analytical queries.

## Database Schema

This project uses two related tables:

- departments
  - department_id INTEGER PRIMARY KEY
  - department_name VARCHAR(100) NOT NULL
- employees
  - employee_id INTEGER PRIMARY KEY
  - first_name VARCHAR(100) NOT NULL
  - last_name VARCHAR(100) NOT NULL
  - department_id INTEGER NOT NULL
  - salary NUMERIC(10, 2) NOT NULL
  - hire_date DATE NOT NULL
  - FOREIGN KEY department_id references departments.department_id

Schema files:
- schema/create_tables.sql
- schema/drop_tables.sql
- schema/seed_data.sql

## Topics Learned

- SELECT fundamentals and column projection
- Filtering with WHERE conditions
- Aggregations and GROUP BY
- JOINs between related tables
- Common Table Expressions (CTEs)
- Window functions for advanced reporting
- Query formatting and SQL comments

## How To Create The Database

From the repository root:

```bash
psql -U postgres -h localhost -p 5432 -d postgres -c "CREATE DATABASE company_db;"
```

If the database already exists, you can skip this step.

## How To Load Data

1. Create tables:

```bash
psql -U postgres -h localhost -p 5432 -d company_db -f week02-sql/schema/create_tables.sql
```

2. Seed data:

```bash
psql -U postgres -h localhost -p 5432 -d company_db -f week02-sql/schema/seed_data.sql
```

3. Validate loaded rows:

```bash
psql -U postgres -h localhost -p 5432 -d company_db -c "SELECT COUNT(*) FROM departments;"
psql -U postgres -h localhost -p 5432 -d company_db -c "SELECT COUNT(*) FROM employees;"
```

## How To Run Queries

Run a single query file:

```bash
psql -U postgres -h localhost -p 5432 -d company_db -f week02-sql/queries/day01_select.sql
```

Run any day file the same way:

```bash
psql -U postgres -h localhost -p 5432 -d company_db -f week02-sql/queries/day04_joins.sql
```

Or open an interactive session and run scripts with \i:

```bash
psql -U postgres -h localhost -p 5432 -d company_db
```

Inside psql:

```sql
\i week02-sql/schema/create_tables.sql
\i week02-sql/schema/seed_data.sql
\i week02-sql/queries/day01_select.sql
```
