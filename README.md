# P&T Hospitality - Data Analyst Interview
---

## Python Test
Welcome to the Python test for the Data Analyst position at P&T Hospitality. This test is designed to assess your 
Python programming skills and your ability to work with data.

---

## 🧪 Objectives

You will demonstrate your ability to:
- Use Git and virtual environments
- Understand Python project structure
- Read and manipulate a dataset
- Organize code and write simple tests
- Use best practices in package management

---

## 📦 Setup Instructions

1. Clone this repository. Example:
   ```bash
   git clone https://github.com/ls-lucas-vogt/pt_hospitality_data_analyst_interview.git
   cd pt_hospitality_data_analyst_interview
   ```
   
2. Create a new branch for your changes.
   
3. Create and activate a virtual environment. Example:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages from `requirements.txt` file.

## 📁 Initial Project Structure
```
pt_hospitality_data_analyst_interview/
├── data/
│   └── sample.csv
├── src/
│   └── process_transactions.py
├── tests/
│   └── test_processor.py
├── main.py
├── requirements.txt
├── .gitignore
├── .pytest.ini
├── setup.cfg
└── README.md
```

## 📊 Exercise

1. You are given a dataset containing transaction data for a hospitality business. Your task is to process this data and 
generate a summary report using the `src/process_transactions.py` file. The details of the instructions and dataset are outlined
in the file. 

2. Once you are done, you will be expected to create at least one test in the `tests/test_processor.py` file to test 
your newly implemented function.

3. The next step will be to update the requirements.txt file before committing and pushing your changes to the remote.

## 🌟 Impress Us!
If you have extra time and want to show off your tooling or best practices, feel free to:
- Format your code with black 
- Lint your code with flake8 
- Run tests using pytest

Create a Makefile allowing you to run the following commands:
``` bash
make test     # Runs tests
make format   # Applies black formatting
make lint     # Lints with flake8
make all      # Runs format, lint, and test
```
