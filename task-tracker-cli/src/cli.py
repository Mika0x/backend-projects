"""
CLI command router for the Task Tracker application.

This module is responsible for:
- Parsing user input from the command line
- Validating arguments
- Routing commands to the appropriate handler functions

It does NOT contain business logic or data persistence.
"""

from handlers import (
    add_task,
    update_task,
    delete_task,
    mark_in_progress,
    mark_done,
    list_all_tasks,
    list_complete_tasks,
    list_in_progress_tasks,
    list_incomplete_tasks,
)


def handle_command(args):
    """
    Routes CLI commands to their respective handlers.

    Args:
        args (list): Command-line arguments excluding the script name.
    """
    command = args[0]

    # -----------------------
    # ADD TASK
    # -----------------------
    if command == "add":
        # Require at least one word for description
        if len(args) < 2:
            print('Usage: task-cli add "description"')
            return

        add_task(args)

    # -----------------------
    # UPDATE TASK
    # -----------------------
    elif command == "update":
        # Require: command + id + at least one word of description
        if len(args) < 3:
            print('Usage: task-cli update [id] "new description"')
            return

        # Validate ID
        if not args[1].isdigit():
            print("Error: ID must be a number.")
            return

        update_task(args)

    # -----------------------
    # DELETE TASK
    # -----------------------
    elif command == "delete":
        if len(args) < 2:
            print("Usage: task-cli delete [id]")
            return

        if not args[1].isdigit():
            print("Error: ID must be a number.")
            return

        delete_task(args)

    # -----------------------
    # MARK TASK STATUS
    # -----------------------
    elif command in ["mark-in-progress", "mark-done"]:
        if len(args) < 2:
            print(f"Usage: task-cli {command} [id]")
            return

        if not args[1].isdigit():
            print("Error: ID must be a number.")
            return

        # Dispatch based on command
        if command == "mark-in-progress":
            mark_in_progress(args)
        else:
            mark_done(args)

    # -----------------------
    # LIST TASKS
    # -----------------------
    elif command == "list":
        # No filter → list all tasks
        if len(args) == 1:
            list_all_tasks()
            return

        # Filtered listing
        if len(args) == 2:
            option = args[1]

            if option == "done":
                list_complete_tasks()
            elif option == "todo":
                list_incomplete_tasks()
            elif option == "in-progress":
                list_in_progress_tasks()
            else:
                print(
                    "Error: Invalid list option. Use 'done', 'todo', or 'in-progress'."
                )
            return

        # Too many arguments
        print("Usage: task-cli list [done|todo|in-progress]")

    # -----------------------
    # UNKNOWN COMMAND
    # -----------------------
    else:
        print(f"Unknown command: {command}")