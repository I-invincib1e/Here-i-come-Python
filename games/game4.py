#!/usr/bin/env python3
"""
Game 4: Hangman
A word guessing game with limited attempts.
"""

import random

def choose_word():
    words = ["python", "programming", "computer", "algorithm", "function", "variable"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print("Wrong guess!")

    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
