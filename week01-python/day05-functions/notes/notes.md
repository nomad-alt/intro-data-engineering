# Day 5 Notes — Python Functions

## Why Functions Are Useful

Functions let you package reusable logic under a single name. Instead of repeating the same code multiple times, you write it once in a function and call it whenever needed. This reduces mistakes, makes changes easier, and keeps code organized.

## Parameters vs Arguments

A **parameter** is a variable listed in the function definition. An **argument** is the actual value passed when calling the function.

```python
def greet(name):  # name is a parameter
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an argument
```

## Return Values

Functions use `return` to send a value back to the caller. A function can return early on error or return different values based on conditions.

```python
def double(x):
    return x * 2

result = double(5)  # result is 10
```

## Type Hints

Type hints document what types a function expects and returns. They help catch mistakes before runtime and make code clearer.

```python
def increase_salary(salary: float, percentage: float) -> float:
    return salary * (1 + percentage / 100)
```

## Variable Scope

A variable defined inside a function only exists within that function (local scope). Variables defined outside all functions are global.

```python
global_var = 100  # global scope

def my_function():
    local_var = 50  # local scope, only exists in this function
    print(local_var)  # 50

print(global_var)  # 100
# print(local_var)  # Error — local_var doesn't exist outside the function
```

## Default Arguments

Functions can have default parameter values. If no argument is provided, the default is used.

```python
def greet(name="World"):
    print(f"Hello, {name}")

greet()  # prints "Hello, World"
greet("Alice")  # prints "Hello, Alice"
```

## Keyword Arguments

Arguments can be passed by name instead of position. This makes code clearer when a function has many parameters.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments
describe_person("Alice", 30, "Sydney")

# Keyword arguments
describe_person(name="Bob", age=25, city="Stockholm")

# Mixed
describe_person("Charlie", city="Oslo", age=35)
```

## Docstrings

A docstring is a multi-line string that documents what a function does. It appears as the first line in the function body and helps users understand the function's purpose.

```python
def calculate_average(values: list[float]) -> float:
    """Calculate and return the average of a list of numbers."""
    return sum(values) / len(values) if values else 0.0
```

## Small Functions

Small, focused functions are easier to understand, test, and reuse. If a function gets long or does too many things, consider splitting it into smaller functions.

## Pure Functions

A **pure function** returns a value based only on its inputs and does not change external state (no side effects). Pure functions are:

- Easier to test (same input always produces same output)
- Safer to use (no hidden surprises)
- Easier to reason about

```python
# Pure function — only depends on inputs, no side effects
def calculate_new_salary(salary: float, raise_percent: float) -> float:
    return salary * (1 + raise_percent / 100)

# Impure function — modifies external state
global_employees = []

def add_employee_impure(name):
    global_employees.append(name)  # side effect: modifying global state
```

## How Functions Make Code Better

### Reusable

Write logic once, use it many times. This saves time and reduces errors.

```python
def validate_email(email: str) -> bool:
    return "@" in email

# Use the same function everywhere emails are validated
is_valid_1 = validate_email("alice@example.com")
is_valid_2 = validate_email("bob@example.com")
```

### Testable

Functions isolate logic so you can test it independently without running the entire program. Unit tests verify that each function works correctly.

```python
def test_validate_email():
    assert validate_email("alice@example.com") == True
    assert validate_email("invalid") == False
```

### Easier to Maintain

When logic is in a function, you change it in one place and all calls benefit. If logic was duplicated across the code, you'd have to update many places and risk inconsistencies.
