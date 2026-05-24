"""
The list of commands and their expected output is shown below:

$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20

JSON object for a single expense:
[
  {
    "id": 1,
    "date": "2026-05-24",
    "description": "Lunch",
    "amount": 20.0
  }
]
"""

# expense-tracker.py

# argparse is used for parsing command-line arguments
import argparse

# json is used for reading and writing expenses to a file
import json

# os is used for checking if the expenses file exists
import os

# datetime is used for handling dates of expenses
from datetime import datetime

EXPENSE_DIR = "data"
EXPENSE_FILE = os.path.join(EXPENSE_DIR, "expenses.json")

def initialize_storage():
    """Initialize the storage for expenses."""

    # Create data directory if it doesn't exist
    if not os.path.exists(EXPENSE_DIR):
        os.makedirs(EXPENSE_DIR)

    # Create expenses.json file if it doesn't exist
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w') as f:
            json.dump([], f)

