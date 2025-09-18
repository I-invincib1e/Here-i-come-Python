# Rock, Paper, Scissors (CLI)

Play against the computer using simple REPL input.

## How It Works

- Choices: `rock`, `paper`, `scissors`
- Computer picks randomly each round
- Outcome decided by a fixed win set: `{(rock,scissors), (scissors,paper), (paper,rock)}`
- Draw if both pick the same

## Example

```text
Your choice: rock
Computer chose: scissors
You win!
```

## Internals

- Functions: `computer_choice()`, `decide(user, comp)`
- Shared REPL loop handles input and errors
