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
- Primary keys for unique row identification
- Foreign keys for table relationships and referential integrity
- Filtering data with WHERE conditions
- Sorting results with ORDER BY
- Pattern matching with LIKE and ILIKE
- Data modification with INSERT, UPDATE, and DELETE
- Handling NULL values with IS NULL, IS NOT NULL, and COALESCE()
- Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- GROUP BY for category-level summaries
- HAVING for filtering grouped results
- INNER JOIN for matched records only
- LEFT JOIN for all left-table rows and matched right-table rows
- RIGHT JOIN for all right-table rows and matched left-table rows
- FULL OUTER JOIN for all rows from both tables with NULL where unmatched
- Scalar subqueries for single-value results
- Multi-row subqueries for sets of values
- Derived tables for inline subqueries used as temporary result sets
- Common Table Expressions (CTEs)
- Multiple CTEs for cleaner, layered query logic
- Analytical queries for business reporting and metrics
- Reporting queries for business summaries
- Query execution order
- Window functions for advanced reporting
- OVER() for defining a window of rows
- PARTITION BY for dividing rows into groups within a window
- ROW_NUMBER() for assigning row numbers
- RANK() for ranking with gaps
- DENSE_RANK() for ranking without gaps
- LAG() for accessing a previous row value
- LEAD() for accessing a next row value
- Query formatting and SQL comments

## Window Functions vs GROUP BY

Window functions are different from GROUP BY because they do not collapse rows into one summary row per group. Instead, they keep the original rows and calculate additional values across a defined window of rows, which is useful for rankings, running totals, and comparisons with adjacent rows.

## Query Execution Order

SQL is written in one order but executed logically in another:

1. FROM / JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

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
