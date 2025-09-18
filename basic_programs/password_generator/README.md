# Password Generator

A command-line password generator that creates secure passwords with customizable options.

## Features

- Generate passwords of any length
- Include/exclude uppercase letters, digits, and symbols
- Password strength indicator
- Interactive CLI interface

## Usage

```bash
python main.py
```

Follow the prompts to customize your password generation options.

## Security Notes

- Uses Python's `random` module for randomness
- Includes strength checking based on length and character variety
- For production use, consider using `secrets` module instead of `random`
