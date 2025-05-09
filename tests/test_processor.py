from src.process_transactions import process_transactions


def test_process_transactions(tmp_path):
    input_path = "data/sample.csv"
    output_path = tmp_path / "summary.csv"

    process_transactions(input_path, output_path)  # Your output file will be available at output_path

    # Read the output file into a dataframe
    df = 'placeholder'

    # Implement your tests here
    # Some ideas:
    # - Check if the file exists
    # - Check if the dataframe is not empty
    # - Check if the columns are as expected
    # - Check if the data types are as expected
    # - Check if the calculations are correct
    # - Feel free to come up with other ideas but not necessary.

    assert False, "This test is a placeholder. Please implement your tests."
