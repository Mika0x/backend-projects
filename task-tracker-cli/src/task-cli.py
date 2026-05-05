#!/usr/bin/env python3

"""
Entry point for the Task Tracker CLI application.

Parses command-line arguments and delegates execution
to the CLI command handler.
"""

import sys
from cli import handle_command


def main():
    """
    Main execution function.

    Extracts command-line arguments and passes them to the CLI handler.
    """
    args = sys.argv[1:]

    if not args:
        print("No command provided.")
        return

    handle_command(args)


if __name__ == "__main__":
    main()