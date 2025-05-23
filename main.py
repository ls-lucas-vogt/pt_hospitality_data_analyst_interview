from src.process_transactions import process_transactions

if __name__ == "__main__":
    input_path = "data/sample.csv"
    output_path = "data/summary.csv"
    process_transactions(input_path, output_path)
    print("Processing complete. Summary saved.")
