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

def process_transactions(input_csv, output_csv):
    pass



def loading_cleaning_data(input_csv,output_csv):
    df_transaction=pd.read_csv('input_csv')
    df_transaction['total_price']=df_transaction['quantity']*df_transaction['unit_price']
    df_transaction['total_price'].astype(float)
    df_transaction['is_high_value']= df_transaction['total_price'].apply(lambda x: 'High' if x>100 else 'Low')
    df_transaction.groupby('location_id')['total_price'].sum()
    df_temp=df_transaction[df_transaction['is_high_value']=='High']
    