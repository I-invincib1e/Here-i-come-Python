# Guess the Number (CLI)

The computer picks a number between 1 and 100. You have 10 attempts.

## How It Works

- Pick a random secret number once at startup
- For each input, validate integer in range 1–100
- Compare and respond (too low / too high / correct)
- Track attempts and stop at 0 or on correct guess

## Example

```text
Attempts left: 10
Enter your guess: 50
Too low!

Attempts left: 9
Enter your guess: 75
Too high!

Attempts left: 8
Enter your guess: 63
🎉 Correct! You guessed the number.
```

## Internals

- Random number from `random.randint(1, 100)`
- Simple loop with decrementing counter
- Clean exit on `q`/`quit`/`exit`
