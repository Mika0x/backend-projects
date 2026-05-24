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

    
def generate_expense_id(expenses):
    """
    Generate a unique ID for a new expense.

    Args:
        expenses (list): The current list of expenses.

    Returns:
        int: The generated unique ID.
    """
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1


"""
Functions for handling expenses will be defined here.
"""
def add_expense(description, amount):
    """
    Add a new expense to the expense list.

    Args:
        description (str): A short description of the expense.
        amount (float): The cost of the expense.
    """

    if amount <= 0:
        print("Amount must be greater than 0")
        return

    expenses = load_expenses()

    new_expense = {
        "id": generate_expense_id(expenses),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount,
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    print(f"Expense added successfully (ID: {new_expense['id']})")


def delete_expense(expense_id):
    """
    Delete an expense from the expense list

    Args:
        expense_id (int): The ID of the expense to delete.
    """
    expenses = load_expenses()

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("Expense ID not found")
        return

    save_expenses(updated_expenses)
    print("Expense deleted successfully")


def update_expense(expense_id, description=None, amount=None):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            if description is not None:
                expense["description"] = description
            if amount is not None:
                expense["amount"] = amount
            save_expenses(expenses)
            print("Expense updated successfully")
            return

    print("Expense ID not found")


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