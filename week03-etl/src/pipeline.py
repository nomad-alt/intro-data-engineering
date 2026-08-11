from pathlib import Path

try:
    from src.extract import extract_csv
except ImportError:  # pragma: no cover - fallback for direct script execution
    from extract import extract_csv

RAW_PATH = Path("data/raw/sales.csv")


def main() -> None:
    df = extract_csv(RAW_PATH)

    print(df.head())
    print()
    print(df.info())
    print()
    print(df.isna().sum())


if __name__ == "__main__":
    main()
