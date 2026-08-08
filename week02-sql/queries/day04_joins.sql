SELECT e.employee_id, e.first_name, d.department_name
FROM employees AS e
    INNER JOIN departments AS d ON e.department_id = d.department_id;

SELECT e.first_name, e.last_name, d.department_name, e.salary
FROM employees AS e
    INNER JOIN departments AS d ON e.department_id = d.department_id;

SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id;

SELECT c.customer_name
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
WHERE
    o.order_id IS NULL;

SELECT c.customer_name, o.order_id
FROM customers AS c
    RIGHT JOIN orders AS o ON c.customer_id = o.customer_id;

SELECT c.customer_name, o.order_id
FROM customers AS c FULL OUTER
    JOIN orders AS o ON c.customer_id = o.customer_id;

SELECT e.first_name, d.department_name
FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id;

SELECT d.department_name, COUNT(*) AS employee_count
FROM employees AS e
    INNER JOIN departments AS d ON e.department_id = d.department_id
GROUP BY
    d.department_name;

SELECT d.department_name, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees AS e
    INNER JOIN departments AS d ON e.department_id = d.department_id
GROUP BY
    d.department_name;

SELECT c.customer_name, SUM(o.amount) AS total_spent
FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_name;

SELECT c.customer_name, COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_name;

-- Show: Employee name Department name
SELECT e.first_name, d.department_name
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id;

-- Show: Employee name Department Salary Order by highest salary.
SELECT e.first_name, d.department_name, e.salary
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
ORDER BY e.salary DESC;

-- Count employees per department.
SELECT d.department_name, COUNT(*) AS employee_count
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name;

-- Average salary per department.
SELECT d.department_name, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name;

-- Show every customer and every order. Use LEFT JOIN to include customers without orders.
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id;

-- Find customers without orders.
SELECT c.customer_name
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
WHERE
    o.order_id IS NULL;

-- Calculate total spending for every customer.
SELECT c.customer_name, COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_name;

-- Show departments with average salary above 40, 000.
SELECT d.department_name, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name
HAVING
    AVG(e.salary) > 40000;

-- Show the department with the highest payroll.
SELECT d.department_name, SUM(e.salary) AS total_payroll
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name
ORDER BY total_payroll DESC
LIMIT 1;

-- Create a report containing:
-- Department
-- Employee count
-- Total payroll
-- Average salary
-- Highest salary
SELECT
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    SUM(e.salary) AS total_payroll,
    ROUND(AVG(e.salary), 2) AS average_salary,
    MAX(e.salary) AS highest_salary
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name
ORDER BY total_payroll DESC;

-- Which department has the most employees ?
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name
ORDER BY employee_count DESC
LIMIT 1;

-- Which customer has spent the most ?
SELECT c.customer_name, COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_name
ORDER BY total_spent DESC
LIMIT 1;

-- Which customers have never placed an order ?
SELECT c.customer_name
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
WHERE
    o.order_id IS NULL;

-- Which department has the highest average salary ?
SELECT d.department_name, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees AS e
    INNER JOIN departments AS d ON d.department_id = e.department_id
GROUP BY
    d.department_name
ORDER BY average_salary DESC
LIMIT 1;

-- What is the total revenue from all orders ?
SELECT COALESCE(SUM(o.amount), 0) AS total_revenue FROM orders AS o;