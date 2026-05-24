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


def load_expenses():
    """
    Load all stored expenses from the JSON file.

    Returns:
        list: A list containing all expense dictionaries.
    """

    with open(EXPENSE_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """
    Save all expenses to the JSON file.

    Args:
        expenses (list): The updated list of expense dictionaries.
    """

    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

"""
Functions for handling expenses will be defined here.
"""
def add_expense():
    return True

def delete_expense():
    return True

def update_expense():
    return True

def list_expenses():
    return []

def show_summary():
    return 0




def main():
    """
        Main function to handle command-line arguments and execute corresponding functions.
    """

    # Initialize storage for expenses
    initialize_storage()