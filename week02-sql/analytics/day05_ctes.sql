SELECT first_name, salary
FROM employees
WHERE
    salary > (
        SELECT AVG(salary)
        FROM employees
    );

SELECT
    first_name,
    salary,
    (
        SELECT MAX(salary)
        FROM employees
    ) AS company_max_salary
FROM employees;

SELECT first_name, department_id
FROM employees
WHERE
    department_id IN (
        SELECT department_id
        FROM departments
        WHERE
            department_name IN ('Engineering', 'Sales')
    );

SELECT department_id, average_salary
FROM (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    ) AS department_summary;

WITH
    department_summary AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT *
FROM department_summary;

WITH
    department_summary AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    ),
    high_salary_departments AS (
        SELECT *
        FROM department_summary
        WHERE
            average_salary > 40000
    )
SELECT *
FROM high_salary_departments;

WITH
    department_summary AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT d.department_name, ds.average_salary
FROM
    department_summary ds
    INNER JOIN departments d ON ds.department_id = d.department_id;

WITH
    department_average AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT e.first_name, d.department_name, e.salary, da.average_salary
FROM
    employees e
    INNER JOIN department_average da ON e.department_id = da.department_id
    INNER JOIN departments d ON e.department_id = d.department_id
WHERE
    e.salary > da.average_salary;

-- Find employees earning above the company average
WITH
    company_average AS (
        SELECT AVG(salary) AS average_salary
        FROM employees
    )
SELECT first_name, salary
FROM employees
WHERE
    salary > (
        SELECT average_salary
        FROM company_average
    );

-- Show the maximum salary beside every employee.
WITH
    max_salary AS (
        SELECT MAX(salary) AS company_max_salary
        FROM employees
    )
SELECT
    first_name,
    salary,
    company_max_salary
FROM employees, max_salary;

/* Create a CTE showing: Department ID Employee count Average salary */
WITH
    department_summary AS (
        SELECT
            department_id,
            COUNT(*) AS employee_count,
            AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT *
FROM department_summary;

/* 
Join the CTE with the departments table.
Display:
Department name
Employee count
Average salary
*/
WITH
    department_summary AS (
        SELECT
            department_id,
            COUNT(*) AS employee_count,
            AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT d.department_name, ds.employee_count, ds.average_salary
FROM
    department_summary ds
    INNER JOIN departments d ON ds.department_id = d.department_id;

/* 
Create two CTEs:
First:
Department averages.
Second:
Departments with average salary above 40,000. 
*/
WITH
    department_summary AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    ),
    high_salary_departments AS (
        SELECT *
        FROM department_summary
        WHERE
            average_salary > 40000
    )
SELECT d.department_name, hsd.average_salary
FROM
    high_salary_departments hsd
    INNER JOIN department_summary ds ON ds.department_id = hsd.department_id
    INNER JOIN departments d ON ds.department_id = d.department_id;

-- Find employees earning above their department average.
WITH
    department_average AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT e.first_name, d.department_name, e.salary, da.average_salary
FROM
    employees e
    INNER JOIN department_average da ON e.department_id = da.department_id
    INNER JOIN departments d ON e.department_id = d.department_id
WHERE
    e.salary > da.average_salary;

-- Find the department with the highest average salary.
WITH
    department_average AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT d.department_name, da.average_salary
FROM
    department_average da
    INNER JOIN departments d ON da.department_id = d.department_id
WHERE
    da.average_salary = (
        SELECT MAX(average_salary)
        FROM department_average
    );

/* 
Create a salary report containing:
Department
Employee count
Total salary
Average salary
Highest salary
Lowest salary
Use a CTE.
*/
WITH
    department_salary_report AS (
        SELECT
            department_id,
            COUNT(*) AS employee_count,
            SUM(salary) AS total_salary,
            AVG(salary) AS average_salary,
            MAX(salary) AS highest_salary,
            MIN(salary) AS lowest_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT d.department_name, dsr.employee_count, dsr.total_salary, dsr.average_salary, dsr.highest_salary, dsr.lowest_salary
FROM
    department_salary_report dsr
    INNER JOIN departments d ON dsr.department_id = d.department_id;

/* 
Create a customer spending report using:
customers
orders
Return:
Customer
Total spending 
*/
WITH
    customer_spending AS (
        SELECT c.customer_id, c.customer_name, SUM(o.amount) AS total_spending
        FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id,
            c.customer_name
    )
SELECT cs.customer_name, cs.total_spending
FROM customer_spending cs;

-- Find customers whose spending is above the average customer spending. Use a CTE.
WITH
    customer_spending AS (
        SELECT c.customer_id, c.customer_name, SUM(o.amount) AS total_spending
        FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id,
            c.customer_name
    )
SELECT cs.customer_name, cs.total_spending
FROM customer_spending cs
WHERE
    cs.total_spending > (
        SELECT AVG(total_spending)
        FROM customer_spending
    );

-- Which employee earns the largest percentage above their department average ?
WITH
    department_average AS (
        SELECT department_id, AVG(salary) AS average_salary
        FROM employees
        GROUP BY
            department_id
    ),
    employee_percentage_above_average AS (
        SELECT
            e.employee_id,
            e.first_name,
            e.salary,
            da.average_salary,
            (
                (e.salary - da.average_salary) / da.average_salary
            ) * 100 AS percentage_above_average
        FROM
            employees e
            INNER JOIN department_average da ON e.department_id = da.department_id
    )
SELECT *
FROM
    employee_percentage_above_average
ORDER BY percentage_above_average DESC
LIMIT 1;

-- Which department contributes the largest percentage of the company's payroll?
WITH
    company_payroll AS (
        SELECT SUM(salary) AS total_payroll
        FROM employees
    ),
    department_payroll AS (
        SELECT
            department_id,
            SUM(salary) AS department_total_salary
        FROM employees
        GROUP BY
            department_id
    )
SELECT d.department_name, dp.department_total_salary, (
        dp.department_total_salary / cp.total_payroll
    ) * 100 AS percentage_of_company
FROM
    department_payroll dp
    CROSS JOIN company_payroll cp
    INNER JOIN departments d ON dp.department_id = d.department_id
ORDER BY percentage_of_company DESC
LIMIT 1;

-- Which customer has spent more than twice the average customer spending ?
WITH
    customer_spending AS (
        SELECT c.customer_id, c.customer_name, SUM(o.amount) AS total_spending
        FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id,
            c.customer_name
    )
SELECT *
FROM customer_spending
WHERE
    total_spending > 2 * (
        SELECT AVG(total_spending)
        FROM customer_spending
    );

-- Which departments have fewer employees than the company average per department?
WITH
    department_employee_count AS (
        SELECT department_id, COUNT(*) AS employee_count
        FROM employees
        GROUP BY
            department_id
    ),
    company_average AS (
        SELECT AVG(employee_count) AS employee_count_average
        FROM department_employee_count
    )
SELECT d.department_name, dec.employee_count
FROM
    department_employee_count dec
    CROSS JOIN company_average ca
    INNER JOIN departments d ON dec.department_id = d.department_id
WHERE
    dec.employee_count < ca.employee_count_average;