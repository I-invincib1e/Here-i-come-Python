import random

from shared.cli_utils import create_repl_loop


def play_game() -> None:
    secret_number: int = random.randint(1, 100)
    attempts_remaining: int = 10

    print("Guess the Number (1-100)")
    print("You have 10 attempts. Type 'q' to quit.\n")

    def handle_guess(guess_input: str) -> None:
        nonlocal attempts_remaining, secret_number
        if attempts_remaining <= 0:
            print(f"Out of attempts! The number was {secret_number}.")
            raise SystemExit

        if not guess_input.isdigit():
            print("Please enter a valid integer between 1 and 100.\n")
            return

        guess: int = int(guess_input)
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.\n")
            return

        if guess == secret_number:
            print("🎉 Correct! You guessed the number.")
            raise SystemExit
        elif guess < secret_number:
            print("Too low!\n")
        else:
            print("Too high!\n")

        attempts_remaining -= 1
        if attempts_remaining > 0:
            print(f"Attempts left: {attempts_remaining}")
        else:
            print(f"Out of attempts! The number was {secret_number}.")
            raise SystemExit

    try:
        create_repl_loop(handle_guess, "", "Enter your guess: ")
    except SystemExit:
        pass


if __name__ == "__main__":
    play_game()


