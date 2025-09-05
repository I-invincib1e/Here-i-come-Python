import random


def play_game() -> None:
    secret_number: int = random.randint(1, 100)
    attempts_remaining: int = 10

    print("Guess the Number (1-100)")
    print("You have 10 attempts. Type 'q' to quit.\n")

    while attempts_remaining > 0:
        print(f"Attempts left: {attempts_remaining}")
        guess_input: str = input("Enter your guess: ").strip().lower()

        if guess_input in {"q", "quit", "exit"}:
            print("Goodbye!")
            return

        if not guess_input.isdigit():
            print("Please enter a valid integer between 1 and 100.\n")
            continue

        guess: int = int(guess_input)
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.\n")
            continue

        if guess == secret_number:
            print("🎉 Correct! You guessed the number.")
            return
        elif guess < secret_number:
            print("Too low!\n")
        else:
            print("Too high!\n")

        attempts_remaining -= 1

    print(f"Out of attempts! The number was {secret_number}.")


if __name__ == "__main__":
    play_game()


