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

## Why SQL Is Declarative

SQL is declarative because you describe what result you want, not the exact step-by-step procedure to fetch it.

You write intent, such as:
- which columns to return
- which table to read from
- which filters, groups, or sort order to apply

Then the database engine decides how to execute the query internally (for example, index scan, sequential scan, join strategy, and execution order optimizations). This separation lets you focus on business logic while the optimizer chooses an efficient retrieval strategy.
