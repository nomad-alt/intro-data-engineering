import pandas as pd


def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw sales data."""
    result = df.copy()

    result = result.dropna(subset=["customer_name", "unit_price"])
    result = result[result["quantity"] > 0]
    result["total_amount"] = result["quantity"] * result["unit_price"]
    result["country"] = result["country"].str.upper()

    return result
