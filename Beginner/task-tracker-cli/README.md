# Task Tracker CLI

A command-line application for managing tasks with persistent JSON storage.  
This project allows users to create, update, delete, and track the status of tasks directly from the terminal.

🔗 Project Source: https://roadmap.sh/projects/task-tracker

🔗 Repository: https://github.com/Mika0x/task-tracker-cli

---

## 📌 Overview

Task Tracker CLI is a lightweight tool designed to help users manage tasks efficiently using simple command-line commands.  
All tasks are stored locally in a JSON file, making the application fast, portable, and easy to use without external dependencies.

---

## 🚀 Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as **in-progress** or **done**
- List all tasks
- Filter tasks by status:
  - `todo`
  - `in-progress`
  - `done`

---

## 🛠️ Tech Stack

- Python (standard library only)
- JSON file for data persistence

---

## 📂 Project Structure

```
task-tracker-cli/
│── data/
│   └── tasks.json
│── src/
│   ├── task-cli.py      # Entry point
│   ├── cli.py           # Command routing
│   ├── handlers.py      # Business logic
│   └── utilities.py     # Data persistence
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli
```

2. Ensure you have Python installed:

```
python3 --version
```

---

## ▶️ Usage

Run commands from the project root:

```
python3 src/task-cli.py <command> [arguments]
```

---

## 📖 Commands

### ➕ Add a Task

```
python3 src/task-cli.py add "Buy groceries"
```

---

### ✏️ Update a Task

```
python3 src/task-cli.py update 1 "Buy groceries and cook dinner"
```

---

### ❌ Delete a Task

```
python3 src/task-cli.py delete 1
```

---

### 🔄 Mark Task Status

```
python3 src/task-cli.py mark-in-progress 1
python3 src/task-cli.py mark-done 1
```

---

### 📋 List Tasks

List all tasks:

```
python3 src/task-cli.py list
```

Filter by status:

```
python3 src/task-cli.py list todo
python3 src/task-cli.py list in-progress
python3 src/task-cli.py list done
```

---

## 🧠 Task Model

Each task is stored with the following structure:

```
{
  "id": 1,
  "description": "Buy groceries",
  "status": "TODO",
  "createdAt": "2026-05-01T19:00:00",
  "updatedAt": "2026-05-01T19:00:00"
}
```

---

## 📝 Notes

- Task IDs are generated using a **gap-based system**, meaning the lowest available ID is reused when tasks are deleted.
- No external libraries are used—this project relies entirely on Python’s standard library.

---

## 🔮 Future Improvements

- Convert CLI into a REST API (FastAPI)
- Add persistent database support (SQLite/PostgreSQL)
- Implement task prioritization and due dates
- Improve CLI output formatting (tables / colors)

---

## 📄 License

This project is open-source and available under the MIT License.
