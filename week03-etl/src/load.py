from pathlib import Path

import pandas as pd


def load_parquet(df: pd.DataFrame, output_path: Path) -> None:
    """Write a DataFrame to a Parquet file."""
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_parquet(
        output_path,
        index=False,
    )
