"""
Utility functions for task persistence and retrieval.

This module is responsible for:
- Loading and saving task data from/to a JSON file
- Generating unique task IDs (gap-based strategy)
- Locating tasks within the dataset
"""

import json
import os


# Resolve data file path relative to this file (robust across environments)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "../data/tasks.json")


def load_tasks():
    """
    Loads tasks from the JSON data file.

    Returns:
        list: A list of task dictionaries. Returns an empty list if the file
              does not exist or contains invalid JSON.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_tasks(tasks):
    """
    Writes tasks to the JSON data file.

    Args:
        tasks (list): List of task dictionaries to persist.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def generate_id():
    """
    Generates the lowest available positive integer ID.

    This function fills gaps in the ID sequence. For example:
        Existing IDs: [1, 2, 4] → returns 3
        Existing IDs: [2, 3, 4] → returns 1

    Returns:
        int: The smallest available positive integer ID.
    """
    tasks = load_tasks()

    if not tasks:
        return 1

    existing_ids = {task["id"] for task in tasks}

    new_id = 1
    while new_id in existing_ids:
        new_id += 1

    return new_id


def find_task_by_id(task_id, tasks):
    """
    Finds the index of a task by its ID.

    Args:
        task_id (int): The ID of the task to locate.
        tasks (list): The list of task dictionaries.

    Returns:
        int | None: Index of the task if found, otherwise None.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return index

    return None