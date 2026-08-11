import logging
from pathlib import Path

try:
    from src.extract import extract_csv
    from src.load import load_parquet
    from src.transform import transform_sales
except ImportError:  # pragma: no cover - fallback for direct script execution
    from extract import extract_csv
    from load import load_parquet
    from transform import transform_sales

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

RAW_PATH = Path("data/raw/sales.csv")
OUTPUT_PATH = Path("data/processed/sales_clean.parquet")


def main() -> None:
    logger.info("Starting sales ETL pipeline")

    raw_df = extract_csv(RAW_PATH)
    logger.info("Extracted %d rows", len(raw_df))

    clean_df = transform_sales(raw_df)
    logger.info("Transformation produced %d rows", len(clean_df))

    load_parquet(clean_df, OUTPUT_PATH)
    logger.info("Loaded cleaned data to %s", OUTPUT_PATH)


if __name__ == "__main__":
    main()
