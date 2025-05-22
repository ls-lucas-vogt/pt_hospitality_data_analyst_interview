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


# def process_transactions(input_csv, output_csv):
#     pass


import pandas as pd


# print("test")
def process_transactions(input_csv, output_csv):
    sample_df = pd.read_csv(input_csv, parse_dates=['datetime'])
    sample_df["total_price"] = sample_df["quantity"] * sample_df["unit_price"]
    sample_df["is_high_value"] = sample_df["total_price"] > 100
    agg_df = pd.dataFrame()
    agg_df = sample_df.groupby("location_id").agg(
        total_sales = ("total_price", "sum"),
        high_values = ("is_high_value", "sum")
    )
    print(agg_df)
    output_csv = print(sample_df.head())
    return output_csv
    pass

inputcsv = "../data/sample.csv"
outputcsv = "../data/output.csv"
process_transactions(inputcsv, outputcsv)
