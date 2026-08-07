-- Day 01: SELECT fundamentals

-- Basic query: return all columns
SELECT * FROM employees;

-- Selecting individual columns (only two columns returned)
SELECT first_name, salary FROM employees;

-- Column order: SQL returns columns in the order requested
SELECT salary, first_name FROM employees;

-- Column aliases: make report columns easier to read
SELECT
    first_name AS employee_name,
    salary AS monthly_salary
FROM employees;

-- LIMIT: return only a few rows
SELECT * FROM employees LIMIT 3;

-- DISTINCT: remove duplicate values
SELECT DISTINCT department_id FROM employees;

-- Arithmetic in SELECT: calculate increased salary
SELECT
    first_name,
    salary,
    salary * 1.10 AS increased_salary
FROM employees;

-- String concatenation: first_name + last_name
SELECT first_name || ' ' || last_name AS full_name FROM employees;

-- Single-line comment example
-- Show employee names
SELECT first_name FROM employees;

/*
Show salary report
for finance team
*/
SELECT first_name, salary FROM employees WHERE department_id = 4;

-- Formatting example (recommended style)
SELECT first_name, salary FROM employees LIMIT 5;

SELECT first_name, last_name FROM employees;

SELECT salary, hire_date FROM employees;

SELECT first_name AS employee_name FROM employees;

SELECT * FROM employees LIMIT 2;

SELECT DISTINCT department_id FROM employees;

SELECT
    first_name || ' ' || last_name AS full_name,
    salary,
    salary * 1.15 AS increased_salary
FROM employees;

SELECT 'Employee: ' || first_name
FROM employees
WHERE
    first_name = 'Alice';