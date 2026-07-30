# Day 1 Notes — Python Basics

## Variables

A variable is a name that refers to a value.

```python
customer_name = "Aisha"
monthly_salary_sek = 42_000
is_customer_active = True
```
### avoid
```python
x = "Aisha"
a = 42_000
value = True
```

### Underscores in numbers improve readability:
```python
annual_revenue_sek = 1_500_000
```

## Basic Data Types
```python
str: text
int: whole numbers
float: decimal numbers
bool: True or False
None: missing or unavailable value
```

## Type Inspection
```python
print(type(customer_name))
```

## Type Conversion
```python
row_count = int("1000")
temperature = float("21.5")
```

## Operators
### Arithmetic
```python
+
-
*
/
//
%
**
```
### Comparison
```python
==
!=
>
<
>=
<=
```
### Logical
```python
and
or
not
```

## Data Engineering Connection
Python types and operators are used to validate, clean, and transform data.

## Common Mistakes
Forgetting that input() returns a string
Using unclear variable names
Confusing = with ==
Dividing by zero
Converting invalid text into numbers

## What I Learned

I learned how Python stores common values, how to inspect and convert data
types, and how operators can be used to perform calculations and create
basic validation rules.

### Data Engineering Relevance
Data pipelines frequently receive values in the wrong type. For example, a
number from a CSV file may initially be represented as text. Understanding
types and conversions is therefore essential for cleaning and transforming
data reliably.

## Known Limitations
The BMI calculator does not yet validate invalid input or prevent impossible
values such as a negative weight.