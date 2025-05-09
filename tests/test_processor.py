import pandas as pd
from src.processor import process_transactions


def test_process_transactions(tmp_path):
    input_path = "data/sample.csv"
    output_path = tmp_path / "summary.csv"

    process_transactions(input_path, output_path)

    # Load result and check if file was created and not empty
    df = pd.read_csv(output_path)
    assert not df.empty
