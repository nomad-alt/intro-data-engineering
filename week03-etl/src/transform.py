import pandas as pd

REQUIRED_COLUMNS = {
    "order_id",
    "customer_name",
    "product",
    "quantity",
    "unit_price",
    "country",
}


def validate_sales(df: pd.DataFrame) -> None:
    """Validate that the sales DataFrame contains all required fields."""
    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df.empty:
        raise ValueError("Sales data is empty.")

    numeric_columns = {"order_id", "quantity", "unit_price"}
    for column in sorted(numeric_columns):
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"Column '{column}' must be numeric")

    if (df["unit_price"] <= 0).any():
        raise ValueError("Column 'unit_price' contains invalid values")


def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw sales data."""
    result = df.copy()

    for column in ["order_id", "quantity", "unit_price"]:
        result[column] = pd.to_numeric(result[column], errors="raise")

    validate_sales(result)

    result = result.dropna(subset=["customer_name", "unit_price"])
    result = result[result["quantity"] > 0]
    result["total_amount"] = result["quantity"] * result["unit_price"]
    result["country"] = result["country"].str.upper()

    return result
