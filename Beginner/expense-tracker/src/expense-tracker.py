# expense-tracker.py

# argparse is used for parsing command-line arguments
import argparse

# json is used for reading and writing expenses to a file
import json

# os is used for checking if the expenses file exists
import os

# datetime is used for handling dates of expenses
from datetime import datetime

# calendar is used for converting month number to month name
import calendar

# csv is used for exporting expenses stored in json format to a column separated value file
import csv

EXPENSE_DIR = "data"
EXPENSE_FILE = os.path.join(EXPENSE_DIR, "expenses.json")
BUDGET_FILE = os.path.join(EXPENSE_DIR, "budgets.json")
EXPORT_FILE = os.path.join(EXPENSE_DIR, "expenses.csv")

# DEFINE THE LIST OF CATEGORIES FOR EXPENSES
CATEGORIES = [
    "Food",
    "Transportation",
    "Bills",
    "Entertainment",
    "Shopping",
]

def initialize_storage():
    """Initialize the storage for expenses."""

    # Create data directory if it doesn't exist
    if not os.path.exists(EXPENSE_DIR):
        os.makedirs(EXPENSE_DIR)

    # Create expenses.json file if it doesn't exist
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w') as f:
            json.dump([], f)

    # Create budgets.json file if it doesn't exist
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'w') as f:
            json.dump([], f)


def load_expenses():
    """
    Load all stored expenses from the JSON file.

    Returns:
        list: A list containing all expense dictionaries.
    """

    with open(EXPENSE_FILE, "r") as file:
        return json.load(file)


def load_budgets():
    """
    Load all stored budgets for each month from the JSON file.

    Returns:
        list: A list containing all budget dictionaries.
    """

    with open(BUDGET_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """
    Save all expenses to the JSON file.

    Args:
        expenses (list): The updated list of expense dictionaries.
    """

    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def save_budgets(budgets):
    """
    Save all budgets to the JSON file.

    Args:
        budgets (list): The updated list of budget dictionaries.
    """

    with open(BUDGET_FILE, "w") as file:
        json.dump(budgets, file, indent=4)

    
def get_monthly_expense_total(month):
    expenses = load_expenses()
    current_year = datetime.now().year
    total = 0

    for expense in expenses:
        expense_date = datetime.strptime(
            expense["date"],
            "%Y-%m-%d"
        )

        if (
            expense_date.month == month
            and expense_date.year == current_year
        ):
            total += expense["amount"]

    return total


def get_budget_for_month(month):
    budgets = load_budgets()
    month_name = datetime(datetime.now().year, month, 1).strftime("%B")

    for budget in budgets:
        if budget["month"] == month_name:
            return budget["amount"]

    return None


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
def add_expense(description, amount, category):
    """
    Add a new expense to the expense list.

    Args:
        description (str): A short description of the expense.
        amount (float): The cost of the expense.
        category (str): A category of the expense.
    """

    if amount <= 0:
        print("Amount must be greater than 0")
        return

    category = category.capitalize()

    if category not in CATEGORIES:
        print(
            "Invalid category. Please choose from: "
            f"{', '.join(CATEGORIES)}"
        )
        return

    expenses = load_expenses()

    new_expense = {
        "id": generate_expense_id(expenses),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount,
        "category": category,
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    print(f"Expense added successfully (ID: {new_expense['id']})")

    expense_month = datetime.now().month
    monthly_total = get_monthly_expense_total(expense_month)
    monthly_budget = get_budget_for_month(expense_month)

    if monthly_budget is not None and monthly_total > monthly_budget:
        month_name = datetime.now().strftime("%B")

        print(
            f"Warning: You have exceeded your "
            f"{month_name} budget of "
            f"${monthly_budget:.2f}"
        )
    budgets = load_budgets()
    month_name = datetime(datetime.now().year, expense_month, 1).strftime("%B")

    for budget in budgets:
        if budget["month"] == month_name:
            return budget["amount"]

    return None


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


def list_expenses(category=None):
    """
    List expenses in a tabular format.

    Args:
        category (str, optional):
            Filter expenses by category.
    """

    expenses = load_expenses()

    if not expenses:
        print("No expenses found")
        return

    # Filter expenses by category if provided
    if category is not None:
        expenses = [
            expense for expense in expenses
            if expense["category"] == category
        ]

    # Table headings
    print("ID  Date        Description  Category        Amount")

    # Print each expense row
    for expense in expenses:
        print(
            f"{expense['id']:<3} "
            f"{expense['date']:<11} "
            f"{expense['description']:<12} "
            f"{expense['category']:<15} "
            f"${expense['amount']:.2f}"
        )
                

def show_summary(month=None):
    """
    Display a summary of expense totals.

    Args:
        month (int, optional):
            The month number used to filter expenses.
            If omitted, all expenses are included.
    """

    # Load all stored expenses from the JSON file
    expenses = load_expenses()

    # Exit early if no expenses exist
    if not expenses:
        return 0

    # Running total accumulator for expense amounts
    total_expenses = 0

    # -----------------------
    # MONTHLY SUMMARY
    # -----------------------

    # Generate summary for a specific month
    # only if a month argument was provided
    if month is not None:

        # Current calendar year
        current_year = datetime.now().year

        # Convert month number into readable month name
        # Example:
        # 8 -> August
        month_name = datetime(2026, month, 1).strftime("%B")

        # Iterate through every stored expense
        for expense in expenses:

            # Convert stored date string into
            # a datetime object for date operations
            expense_date = datetime.strptime(
                expense["date"],
                "%Y-%m-%d"
            )

            # Only include expenses matching:
            # - requested month
            # - current year
            if (
                expense_date.month == month
                and expense_date.year == current_year
            ):
                total_expenses += expense["amount"]

        # Display total for requested month
        print(f"Total expenses for {month_name}: ${total_expenses}")

    # -----------------------
    # ALL-TIME SUMMARY
    # -----------------------

    # If no month filter was provided,
    # calculate total expenses across all records
    else:
        for expense in expenses:
            total_expenses += expense["amount"]

        # Display overall expense total
        print(f"Total expenses: ${total_expenses}")


def add_budget(month, amount):

    budgets = load_budgets()
    month_name = calendar.month_name[month]

    for budget in budgets:
        if budget["month"] == month_name:
            budget["amount"] = amount
            save_budgets(budgets)
            print(
                f"Updated {month_name} "
                f"budget to ${amount:.2f}"
            )
            return

    budget = {
        "month": month_name,
        "amount": amount
    }

    budgets.append(budget)
    save_budgets(budgets)

    print(
        f"Budget set for {month_name}: "
        f"${amount:.2f}"
    )


def export_expenses_to_csv():
    """
    Export all expenses to a CSV file.
    """

    expenses = load_expenses()

    if not expenses:
        print("No expenses found to export")
        return

    with open(EXPORT_FILE, "w", newline="") as file:
        fieldnames = ["id", "date", "description", "category", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported successfully to {EXPORT_FILE}")


def main():
    """
    Main function to handle command-line arguments
    and execute corresponding functions.
    """

    # Initialize storage system
    initialize_storage()

    # Create CLI parser
    parser = create_parser()

    # Parse terminal arguments into Python values
    args = parser.parse_args()

    # -----------------------
    # COMMAND ROUTING
    # -----------------------

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)

    elif args.command == "list":
        list_expenses(args.category)

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "update":
        update_expense(
            args.id,
            args.description,
            args.amount
        )

    elif args.command == "summary":
        show_summary(args.month)

    elif args.command == "budget":
        add_budget(args.month, args.amount)

    elif args.command == "export":
        export_expenses_to_csv()


def create_parser():
    """
    Create and configure the command-line argument parser.

    Returns:
        argparse.ArgumentParser: The configured parser.
    """

    # Create the root CLI parser for the application.
    # This parser is responsible for reading and validating
    # all command-line input entered by the user.
    parser = argparse.ArgumentParser(prog="expense-tracker")


    # Enable support for subcommands such as:
    # add, delete, update, list, and summary.
    #
    # The selected subcommand will be stored in:
    # args.command
    #
    # required=True ensures the user must provide
    # a valid command when running the application.
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # -------------
    # ADD COMMAND #
    # -------------

    # Create the "add" subcommand parser.
    # This command is responsible for creating new expenses.
    add_parser = subparsers.add_parser("add")

    # Required expense description argument.
    # Example:
    # --description "Lunch"
    add_parser.add_argument("--description", required=True)

    # Required expense amount argument.
    # type=float automatically converts terminal input
    # into a floating-point number.
    # Example:
    # --amount 20
    add_parser.add_argument("--amount", type=float, required=True)

    # Required expense category argument.
    # Example:
    # --category "Bills"
    add_parser.add_argument("--category", required=True)


    # --------------
    # LIST COMMAND #
    # --------------

    # Create the "list" subcommand parser.
    # This command displays all stored expenses.
    #
    # No additional arguments are required.
    list_parser = subparsers.add_parser("list")

    # Optional category filter value
    # If omitted, display all expenses
    list_parser.add_argument("--category")


    # ----------------
    # DELETE COMMAND #
    # ----------------

    # Create the "delete" subcommand parser.
    # This command removes an expense by its ID.
    delete_parser = subparsers.add_parser("delete")

    # Required expense ID argument.
    # type=int converts the provided ID into an integer.
    # Example:
    # --id 3
    delete_parser.add_argument("--id", type=int, required=True)


    # ---------------- 
    # UPDATE COMMAND #
    # ----------------

    # Create the "update" subcommand parser.
    # This command modifies an existing expense.
    update_parser = subparsers.add_parser("update")

    # Required expense ID used to locate
    # the expense being updated.
    update_parser.add_argument("--id", type=int, required=True)

    # Optional updated description value.
    # If omitted, existing description remains unchanged.
    update_parser.add_argument("--description")

    # Optional updated amount value.
    # If omitted, existing amount remains unchanged.
    update_parser.add_argument("--amount", type=float)


    # -----------------
    # SUMMARY COMMAND #
    # -----------------

    # Create the "summary" subcommand parser.
    # This command calculates total expenses.
    summary_parser = subparsers.add_parser("summary")

    # Optional month filter argument.
    # Example:
    # --month 8
    #
    # If omitted, summary includes all expenses.
    summary_parser.add_argument("--month", type=int)


    # -----------------
    # BUDGET COMMAND #
    # -----------------

    # Create the "budget" subcommand parser.
    # This command sets the budget of a given month.
    budget_parser = subparsers.add_parser("budget")

    # Required budget month argument.
    # Example:
    # --description "8"
    budget_parser.add_argument("--month", type=int, required=True)

    # Required budget amount argument.
    # type=float automatically converts terminal input
    # into a floating-point number.
    # Example:
    # --amount 20
    budget_parser.add_argument("--amount", type=float, required=True)


    # -----------------
    # EXPORT COMMAND #
    # -----------------

    # Create the "export" subcommand parser.
    # This command exports expenses to a CSV file.
    subparsers.add_parser("export")

    return parser


if __name__ == "__main__":
    main()