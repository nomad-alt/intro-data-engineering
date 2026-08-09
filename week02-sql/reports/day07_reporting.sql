-- Report 1: Employee Overview
SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS full_name,
    d.department_name AS department,
    e.salary,
    ROW_NUMBER() OVER (
        PARTITION BY
            e.department_id
        ORDER BY e.salary DESC
    ) AS salary_rank_within_department
FROM employees AS e
    JOIN departments AS d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC;

-- Report 2: Department Summary
SELECT
    d.department_name AS department,
    COUNT(e.employee_id) AS employee_count,
    SUM(e.salary) AS total_payroll,
    AVG(e.salary) AS average_salary,
    MAX(e.salary) AS highest_salary,
    MIN(e.salary) AS lowest_salary
FROM departments AS d
    LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY
    d.department_id,
    d.department_name
ORDER BY total_payroll DESC;

-- Report 3: High Earners
SELECT
    e.first_name || ' ' || e.last_name AS employee,
    d.department_name AS department,
    e.salary,
    (
        SELECT AVG(salary)
        FROM employees
    ) AS company_average
FROM employees AS e
    JOIN departments AS d ON e.department_id = d.department_id
WHERE
    e.salary > (
        SELECT AVG(salary)
        FROM employees
    )
ORDER BY e.salary DESC;

-- Report 4: Department Leaders
SELECT department, employee, salary
FROM (
        SELECT
            d.department_name AS department, e.first_name || ' ' || e.last_name AS employee, e.salary, ROW_NUMBER() OVER (
                PARTITION BY
                    e.department_id
                ORDER BY e.salary DESC
            ) AS salary_rank
        FROM employees AS e
            JOIN departments AS d ON e.department_id = d.department_id
    ) AS ranked_employees
WHERE
    salary_rank = 1
ORDER BY salary DESC;

-- Report 5: Customer Spending
SELECT
    c.customer_name AS customer,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_spending
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_spending DESC;

-- Report 6: Top Customers
SELECT
    c.customer_name AS customer,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_spending
FROM customers AS c
    LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_spending DESC
LIMIT 3;

-- Report 7: Customer Ranking
SELECT
    customer,
    total_orders,
    total_spending,
    DENSE_RANK() OVER (
        ORDER BY total_spending DESC
    ) AS spending_rank
FROM (
        SELECT
            c.customer_name AS customer, COUNT(o.order_id) AS total_orders, COALESCE(SUM(o.amount), 0) AS total_spending
        FROM customers AS c
            LEFT JOIN orders AS o ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id, c.customer_name
    ) AS customer_spending
ORDER BY total_spending DESC;

-- Report 8: Running Revenue
SELECT
    order_id,
    customer_id,
    amount,
    SUM(amount) OVER (
        ORDER BY order_id
    ) AS running_total_revenue
FROM orders
ORDER BY order_id;

-- Report 9: Sales Analysis
SELECT
    order_id,
    customer_id,
    amount,
    LAG(amount) OVER (
        ORDER BY order_id
    ) AS previous_order,
    amount - LAG(amount) OVER (
        ORDER BY order_id
    ) AS difference
FROM orders
ORDER BY order_id;

-- Report 10: Executive Dashboard
WITH
    employee_metrics AS (
        SELECT
            COUNT(*) AS total_employees,
            COALESCE(SUM(salary), 0) AS total_payroll,
            COALESCE(AVG(salary), 0) AS company_average_salary,
            MAX(salary) AS highest_salary,
            MIN(salary) AS lowest_salary
        FROM employees
    ),
    customer_metrics AS (
        SELECT COUNT(*) AS total_customers
        FROM customers
    ),
    order_metrics AS (
        SELECT COUNT(*) AS total_orders, COALESCE(SUM(amount), 0) AS total_revenue
        FROM orders
    )
SELECT em.total_employees, em.total_payroll, em.company_average_salary, em.highest_salary, em.lowest_salary, cm.total_customers, om.total_orders, om.total_revenue
FROM
    employee_metrics AS em
    CROSS JOIN customer_metrics AS cm
    CROSS JOIN order_metrics AS om;

-- Report 11: Newest Employees
SELECT
    employee_id,
    first_name,
    last_name,
    hire_date
FROM employees
ORDER BY hire_date DESC
LIMIT 5;

-- Report 12: Department Payroll Percentage
WITH department_payroll AS (
    SELECT
        d.department_name AS department,
        SUM(e.salary) AS department_payroll
    FROM departments AS d
        LEFT JOIN employees AS e ON d.department_id = e.department_id
    GROUP BY d.department_id, d.department_name
),
company_payroll AS (
    SELECT SUM(salary) AS total_payroll
    FROM employees
)
SELECT
    dp.department,
    dp.department_payroll,
    cp.total_payroll,
    ROUND((dp.department_payroll::numeric / NULLIF(cp.total_payroll, 0)) * 100, 2) AS payroll_percentage
FROM department_payroll AS dp
    CROSS JOIN company_payroll AS cp
ORDER BY dp.department_payroll DESC;

-- Report 13: Salary Distribution
SELECT
    CASE
        WHEN salary < 35000 THEN 'Junior'
        WHEN salary < 45000 THEN 'Mid'
        ELSE 'Senior'
    END AS salary_band,
    COUNT(*) AS employee_count
FROM employees
GROUP BY
    CASE
        WHEN salary < 35000 THEN 'Junior'
        WHEN salary < 45000 THEN 'Mid'
        ELSE 'Senior'
    END
ORDER BY employee_count DESC;

-- Report 14: Customer Lifetime Value
SELECT
    customer,
    total_spending,
    RANK() OVER (
        ORDER BY total_spending DESC
    ) AS customer_rank
FROM (
        SELECT c.customer_name AS customer, COALESCE(SUM(o.amount), 0) AS total_spending
        FROM customers AS c
            LEFT JOIN orders AS o ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id, c.customer_name
    ) AS customer_spending
ORDER BY total_spending DESC;