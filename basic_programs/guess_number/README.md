# Guess the Number: Interactive Learning Project

**Learn fundamental programming concepts** through a classic number guessing game that demonstrates core Python skills and user interaction patterns.

## 🎯 Learning Objectives

- **Random Number Generation**: Using Python's `random` module for unpredictable behavior
- **Input Validation**: Processing and validating user input with error handling
- **Control Flow**: Conditional statements and loop structures
- **State Management**: Tracking game state (attempts, win/lose conditions)
- **User Experience**: Clear feedback and intuitive interaction design

## 🎮 How to Play

The computer selects a random number between 1 and 100. You have 10 attempts to guess it correctly.

```text
Welcome to Guess the Number!
I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it.

Attempt 1/10: Enter your guess: 50
Too low! Try a higher number.

Attempt 2/10: Enter your guess: 75
Too high! Try a lower number.

Attempt 3/10: Enter your guess: 63
🎉 Congratulations! You guessed 63 correctly in 3 attempts!
```

## 📚 Key Programming Concepts

### Core Language Features
- **Variables**: Storing and updating game state
- **Data Types**: Integers for numbers, strings for messages
- **Operators**: Comparison operators (`<`, `>`, `==`) for game logic

### Control Structures
- **While Loops**: Game continues until win or attempts exhausted
- **If/Else Statements**: Different responses based on guess accuracy
- **Break/Continue**: Loop control for game flow management

### Input/Output
- **User Input**: Reading keyboard input with `input()`
- **Output Formatting**: Clear, informative messages with `print()`
- **Error Handling**: Graceful handling of invalid inputs

### Python Standard Library
- **`random` Module**: Generating random numbers with `randint()`
- **String Methods**: Formatting output with f-strings
- **Exception Handling**: Managing invalid user inputs

## 🔧 Implementation Details

### Game Logic Flow
1. **Initialization**: Generate random number, set attempt counter
2. **Main Loop**: Continue while attempts remain and game not won
3. **Input Processing**: Read and validate user guess
4. **Comparison Logic**: Check if guess is too high, too low, or correct
5. **Feedback**: Provide clear guidance for next guess
6. **Win/Lose Check**: End game appropriately

### Code Structure
```python
import random

def play_game():
    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 10
    attempt_count = 0

    # Main game loop
    while attempts > 0:
        # Get and validate input
        # Compare guess with secret
        # Provide feedback
        # Check win condition

    # Game over - show result
```

## 🚀 Running the Game

```bash
# From the repository root
python basic_programs/guess_number/main.py

# Or using the launcher
python launcher.py
# Then select option 1
```

## 🧪 Testing & Edge Cases

Consider these scenarios when testing:
- **Valid guesses**: Numbers 1-100
- **Boundary values**: 1, 100, 50
- **Invalid inputs**: Non-numbers, numbers outside range
- **Win conditions**: Correct guess on first try, last attempt
- **Lose conditions**: All 10 attempts used without correct guess

## 🔄 Variations & Extensions

### Beginner Extensions
- Change the number range (1-50, 1-1000)
- Modify the number of attempts
- Add hints (even/odd, high/low range)

### Intermediate Extensions
- Track and display guess history
- Implement difficulty levels
- Add scoring system based on attempts used

### Advanced Extensions
- Multiple rounds with score tracking
- Statistics (average guesses per game)
- Different game modes (time-based, limited hints)

## 📈 Learning Progression

This project serves as an excellent **introduction to interactive programming** because it combines:
- ✅ Simple, understandable game mechanics
- ✅ Clear win/lose conditions
- ✅ Immediate user feedback
- ✅ Fundamental programming concepts
- ✅ Room for creative extensions

## 🔗 Related Projects

- **[Calculator](../calculator_cli/)**: More complex input processing
- **[Rock Paper Scissors](../rock_paper_scissors/)**: Random number applications
- **[Todo CLI](../todo_cli/)**: State management and data persistence

---

**Perfect starting point for learning Python through interactive applications!** 🎯
