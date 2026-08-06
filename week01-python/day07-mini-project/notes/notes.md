# Notes

- ETL: Extract, Transform, Load is a common data workflow for reading raw data, processing it, and writing results.
- CSV: Comma-separated values are used for input and output data storage in tabular form.
- JSON: JavaScript Object Notation is used for structured output and summaries.
- pathlib: The `pathlib` module is used to build file paths in a clear, platform-independent way.
- modules: The code is organized into separate modules for extraction, transformation, reporting, loading, and the pipeline entrypoint.
- functions: Small, focused functions are used for single responsibilities like `extract`, `transform`, `generate_summary`, `save_csv`, and `save_json`.
- testing: Unit tests verify each pipeline stage and help ensure behavior remains correct.
- clean architecture: The project keeps extraction, transformation, reporting, and loading separate so each part is easy to understand and maintain.
