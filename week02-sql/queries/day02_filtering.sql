SELECT * FROM employees WHERE salary > 40000;

SELECT * FROM employees WHERE hire_date > '2021-12-31';

SELECT *
FROM employees
WHERE
    department_id = 1
    OR department_id = 3;

SELECT * FROM employees WHERE department_id IN (1, 3);

SELECT * FROM employees WHERE salary BETWEEN 30000 AND 45000;

SELECT first_name FROM employees WHERE first_name LIKE 'S%';

SELECT first_name, salary FROM employees ORDER BY salary DESC;

SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 2;

INSERT INTO
    employees (
        employee_id,
        first_name,
        last_name,
        department_id,
        salary,
        hire_date
    )
VALUES (
        7,
        'Michael',
        'Scott',
        2,
        55000,
        '2021-03-15'
    );

UPDATE employees
SET
    salary = employees.salary * 1.10
WHERE
    employee_id = 7;

DELETE FROM employees WHERE employee_id = 7;

SELECT * FROM employees WHERE salary >= 39000;

-- Which employees work outside the Sales department?
SELECT * FROM employees WHERE department_id != 2;

SELECT * FROM employees ORDER BY hire_date DESC LIMIT 2;

SELECT * FROM employees WHERE salary < 35000;