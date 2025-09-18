#!/usr/bin/env python3
"""
Game 7: Memory Game
A CLI memory matching game.
"""

import random
import time

def create_board(size=4):
    numbers = list(range(1, (size*size)//2 + 1)) * 2
    random.shuffle(numbers)
    board = [numbers[i:i+size] for i in range(0, len(numbers), size)]
    return board

def print_board(board, revealed):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if revealed[i][j]:
                print(f"{num:2}", end=" ")
            else:
                print(" ?", end=" ")
        print()

def memory_game():
    size = 4
    board = create_board(size)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    matches = 0
    total_pairs = (size * size) // 2

    print("Welcome to Memory Game!")
    print("Match all pairs by remembering positions.")

    while matches < total_pairs:
        print_board(board, revealed)

        try:
            print("\nEnter first position (row col): ")
            r1, c1 = map(int, input().split())
            print("Enter second position (row col): ")
            r2, c2 = map(int, input().split())

            if (r1, c1) == (r2, c2) or revealed[r1][c1] or revealed[r2][c2]:
                print("Invalid positions!")
                continue

            revealed[r1][c1] = True
            revealed[r2][c2] = True

            print_board(board, revealed)

            if board[r1][c1] == board[r2][c2]:
                print("Match!")
                matches += 1
            else:
                print("No match!")
                time.sleep(2)
                revealed[r1][c1] = False
                revealed[r2][c2] = False

        except (ValueError, IndexError):
            print("Invalid input!")

    print("Congratulations! You won!")

if __name__ == "__main__":
    memory_game()
