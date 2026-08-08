# Week 02 SQL Notes

## Core Concepts

- Relational databases: Store data in related tables, using keys to connect records across entities.
- Tables: Structured containers for data, usually representing one entity (for example, employees or departments).
- Rows: Individual records in a table (one employee = one row).
- Columns: Attributes of each record (for example, first_name, salary, hire_date).
- Primary key: A column (or set of columns) that uniquely identifies each row in a table.
- Foreign key: A column that references a primary key in another table to enforce relationships and data integrity.

## Query Basics

- SELECT: Chooses which columns or expressions to return in the result.
- FROM: Chooses which table (or tables) the data should come from.
- DISTINCT: Removes duplicate values from query results.
- LIMIT: Restricts how many rows are returned.
- Column aliases: Renames output columns with AS for readability (for example, salary AS monthly_salary).
- SQL comments: Used to document queries.
  - Single-line comment: -- comment text
  - Multi-line comment: /* comment text */

## Filtering, Sorting, and Data Changes

- WHERE: Filters rows before results are returned.
  - WHERE is one of the most important clauses in SQL for both correctness and performance because it narrows the dataset early.
- Comparison operators: Used inside filters, including =, !=, >, <, >=, <=.
- AND: Combines multiple conditions and requires all to be true.
- OR: Combines conditions and requires at least one to be true.
- NOT: Negates a condition.
- IN: Matches a value against a list of allowed values.
- BETWEEN: Filters a value within an inclusive range.
- LIKE: Pattern matching with wildcards such as % and _.
- IS NULL: Filters rows where a column has no value.
- ORDER BY: Sorts rows, ascending by default, descending with DESC.
- LIMIT: Caps the number of rows returned.
- INSERT: Adds new rows to a table.
- UPDATE: Modifies existing rows, usually with a WHERE clause.
- DELETE: Removes rows, usually with a WHERE clause.

## Aggregation and Reporting

Aggregate functions summarize many rows into one value. Combined with GROUP BY, they allow SQL to produce reports and business metrics directly from raw data.

- COUNT(): Counts rows (or non-NULL values in a specific column).
  - Example: COUNT(*) returns total row count.
- SUM(): Adds numeric values.
  - Example: SUM(salary) returns total payroll.
- AVG(): Returns the average of numeric values.
  - Example: AVG(salary) returns mean salary.
- MIN(): Returns the smallest value.
  - Example: MIN(hire_date) returns earliest hire date.
- MAX(): Returns the largest value.
  - Example: MAX(salary) returns highest salary.
- GROUP BY: Splits rows into groups, then applies aggregate functions per group.
  - Example: GROUP BY department_id gives one summary row per department.
- HAVING: Filters grouped results after aggregation.
  - Example: HAVING AVG(salary) > 40000 keeps only high-average departments.

### WHERE vs HAVING

- WHERE filters individual rows before grouping and aggregation.
- HAVING filters grouped rows after GROUP BY and aggregate calculations.
- Rule of thumb: use WHERE for row-level filtering, HAVING for aggregate-level filtering.

### SQL Execution Order (Logical)

1. FROM / JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

## Why SQL Is Declarative

SQL is declarative because you describe what result you want, not the exact step-by-step procedure to fetch it.

You write intent, such as:
- which columns to return
- which table to read from
- which filters, groups, or sort order to apply

Then the database engine decides how to execute the query internally (for example, index scan, sequential scan, join strategy, and execution order optimizations). This separation lets you focus on business logic while the optimizer chooses an efficient retrieval strategy.

## Relationships and Joins

- Primary key: A unique identifier for each row in a table.
- Foreign key: A column that references a primary key in another table to create a relationship.
- One-to-many relationship: One row in a parent table can relate to many rows in a child table (for example, one department to many employees).
- INNER JOIN: Returns only rows where join keys match in both tables.
- LEFT JOIN: Returns all rows from the left table and matching rows from the right table.
- RIGHT JOIN: Returns all rows from the right table and matching rows from the left table.
- FULL OUTER JOIN: Returns all rows from both tables, with NULL where no match exists.
- Table aliases: Short names for tables (for example, e for employees) to make joins easier to read and write.
- COALESCE(): Returns the first non-NULL value from a list of expressions and is useful for default values in reports.

INNER JOIN returns only matching rows. LEFT JOIN returns all rows from the left table and matching rows from the right table. This makes LEFT JOIN especially useful for finding missing or unmatched data in ETL pipelines.

## Subqueries and CTEs

- Scalar subquery: Returns exactly one value and is often used in a SELECT list or WHERE clause.
- Multi-row subquery: Returns multiple values and is commonly used with IN, ANY, or ALL.
- Derived table: A subquery used in the FROM clause, treated like a temporary table.
- CTE (Common Table Expression): A named temporary result set defined with WITH that makes complex SQL easier to read.
- Multiple CTEs: Several CTEs can be chained together to break a problem into logical steps.
- Why CTEs improve readability: They break a large query into smaller, named building blocks, which makes logic easier to follow and debug.
- When to choose a CTE instead of a nested subquery: Use a CTE when the query becomes long, layered, or needs to be reused in several parts of the same statement.

CTEs don't necessarily make a query faster, but they often make it much easier to understand, maintain, and debug. In analytics engineering and dbt, complex transformations are commonly built as a sequence of readable CTEs.
