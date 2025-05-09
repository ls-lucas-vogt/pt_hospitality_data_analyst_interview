from src.process_transactions import process_transactions

if __name__ == "__main__":
    input_path = "enter_your_input_data_path_here"
    output_path = "enter_you_summary_path_here"
    process_transactions(input_path, output_path)
    print("✅ Processing complete. Summary saved.")
