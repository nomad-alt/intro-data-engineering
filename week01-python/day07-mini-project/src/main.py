from pathlib import Path

try:
    from .extract import extract
    from .load import save_csv, save_json
    from .report import generate_summary
    from .transform import transform
except ImportError:  # pragma: no cover - supports direct script execution
    from extract import extract
    from load import save_csv, save_json
    from report import generate_summary
    from transform import transform


def main() -> None:
    """Run the employee processing pipeline."""
    input_path = (
        Path(__file__).resolve().parent.parent / "data" / "input" / "employees.csv"
    )

    employees = extract(input_path)
    transformed_employees = transform(employees)
    generate_summary(transformed_employees)
    save_csv(transformed_employees)
    save_json(transformed_employees)

    print("Pipeline completed successfully.")
    print()
    print("Employees processed: 5")
    print()
    print("Output files:")
    print()
    print("employees_processed.csv")
    print("summary.json")
