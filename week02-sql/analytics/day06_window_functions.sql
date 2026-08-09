SELECT
    first_name,
    salary,
    AVG(salary) OVER () AS company_average
FROM employees;

SELECT
    first_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY
                department_id
        ),
        2
    ) AS department_average
FROM employees;

SELECT first_name, salary, ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_number
FROM employees;

SELECT
    first_name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

SELECT
    first_name,
    department_id,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY
            department_id
        ORDER BY salary DESC
    ) AS department_rank
FROM employees;

SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;

SELECT
    order_date,
    amount,
    LAG(amount) OVER (
        ORDER BY order_date
    ) AS previous_order
FROM orders;

SELECT
    order_date,
    amount,
    LEAD(amount) OVER (
        ORDER BY order_date
    ) AS next_order
FROM orders;

SELECT
    first_name,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY
                department_id
        ),
        2
    ) AS department_average,
    salary - AVG(salary) OVER (
        PARTITION BY
            department_id
    ) AS salary_difference
FROM employees;

WITH
    ranked_employees AS (
        SELECT *, ROW_NUMBER() OVER (
                PARTITION BY
                    department_id
                ORDER BY salary DESC
            ) AS salary_rank
        FROM employees
    )
SELECT
    first_name,
    department_id,
    salary
FROM ranked_employees
WHERE
    salary_rank = 1;

-- Show: Employee Salary Company average salary
SELECT
    first_name,
    salary,
    AVG(salary) OVER () AS company_average
FROM employees;

-- Show: Employee Department Department average salary
SELECT
    first_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY
                department_id
        ),
        2
    ) AS department_average
FROM employees;

-- Rank employees by salary. Use: ROW_NUMBER()
SELECT first_name, salary, ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_number
FROM employees;

-- Rank employees by salary. Use: RANK()
SELECT
    first_name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

-- Rank employees by salary. Use: DENSE_RANK()
SELECT
    first_name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

-- Rank employees inside each department.
SELECT
    first_name,
    department_id,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY
            department_id
        ORDER BY salary DESC
    ) AS department_rank
FROM employees;

-- Calculate salary difference from department average.
SELECT
    first_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY
                department_id
        ),
        2
    ) AS department_average,
    salary - AVG(salary) OVER (
        PARTITION BY
            department_id
    ) AS salary_difference
FROM employees;

-- Show the highest-paid employee in every department.
WITH
    ranked_employees AS (
        SELECT *, ROW_NUMBER() OVER (
                PARTITION BY
                    department_id
                ORDER BY salary DESC
            ) AS salary_rank
        FROM employees
    )
SELECT
    first_name,
    department_id,
    salary
FROM ranked_employees
WHERE
    salary_rank = 1;

-- Calculate running total of order amounts.
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;

-- Use: LAG() Compare every order with the previous order.
SELECT
    order_date,
    amount,
    LAG(amount) OVER (
        ORDER BY order_date
    ) AS previous_order
FROM orders;

-- Which employee earns the highest percentage above the department average ?
SELECT
    first_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY
                department_id
        ),
        2
    ) AS department_average,
    salary - AVG(salary) OVER (
        PARTITION BY
            department_id
    ) AS salary_difference,
    (
        salary - AVG(salary) OVER (
            PARTITION BY
                department_id
        )
    ) / AVG(salary) OVER (
        PARTITION BY
            department_id
    ) * 100 AS percentage_above_average
FROM employees
ORDER BY percentage_above_average DESC
LIMIT 1;

-- Which department has the biggest salary gap between the highest and lowest  employee ?
WITH
    ranked_employees AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY
                    department_id
                ORDER BY salary DESC
            ) AS salary_rank_desc,
            ROW_NUMBER() OVER (
                PARTITION BY
                    department_id
                ORDER BY salary ASC
            ) AS salary_rank_asc
        FROM employees
    )
SELECT
    department_id,
    MAX(
        CASE
            WHEN salary_rank_desc = 1 THEN salary
        END
    ) AS highest_salary,
    MAX(
        CASE
            WHEN salary_rank_asc = 1 THEN salary
        END
    ) AS lowest_salary,
    MAX(
        CASE
            WHEN salary_rank_desc = 1 THEN salary
        END
    ) - MAX(
        CASE
            WHEN salary_rank_asc = 1 THEN salary
        END
    ) AS salary_gap
FROM ranked_employees
GROUP BY
    department_id
ORDER BY salary_gap DESC
LIMIT 1;

-- Which customer has the largest increase between consecutive orders?
WITH
    ranked_orders AS (
        SELECT *, LAG(amount) OVER (
                PARTITION BY
                    customer_id
                ORDER BY order_date
            ) AS previous_order
        FROM orders
    )
SELECT
    customer_id,
    order_date,
    amount,
    previous_order,
    amount - previous_order AS increase
FROM ranked_orders
WHERE
    previous_order IS NOT NULL
ORDER BY increase DESC
LIMIT 1;

-- Rank customers by total spending.
WITH
    customer_spending AS (
        SELECT customer_id, SUM(amount) AS total_spent
        FROM orders
        GROUP BY
            customer_id
    )
SELECT
    customer_id,
    total_spent,
    RANK() OVER (
        ORDER BY total_spent DESC
    ) AS spending_rank
FROM customer_spending;