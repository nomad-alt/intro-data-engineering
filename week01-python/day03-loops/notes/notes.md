# Day 3 Notes — Python Loops

## For Loops

A `for` loop processes each item in an iterable.

```python
for file_name in file_names:
    print(file_name)
```

## Range

range() generates a sequence of integers.
```python
for batch_number in range(1, 6):
    print(batch_number)
```

## Enumerate

enumerate() provides an item and its position.

```python
for position, column in enumerate(columns, start=1):
    print(position, column)
```

## While Loops

A while loop runs while a condition remains true.

## Continue

continue skips the current iteration.

## Break

break stops the entire loop.

## Accumulators

An accumulator stores a running value.

```python
total = 0

for value in values:
    total += value
```

## Data Engineering Relevance

Loops are used to:

- Process records
- Iterate through files
- Validate rows
- Process API pages
- Create batches
- Count valid and invalid records
- Retry failed operations

## Common Mistakes

- Creating infinite while loops
- Modifying a list while iterating through it
- Using unclear loop variable names
- Forgetting to initialize accumulators
- Dividing by zero when calculating averages
- Using nested loops unnecessarily