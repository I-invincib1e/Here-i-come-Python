import random
from typing import Literal

from shared.cli_utils import create_repl_loop


Choice = Literal["rock", "paper", "scissors"]


def computer_choice() -> Choice:
    return random.choice(["rock", "paper", "scissors"])  # type: ignore[return-value]


def decide(who: Choice, comp: Choice) -> str:
    if who == comp:
        return "draw"
    wins = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    return "win" if (who, comp) in wins else "lose"


def play_round(choice: str) -> None:
    """Play a single round of rock paper scissors."""
    if choice not in {"rock", "paper", "scissors"}:
        print("Invalid choice. Try rock, paper, or scissors.\n")
        return
    
    comp = computer_choice()
    outcome = decide(choice, comp)  # type: ignore[arg-type]
    print(f"Computer chose: {comp}")
    if outcome == "draw":
        print("It's a draw!\n")
    elif outcome == "win":
        print("You win! 🎉\n")
    else:
        print("You lose!\n")


def main() -> None:
    welcome = "Rock, Paper, Scissors\nType rock/paper/scissors to play"
    create_repl_loop(play_round, welcome, "Your choice: ")


if __name__ == "__main__":
    main()


