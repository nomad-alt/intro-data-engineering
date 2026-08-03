# Day 5 — Python Functions

## Objective

Learn how to write reusable, testable functions and understand how they improve code quality and maintainability.

## Topics Covered

- Function definition and calls
- Parameters and arguments
- Return values
- Type hints
- Default and keyword arguments
- Docstrings
- Variable scope
- Pure functions (functions without side effects)
- Composition (combining functions to build larger workflows)

## Files

- `src/data_transformer.py` — multi-step transformation pipeline
- `tests/test_data_transformer.py` — unit tests for individual functions
- `notes/notes.md` — personal learning notes

## Running the Examples

From the repository root:

```bash
python week01-python/day05-functions/src/data_transformer.py
```

## Running Tests

From the repository root:

```bash
pytest week01-python/day05-functions/tests -v
```

## Code Quality

```bash
ruff check week01-python/day05-functions
ruff format --check week01-python/day05-functions
```

Format code automatically:

```bash
ruff format week01-python/day05-functions
```

## Data Engineering Relevance

ETL pipelines are typically composed of **many small transformation functions** rather than one large script. Each function handles one step:

- **Extract**: read data from a source
- **Transform**: clean, validate, or restructure data
- **Load**: write to a destination

Breaking a pipeline into small functions makes it easier to:

- Test each step independently
- Reuse transformations across different pipelines
- Debug issues (you know exactly which step failed)
- Maintain and modify the pipeline over time

For example, the `data_transformer.py` file demonstrates how a salary transformation workflow is built from small, testable functions:

1. `increase_salary()` — applies a percentage increase
2. `transform_employee()` — processes one record
3. `transform_employees()` — processes many records
4. `average_salary()` and `highest_salary()` — compute summaries
5. `print_summary()` — format and display results

This modular design is the foundation of production data systems at all scales.
