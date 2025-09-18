#!/usr/bin/env python3
"""
Python Exercises Runner
A simple CLI to select and run Python exercises.
"""

import os
import subprocess
import sys

def list_exercises():
    """List all available exercises."""
    exercises = []
    for i in range(1, 11):
        filename = f"exercise{i}.py"
        if os.path.exists(filename):
            exercises.append((i, filename))
    return exercises

def run_exercise(exercise_num):
    """Run a specific exercise."""
    filename = f"exercise{exercise_num}.py"
    if os.path.exists(filename):
        print(f"\n{'='*50}")
        print(f"Running Exercise {exercise_num}")
        print(f"{'='*50}")
        try:
            result = subprocess.run([sys.executable, filename], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("Errors:")
                print(result.stderr)
        except Exception as e:
            print(f"Error running exercise: {e}")
    else:
        print(f"Exercise {exercise_num} not found.")

def main():
    print("Python Exercises Runner")
    print("=" * 30)

    exercises = list_exercises()

    if not exercises:
        print("No exercises found in this directory.")
        return

    print(f"Found {len(exercises)} exercises:")
    for num, filename in exercises:
        print(f"{num}. {filename}")

    while True:
        try:
            choice = input("\nEnter exercise number (1-10) or 'q' to quit: ").strip().lower()
            if choice == 'q':
                break
            exercise_num = int(choice)
            if 1 <= exercise_num <= 10:
                run_exercise(exercise_num)
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
