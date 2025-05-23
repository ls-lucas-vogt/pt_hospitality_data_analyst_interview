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
import os

def process_transactions(input_csv, output_csv):

    try:    
        # read csv with date parsing
        sample_df = pd.read_csv(input_csv, parse_dates=["datetime"])
        
        # clean data: select only rows with a transaction id
        sample_df = sample_df.dropna(subset=["transaction_id"])

        # fill missing dimensions with values
        sample_df["product_name"] = sample_df["product_name"].fillna("Unknown")
        sample_df["category"] = sample_df["category"].fillna("Unknown")
        sample_df["payment_method"] = sample_df["payment_method"].fillna("Unknown")
        
        # 1) calculate total price
        sample_df["total_price"] = sample_df["quantity"] * sample_df["unit_price"]
        
        # 2) flag high value transactions
        sample_df["is_high_value"] = sample_df["total_price"] > 100
        
        # 3) goup by location_id 
        agg_df = sample_df.groupby("location_id").agg(
            total_price = ("total_price", "sum"),
            high_values = ("is_high_value", "sum"),
            total_transactions = ("is_high_value", "count")
        ).reset_index()
        
        # 4) calculate PERCENTAGE OF TOTAL transactions with 'is_high_value' = True
        agg_df["high_value_percentage"] = (
            agg_df["high_values"] / agg_df["total_transactions"] * 100
        ).round(2)
        
        # 5) select output columns
        output = agg_df[["location_id", "total_price", "high_value_percentage"]]
        
        # 6) sort by highest value percentage
        output = output.sort_values(by="high_value_percentage", ascending=False)

        print(output.head())
        
        # check if output folder name exists and save output to csv
        os.makedirs(os.path.dirname(output_csv), exist_ok = True)
        save_file = output.to_csv(output_csv, index = False)
        print("Summary output saved as summary_csv in folder 'data'")
        
        return save_file
    
    # error handling    
    except Exception as e: 
        print(f"Error: {e}")


if __name__ == "__main__":
    # either run python file from main
    inputcsv = "data/sample.csv"
    outputcsv = "data/summary.csv"
    
    # # Or run python file from src
    # inputcsv = "../data/sample.csv"
    # outputcsv = "../data/summary.csv"
    process_transactions(inputcsv, outputcsv)
