# Expense Tracker CLI

A command-line application for tracking and managing personal expenses. This project demonstrates CLI development, JSON data persistence, file handling, input validation, and financial reporting.

🔗 **Project Source:** https://roadmap.sh/projects/expense-tracker

🔗 **Repository:** https://github.com/Mika0x/backend-projects/tree/main/Beginner/expense-tracker

---

## 📌 Overview

Expense Tracker CLI is a lightweight tool that allows users to record, manage, and analyze expenses directly from the terminal.

All expense data is stored locally in JSON format, providing persistent storage without requiring a database. Users can create, update, delete, and view expenses, generate spending summaries, set monthly budgets, and export data for external use.

---

## 🚀 Features

### Core Features

- Add new expenses
- Update existing expenses
- Delete expenses
- View all expenses
- Generate total expense summaries
- Generate monthly expense summaries

### Additional Features

- Expense categories
- Filter expenses by category
- Monthly budget tracking
- Budget warnings when spending exceeds the configured budget
- Export expenses to CSV

---

## 🛠️ Tech Stack

- Python
- JSON file storage
- CSV export functionality
- Python Standard Library

---

## 📂 Project Structure

```text
expense-tracker/
│── data/
│   ├── expenses.json
│   └── budgets.json
│
│── exports/
│   └── expenses.csv
│
│── src/
│   ├── expense-tracker.py   # Entry point
│   ├── cli.py              # Command routing
│   ├── handlers.py         # Business logic
│   └── utilities.py        # File operations and persistence
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mika0x/backend-projects.git
cd backend-projects/Beginner/expense-tracker
```

### 2. Verify Python Installation

```bash
python3 --version
```

---

## ▶️ Usage

Run commands from the project directory:

```bash
python3 src/expense-tracker.py <command> [arguments]
```

---

## 📖 Commands

### ➕ Add an Expense

```bash
python3 src/expense-tracker.py add \
  --description "Lunch" \
  --amount 20 \
  --category Food
```

**Output**

```text
Expense added successfully (ID: 1)
```

---

### ✏️ Update an Expense

```bash
python3 src/expense-tracker.py update \
  --id 1 \
  --description "Lunch with coworkers" \
  --amount 25
```

---

### ❌ Delete an Expense

```bash
python3 src/expense-tracker.py delete --id 1
```

---

### 📋 List Expenses

```bash
python3 src/expense-tracker.py list
```

**Example Output**

```text
ID  Date        Description         Category    Amount
1   2026-05-30  Lunch               Food        $20.00
2   2026-05-30  Coffee              Food        $5.00
```

---

### 🔍 Filter Expenses by Category

```bash
python3 src/expense-tracker.py list --category Food
```

---

### 📊 View Total Expense Summary

```bash
python3 src/expense-tracker.py summary
```

**Example Output**

```text
Total expenses: $125.50
```

---

### 📅 View Monthly Expense Summary

```bash
python3 src/expense-tracker.py summary --month 8
```

**Example Output**

```text
Total expenses for August: $245.75
```

---

### 💰 Set a Monthly Budget

```bash
python3 src/expense-tracker.py budget --amount 1000
```

**Example Output**

```text
Budget for May set to $1000.00
```

---

### 📤 Export Expenses to CSV

```bash
python3 src/expense-tracker.py export
```

**Example Output**

```text
Expenses exported successfully to exports/expenses.csv
```

---

## 🧠 Expense Model

Each expense is stored using the following structure:

```json
{
  "id": 1,
  "description": "Lunch",
  "amount": 20.00,
  "category": "Food",
  "createdAt": "2026-05-30T12:30:00",
  "updatedAt": "2026-05-30T12:30:00"
}
```

---

## 📝 Notes

- Expense data is stored locally in JSON format.
- Expense IDs are generated automatically.
- Invalid amounts are rejected.
- Monthly summaries are calculated using expenses from the current year.
- Budget warnings are displayed when monthly spending exceeds the configured budget.
- CSV exports can be opened in spreadsheet applications such as Microsoft Excel or Google Sheets.

---

## 🔮 Future Improvements

- Recurring expenses
- Due dates and reminders
- Multiple budget categories
- Spending reports and analytics
- SQLite or PostgreSQL support
- REST API version using FastAPI
- Terminal table formatting and colored output

---

## 📄 License

This project is open-source and available under the MIT License.
