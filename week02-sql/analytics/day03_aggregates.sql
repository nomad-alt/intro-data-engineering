SELECT COUNT(*) AS employee_count FROM employees;

SELECT
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees;

-- Count employees in each department.
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY
    department_id;

-- Calculate the average salary for each department.
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY
    department_id;

-- Calculate total payroll for each department.
SELECT department_id, SUM(salary) AS total_payroll
FROM employees
GROUP BY
    department_id;

-- Show departments with more than one employee.
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY
    department_id
HAVING
    COUNT(*) > 1;

-- Show departments whose average salary is greater than: 40000
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY
    department_id
HAVING
    AVG(salary) > 40000;

-- Sort departments by total payroll. Highest first.
SELECT department_id, SUM(salary) AS total_payroll
FROM employees
GROUP BY
    department_id
ORDER BY total_payroll DESC;

-- Show the department with the highest average salary.
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY
    department_id
ORDER BY average_salary DESC
LIMIT 1;

-- Create a report showing: Department ID Employee count Total salary Average salary Minimum salary Maximum salary
SELECT
    department_id,
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees
GROUP BY
    department_id
ORDER BY department_id;

-- What percentage of the company's payroll belongs to each department?
SELECT
    department_id,
    SUM(salary) AS total_salary,
    (
        SUM(salary) / (
            SELECT SUM(salary)
            FROM employees
        )
    ) * 100 AS payroll_percentage
FROM employees
GROUP BY
    department_id
ORDER BY payroll_percentage DESC;

-- Which department has the widest salary range (MAX - MIN) ?
SELECT department_id, MAX(salary) - MIN(salary) AS salary_range
FROM employees
GROUP BY
    department_id
ORDER BY salary_range DESC;

-- Which department has the lowest average salary ?
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY
    department_id
ORDER BY average_salary ASC
LIMIT 1;

-- Which departments have exactly two employees ?
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY
    department_id
HAVING
    COUNT(*) = 2;