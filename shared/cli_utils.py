"""
Shared CLI utilities for Python projects.
Provides common patterns for command-line applications.
"""

import sys
from typing import Callable, List, Optional


def handle_quit_input(user_input: str) -> bool:
    """
    Check if user wants to quit the application.

    Args:
        user_input: The user's input string

    Returns:
        True if user wants to quit, False otherwise
    """
    quit_commands = {"q", "quit", "exit"}
    return user_input.strip().lower() in quit_commands


def get_user_input(prompt: str = "> ", quit_message: str = "Goodbye!") -> Optional[str]:
    """
    Get user input with quit handling.

    Args:
        prompt: Input prompt to display
        quit_message: Message to print when user quits

    Returns:
        User input string, or None if user quit
    """
    try:
        user_input = input(prompt).strip()
        if handle_quit_input(user_input):
            print(quit_message)
            return None
        return user_input
    except (EOFError, KeyboardInterrupt):
        print(f"\n{quit_message}")
        return None


def validate_numeric_input(user_input: str, min_val: Optional[float] = None,
                          max_val: Optional[float] = None) -> Optional[float]:
    """
    Validate and convert numeric input.

    Args:
        user_input: String to validate
        min_val: Minimum allowed value (optional)
        max_val: Maximum allowed value (optional)

    Returns:
        Converted float value, or None if invalid
    """
    try:
        value = float(user_input)
        if min_val is not None and value < min_val:
            print(f"Value must be at least {min_val}")
            return None
        if max_val is not None and value > max_val:
            print(f"Value must be at most {max_val}")
            return None
        return value
    except ValueError:
        print("Please enter a valid number")
        return None


def create_repl_loop(process_input: Callable[[str], None],
                    welcome_message: str = "",
                    prompt: str = "> ") -> None:
    """
    Create a standard REPL (Read-Eval-Print Loop) for CLI applications.

    Args:
        process_input: Function to process user input
        welcome_message: Message to display at start
        prompt: Input prompt
    """
    if welcome_message:
        print(welcome_message)

    while True:
        user_input = get_user_input(prompt)
        if user_input is None:  # User quit
            break
        if not user_input:  # Empty input
            continue

        try:
            process_input(user_input)
        except Exception as e:  # noqa: BLE001
            print(f"Error: {e}")


def print_header(title: str, width: int = 50) -> None:
    """
    Print a formatted header.

    Args:
        title: Header text
        width: Width of the header
    """
    print(title.center(width, "="))


def print_menu(options: List[str], title: str = "Menu") -> None:
    """
    Print a numbered menu.

    Args:
        options: List of menu options
        title: Menu title
    """
    print(f"\n{title}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print()


def get_menu_choice(options: List[str], title: str = "Menu") -> Optional[int]:
    """
    Display menu and get user's choice.

    Args:
        options: List of menu options
        title: Menu title

    Returns:
        Selected option index (0-based), or None if invalid
    """
    print_menu(options, title)

    choice_input = get_user_input("Enter your choice: ")
    if choice_input is None:
        return None

    try:
        choice = int(choice_input) - 1  # Convert to 0-based index
        if 0 <= choice < len(options):
            return choice
        else:
            print(f"Please enter a number between 1 and {len(options)}")
            return None
    except ValueError:
        print("Please enter a valid number")
        return None
