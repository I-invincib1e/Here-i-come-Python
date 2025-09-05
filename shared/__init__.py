"""
Shared utilities for Python projects.
"""

from .cli_utils import (
    create_repl_loop,
    get_user_input,
    handle_quit_input,
    print_header,
    print_menu,
    get_menu_choice,
    validate_numeric_input
)

__all__ = [
    "create_repl_loop",
    "get_user_input",
    "handle_quit_input",
    "print_header",
    "print_menu",
    "get_menu_choice",
    "validate_numeric_input"
]
