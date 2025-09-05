import random
from typing import Literal


Choice = Literal["rock", "paper", "scissors"]


def computer_choice() -> Choice:
    return random.choice(["rock", "paper", "scissors"])  # type: ignore[return-value]


def decide(who: Choice, comp: Choice) -> str:
    if who == comp:
        return "draw"
    wins = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    return "win" if (who, comp) in wins else "lose"


def main() -> None:
    print("Rock, Paper, Scissors")
    print("Type rock/paper/scissors or q to quit.\n")
    while True:
        user = input("Your choice: ").strip().lower()
        if user in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        if user not in {"rock", "paper", "scissors"}:
            print("Invalid choice. Try again.\n")
            continue
        comp = computer_choice()
        outcome = decide(user, comp)  # type: ignore[arg-type]
        print(f"Computer chose: {comp}")
        if outcome == "draw":
            print("It's a draw!\n")
        elif outcome == "win":
            print("You win! 🎉\n")
        else:
            print("You lose!\n")


if __name__ == "__main__":
    main()


