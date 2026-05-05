"""
Task command handlers.

This module contains business logic for:
- Creating tasks
- Updating tasks
- Deleting tasks
- Changing task status
- Listing tasks with optional filtering

It operates on persisted JSON data via utility functions.
"""

from datetime import datetime
from enum import Enum
from utilities import generate_id, load_tasks, write_tasks, find_task_by_id


class Status(Enum):
    """Enumeration of valid task statuses."""
    TODO = "TODO"
    IN_PROGRESS = "IN-PROGRESS"
    DONE = "DONE"


def _print_task(task):
    """
    Prints a single task in a consistent format.

    Args:
        task (dict): Task object.
    """
    print(f"Task ID: {task['id']}")
    print(f"Description: {task['description']}")
    print(f"Status: {task['status']}")
    print(f"Created At: {task['createdAt']}")
    print(f"Updated At: {task['updatedAt']}")
    print()


def _update_status(task, status):
    """
    Updates the status and timestamp of a task.

    Args:
        task (dict): Task object.
        status (Status): New status.
    """
    task["status"] = status.value
    task["updatedAt"] = datetime.now().isoformat()


# -----------------------
# CREATE
# -----------------------

def add_task(args):
    """
    Creates a new task and persists it.

    Args:
        args (list): CLI arguments containing description.
    """
    description = " ".join(args[1:])

    task = {
        "id": generate_id(),
        "description": description,
        "status": Status.TODO.value,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    tasks = load_tasks()
    tasks.append(task)
    write_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']})")


# -----------------------
# UPDATE
# -----------------------

def update_task(args):
    """
    Updates the description of an existing task.

    Args:
        args (list): CLI arguments containing task ID and description.
    """
    task_id = int(args[1])
    description = " ".join(args[2:])

    tasks = load_tasks()
    index = find_task_by_id(task_id, tasks)

    if index is None:
        print(f"Task with ID {task_id} not found.")
        return

    tasks[index]["description"] = description
    tasks[index]["updatedAt"] = datetime.now().isoformat()

    write_tasks(tasks)
    print(f"Task with ID {task_id} updated successfully.")


# -----------------------
# DELETE
# -----------------------

def delete_task(args):
    """
    Deletes a task by ID.

    Args:
        args (list): CLI arguments containing task ID.
    """
    task_id = int(args[1])

    tasks = load_tasks()
    index = find_task_by_id(task_id, tasks)

    if index is None:
        print(f"Task with ID {task_id} not found.")
        return

    del tasks[index]
    write_tasks(tasks)

    print(f"Task with ID {task_id} deleted successfully.")


# -----------------------
# STATUS UPDATES
# -----------------------

def mark_in_progress(args):
    """
    Marks a task as in-progress.

    Args:
        args (list): CLI arguments containing task ID.
    """
    task_id = int(args[1])

    tasks = load_tasks()
    index = find_task_by_id(task_id, tasks)

    if index is None:
        print(f"Task with ID {task_id} not found.")
        return

    _update_status(tasks[index], Status.IN_PROGRESS)
    write_tasks(tasks)

    print(f"Task with ID {task_id} marked as in-progress.")


def mark_done(args):
    """
    Marks a task as done.

    Args:
        args (list): CLI arguments containing task ID.
    """
    task_id = int(args[1])

    tasks = load_tasks()
    index = find_task_by_id(task_id, tasks)

    if index is None:
        print(f"Task with ID {task_id} not found.")
        return

    _update_status(tasks[index], Status.DONE)
    write_tasks(tasks)

    print(f"Task with ID {task_id} marked as done.")


# -----------------------
# LISTING
# -----------------------

def list_all_tasks():
    """
    Lists all tasks.
    """
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        _print_task(task)


def list_complete_tasks():
    """
    Lists all completed tasks.
    """
    tasks = load_tasks()
    filtered = [t for t in tasks if t["status"] == Status.DONE.value]

    if not filtered:
        print("No completed tasks found.")
        return

    for task in filtered:
        _print_task(task)


def list_incomplete_tasks():
    """
    Lists all tasks with TODO status.
    """
    tasks = load_tasks()
    filtered = [t for t in tasks if t["status"] == Status.TODO.value]

    if not filtered:
        print("No incomplete tasks found.")
        return

    for task in filtered:
        _print_task(task)


def list_in_progress_tasks():
    """
    Lists all in-progress tasks.
    """
    tasks = load_tasks()
    filtered = [t for t in tasks if t["status"] == Status.IN_PROGRESS.value]

    if not filtered:
        print("No in-progress tasks found.")
        return

    for task in filtered:
        _print_task(task)