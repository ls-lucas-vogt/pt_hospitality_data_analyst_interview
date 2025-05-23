import pandas as pd
from src.process_transactions import process_transactions
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_process_transactions(tmp_path):
    input_path = "data/sample.csv"
    output_path = tmp_path / "summary.csv"

    process_transactions(input_path, output_path)

    # Check that the output file was created
    assert output_path.exists()

    # Read the output file
    df = pd.read_csv(output_path)

    # Check that it's not empty
    assert not df.empty

    # Check that required columns exist
    expected_cols = {"location_id", "total_price", "high_value_percentage"}
    assert expected_cols.issubset(df.columns)

    # Check data types
    assert df["location_id"].dtype == object
    assert pd.api.types.is_numeric_dtype(df["total_price"])
    assert pd.api.types.is_float_dtype(df["high_value_percentage"])

    # Check value ranges
    assert (df["high_value_percentage"] >= 0).all()
    assert (df["high_value_percentage"] <= 1).all()

    # Optional: basic sanity check
    assert (df["total_price"] > 0).all()
