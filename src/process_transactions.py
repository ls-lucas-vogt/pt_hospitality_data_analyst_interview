# The task is to implement a function that processes transaction data from a CSV file.

# The function should read the data, perform some calculations, and save the results to a new CSV file.

# The function should:
#   - Read the input CSV file into a DataFrame. Columns include:
#       - transaction_id
#       - datetime
#       - location_id
#       - product_name
#       - category
#       - quantity
#       - unit_price
#       - payment_method
#   - Add a new total_price (float) column (quantity * unit price).
#   - Add a new is_high_value column (boolean) indicating whether the total_price is high value (total_price > 100).
#   - Group the data by location_id:
#       - SUM total_price
#       - PERCENTAGE OF TOTAL transactions with is_high_value = True
#   - The resulting data should have three columns named as follows:
#       - location_id
#       - total_price (sum of total_price for each location_id)
#       - high_value_percentage (percentage of transactions with is_high_value = True for each location_id)
#   - Save the resulting DataFrame to a new CSV file in data/summary.csv (keep in mind the script runs from main).

# Bonus: The function should also handle null/missing values.

import pandas as pd
from src.process_transactions import process_transactions


def process_transactions(input_csv, output_csv):
    # load the data
    df = pd.read_csv(input_csv)

    # handle missing values
    df = df.dropna(subset=["location_id", "quantity", "unit_price"])

    # calculate total price

    df["total_price"] = df["quantity"] * df["unit_price"]

    # flag high value transactions

    threshold = 100
    df["is_high_value"] = df["total_price"] > threshold

    # Group by location_id and calculate metrics

    summary = (
        df.groupby("location_id")
        .agg(
            total_price=("total_price", "sum"),
            high_value_count=("is_high_value", "sum"),
            total_count=("is_high_value", "count"),
        )
        .reset_index()
    )

    # calculate high value transaction percentage %

    summary["high_value_percentage"] = round(
        (summary["high_value_count"] / summary["total_count"])
    )

    # select and rename the required columns

    summary = summary[["location_id", "total_price", "high_value_percentage"]]

    # save the summary report

    summary.to_csv(output_csv, index=False)


process_transactions("../data/sample.csv", "../data/summary.csv")
