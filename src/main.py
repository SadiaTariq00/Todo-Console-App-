#!/usr/bin/env python3
"""
Entry point for the In-Memory Python Console Todo Application.

This module initializes the application and starts the main console interface.
"""

from ui.console import ConsoleUI


def main():
    """Main entry point for the todo application."""
    print("Welcome to the In-Memory Python Console Todo Application!")
    print("=" * 55)

    # Initialize and start the console UI
    console_ui = ConsoleUI()
    console_ui.run()


if __name__ == "__main__":
    main()