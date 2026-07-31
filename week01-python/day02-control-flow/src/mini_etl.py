sales = [120, 80, 300, 40, 250]


def filter_large_sales(sales: list[int], minimum: int) -> list[int]:
    """Filter sales greater than or equal to the minimum value."""
    return [sale for sale in sales if sale >= minimum]


large_sales = filter_large_sales(sales, 100)
print(f"Large sales: {large_sales}")
