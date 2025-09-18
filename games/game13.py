#!/usr/bin/env python3
"""
Game 13: Simple Tetris-like Game
A basic falling blocks game in CLI.
"""

import random
import time

def create_board(width=10, height=20):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_board(board):
    print('\n'.join([''.join(row) for row in board]))
    print('-' * len(board[0]))

def get_random_piece():
    pieces = [
        [['#']],  # Single block
        [['#', '#']],  # Two blocks horizontal
        [['#'], ['#']],  # Two blocks vertical
        [['#', '#'], ['#', '#']]  # Square
    ]
    return random.choice(pieces)

def can_place(board, piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell == '#':
                if (y + i >= len(board) or
                    x + j < 0 or x + j >= len(board[0]) or
                    board[y + i][x + j] != ' '):
                    return False
    return True

def place_piece(board, piece, x, y):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell == '#':
                board[y + i][x + j] = '#'

def clear_lines(board):
    lines_cleared = 0
    for i in range(len(board)):
        if all(cell == '#' for cell in board[i]):
            del board[i]
            board.insert(0, [' ' for _ in range(len(board[0]))])
            lines_cleared += 1
    return lines_cleared

def tetris_game():
    board = create_board()
    score = 0
    game_over = False

    while not game_over:
        piece = get_random_piece()
        x = len(board[0]) // 2 - len(piece[0]) // 2
        y = 0

        while True:
            print_board(board)
            print(f"Score: {score}")

            # Check if piece can be placed
            if not can_place(board, piece, x, y):
                game_over = True
                break

            # Move piece down
            time.sleep(0.5)
            y += 1

            # Check if piece should stop
            if not can_place(board, piece, x, y):
                place_piece(board, piece, x - 1, y - 1)
                score += clear_lines(board) * 10
                break

    print("Game Over!")
    print(f"Final Score: {score}")

if __name__ == "__main__":
    tetris_game()
