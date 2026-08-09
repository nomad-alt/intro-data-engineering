# Business Questions for SQL Reports

## Report 1 - Employee Overview

### Business Question
Which employees belong to each department, and how do they compare by salary within their department?

### SQL Techniques
JOIN
ROW_NUMBER()
PARTITION BY
ORDER BY

### Why This Matters
Managers can review team composition and see how salary levels are distributed inside each department.

## Report 2 - Department Summary

### Business Question
Which departments have the highest payroll, the most employees, and the widest salary spread?

### SQL Techniques
JOIN
GROUP BY
COUNT()
SUM()
AVG()
MAX()
MIN()
ORDER BY

### Why This Matters
This helps leadership understand staffing levels and payroll concentration across the company.

## Report 3 - High Earners

### Business Question
Which employees earn above the company average salary?

### SQL Techniques
JOIN
WHERE
Subquery
AVG()
ORDER BY

### Why This Matters
HR and management can identify strong performers or salary outliers that may require review.

## Report 4 - Department Leaders

### Business Question
Who is the top-paid employee in each department?

### SQL Techniques
JOIN
ROW_NUMBER()
PARTITION BY
WHERE
ORDER BY

### Why This Matters
This supports leadership reviews and helps identify department heads or key contributors.

## Report 5 - Customer Spending

### Business Question
How much has each customer spent in total?

### SQL Techniques
LEFT JOIN
GROUP BY
COUNT()
SUM()
COALESCE()
ORDER BY

### Why This Matters
This helps the business understand customer engagement and revenue contribution by client.

## Report 6 - Top Customers

### Business Question
Which customers are generating the highest total spending?

### SQL Techniques
LEFT JOIN
GROUP BY
SUM()
ORDER BY
LIMIT

### Why This Matters
Sales and account teams can quickly identify the most valuable customers.

## Report 7 - Customer Ranking

### Business Question
How do customers rank by total spending?

### SQL Techniques
GROUP BY
SUM()
DENSE_RANK()
OVER()
ORDER BY

### Why This Matters
Ranking customers makes it easier to compare their value and prioritize relationship management.

## Report 8 - Running Revenue

### Business Question
How does total revenue accumulate over time as orders are listed?

### SQL Techniques
SUM()
OVER()
ORDER BY

### Why This Matters
This gives a simple view of revenue growth and helps track cumulative sales performance.

## Report 9 - Sales Analysis

### Business Question
How does each order compare with the one before it?

### SQL Techniques
LAG()
OVER()
ORDER BY

### Why This Matters
This helps analysts spot unusual changes in sales activity and monitor order trends.

## Report 10 - Executive Dashboard

### Business Question
What is the overall snapshot of the company’s people and sales performance?

### SQL Techniques
CTE
COUNT()
SUM()
AVG()
MAX()
MIN()
CROSS JOIN

### Why This Matters
Executives can use this single summary to quickly assess workforce size, payroll, customers, and revenue.

## Report 11 - Newest Employees

### Business Question
Who are the most recently hired employees?

### SQL Techniques
ORDER BY
LIMIT

### Why This Matters
HR can use this report to track recent hiring activity and onboarding progress.

## Report 12 - Department Payroll Percentage

### Business Question
What percentage of the company payroll belongs to each department?

### SQL Techniques
CTE
JOIN
SUM()
NULLIF()
ROUND()

### Why This Matters
This report helps leadership understand how payroll costs are distributed across departments.

## Report 13 - Salary Distribution

### Business Question
How many employees fall into each salary band?

### SQL Techniques
CASE
WHEN
GROUP BY
COUNT()

### Why This Matters
This supports workforce planning and helps identify whether the company has a balanced salary structure.

## Report 14 - Customer Lifetime Value

### Business Question
Which customers have the highest total spending and how do they rank?

### SQL Techniques
LEFT JOIN
GROUP BY
SUM()
RANK()
OVER()
ORDER BY

### Why This Matters
This helps the business prioritize high-value customers and understand long-term revenue potential.
