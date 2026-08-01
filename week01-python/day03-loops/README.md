# Day 3 — Python Loops

## Objective

Learn how to repeat operations and process collections of data using Python
loops.

## Topics Covered

- `for` loops
- `while` loops
- `range()`
- `enumerate()`
- Dictionary iteration
- Accumulator patterns
- `break`
- `continue`
- Nested loops
- Basic record processing

## Files

- `src/loop_examples.py` — loop syntax and examples
- `src/exercises.py` — practical loop exercises
- `src/record_processor.py` — transaction-processing mini-project
- `tests/test_record_processor.py` — unit tests
- `notes.md` — personal learning notes

## Running the Examples

From the repository root:

```bash
python week01-python/day03-loops/src/loop_examples.py
python week01-python/day03-loops/src/exercises.py
python week01-python/day03-loops/src/record_processor.py
```

## Running Tests
```bash
pytest week01-python/day03-loops/tests -v
```

## Code Quality
```bash
ruff check week01-python/day03-loops
ruff format --check week01-python/day03-loops
```

## Data Engineering Relevance

Data pipelines frequently process multiple files, records, batches, and API
pages. Loops provide the basic mechanism for repeatedly applying validation
and transformation logic.

For larger datasets, row-by-row Python loops may be replaced with SQL, Polars,
Pandas, or Spark operations for better performance.


