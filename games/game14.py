#!/usaartsgr/bin/env python3
"""
Game 14: Simple Space Invaders
A basic space invaders game in CLI.
"""

import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(width=20, height=10):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_board(board, score):
    clear_screen()
    print(f"Score: {score}")
    print('\n'.join([''.join(row) for row in board]))
    print('-' * len(board[0]))

def space_invaders():
    width, height = 20, 10
    board = create_board(width, height)

    # Player
    player_x = width // 2
    board[height-1][player_x] = 'A'

    # Enemies
    enemies = []
    for i in range(3):
        for j in range(5):
            enemy_x = 2 + j * 3
            enemy_y = 1 + i
            enemies.append([enemy_x, enemy_y])
            board[enemy_y][enemy_x] = 'V'

    score = 0
    direction = 1
    enemy_move_counter = 0

    while True:
        print_board(board, score)

        # Player input
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key == 'a' and player_x > 0:
                    board[height-1][player_x] = ' '
                    player_x -= 1
                    board[height-1][player_x] = 'A'
                elif key == 'd' and player_x < width-1:
                    board[height-1][player_x] = ' '
                    player_x += 1
                    board[height-1][player_x] = 'A'
                elif key == ' ':
                    # Shoot
                    bullet_x, bullet_y = player_x, height-2
                    while bullet_y > 0:
                        if board[bullet_y][bullet_x] == 'V':
                            board[bullet_y][bullet_x] = ' '
                            enemies = [e for e in enemies if e != [bullet_x, bullet_y]]
                            score += 10
                            break
                        bullet_y -= 1
                        time.sleep(0.05)

        # Move enemies
        enemy_move_counter += 1
        if enemy_move_counter % 5 == 0:
            # Check if enemies hit bottom
            if any(e[1] >= height-2 for e in enemies):
                print("Game Over!")
                return

            # Move enemies
            for enemy in enemies:
                board[enemy[1]][enemy[0]] = ' '

            for enemy in enemies:
                enemy[0] += direction
                if enemy[0] <= 0 or enemy[0] >= width-1:
                    direction = -direction
                    for e in enemies:
                        e[1] += 1
                    break

            for enemy in enemies:
                board[enemy[1]][enemy[0]] = 'V'

        if not enemies:
            print("You Win!")
            return

        time.sleep(0.1)

if __name__ == "__main__":
    space_invaders()
