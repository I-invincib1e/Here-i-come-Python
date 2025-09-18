#!/usr/bin/env python3
"""
Password Generator - CLI
Generate secure passwords with customizable options.
"""

import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a random password with specified criteria."""
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("-" * 30)

    try:
        length = int(input("Enter password length (default 12): ") or 12)

        use_upper = input("Include uppercase letters? (y/n, default y): ").lower().strip()
        use_upper = use_upper != 'n'

        use_digits = input("Include digits? (y/n, default y): ").lower().strip()
        use_digits = use_digits != 'n'

        use_symbols = input("Include symbols? (y/n, default y): ").lower().strip()
        use_symbols = use_symbols != 'n'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")

        # Password strength check
        strength = 0
        if length >= 8:
            strength += 1
        if use_upper:
            strength += 1
        if use_digits:
            strength += 1
        if use_symbols:
            strength += 1

        strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
        print(f"Password Strength: {strength_levels[min(strength, 4)]}")

    except ValueError:
        print("Invalid input. Please enter a number for length.")

if __name__ == "__main__":
    main()
