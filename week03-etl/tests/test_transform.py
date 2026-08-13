import pandas as pd
import pytest
from src.transform import transform_sales, validate_sales


def test_validate_sales_raises_for_missing_required_columns() -> None:
    input_df = pd.DataFrame(
        {
            "customer_name": ["Alice"],
            "quantity": [1],
        }
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_sales(input_df)


def test_transform_sales_removes_invalid_quantity() -> None:
    input_df = pd.DataFrame(
        {
            "order_id": [1, 2],
            "customer_name": ["Alice", "Bob"],
            "product": ["Laptop", "Mouse"],
            "quantity": [1, 0],
            "unit_price": [1000.0, 50.0],
            "country": ["Sweden", "Norway"],
        }
    )

    result = transform_sales(input_df)

    assert len(result) == 1


def test_transform_sales_calculates_total_amount() -> None:
    input_df = pd.DataFrame(
        {
            "order_id": [1],
            "customer_name": ["Alice"],
            "product": ["Laptop"],
            "quantity": [2],
            "unit_price": [100.0],
            "country": ["Sweden"],
        }
    )

    result = transform_sales(input_df)

    assert result.iloc[0]["total_amount"] == 200.0


def test_transform_sales_normalizes_country() -> None:
    input_df = pd.DataFrame(
        {
            "order_id": [1],
            "customer_name": ["Alice"],
            "product": ["Laptop"],
            "quantity": [1],
            "unit_price": [100.0],
            "country": ["Sweden"],
        }
    )

    result = transform_sales(input_df)

    assert result.iloc[0]["country"] == "SWEDEN"
