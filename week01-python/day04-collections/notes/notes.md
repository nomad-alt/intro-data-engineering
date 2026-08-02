# Day 4 Notes — Python Collections

## Lists

Lists are ordered, mutable collections that allow duplicates.

```python
datasets = ["customers", "orders", "products"]
```

Common methods:

- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`

## Tuples

Tuples are ordered collections that should not be modified.

```python
database_address = ("localhost", 5432)
```

## Sets

Sets contain unique values and support fast membership tests.

```python
unique_ids = {101, 102, 103}
```

Useful operations:

- Union: `|`
- Intersection: `&`
- Difference: `-`
- Symmetric difference: `^`

## Dictionaries

Dictionaries store key-value pairs.

```python
customer = {
    "customer_id": 101,
    "name": "Amina",
}
```

Use `.get()` when a key might not exist.

## Nested Collections

A list of dictionaries commonly represents rows or JSON records.

## Comprehensions

A comprehension creates a collection using a concise expression.

```python
valid_ids = [
    record["id"]
    for record in records
    if record["is_valid"]
]
```

## Data Engineering Relevance

Collections are used to represent:

- Records
- JSON objects
- API responses
- Column names
- Configuration values
- Validation results
- Unique identifiers
- Lookup tables

## Common Mistakes

- Accessing a missing dictionary key with square brackets
- Accessing an invalid list index
- Modifying a list while iterating through it
- Assuming sets preserve meaningful order
- Using mutable lists when fixed tuples are more suitable
- Writing overly complex comprehensions
