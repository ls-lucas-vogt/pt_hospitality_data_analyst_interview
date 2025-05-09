import pandas as pd


def process_transactions(input_csv: str, output_csv: str) -> None:
    """Read, process, and summarize transaction data."""
    df = pd.read_csv(input_csv)

    # TODO: Implement your processing logic
    # - total_price
    # - is_high_value
    # - groupby summary
    # - handle edge cases (optional)

    # Example (commented out):
    # df['total_price'] = df['quantity'] * df['unit_price']
    # df['is_high_value'] = df['total_price'] > 100
    # summary = df.groupby('location_id').agg(...)

    # TODO: Save result
    # summary.to_csv(output_csv, index=False)
    pass
