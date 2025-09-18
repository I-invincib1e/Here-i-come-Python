#!/usr/bin/env python3
"""
Game 9: Simple RPG
A basic text-based RPG adventure.
"""

import random

class Player:
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.defense = 5

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.health > 0 and enemy.health > 0:
        print(f"\nYour HP: {player.health}")
        print(f"{enemy.name} HP: {enemy.health}")

        action = input("Choose action (attack/run): ").lower()

        if action == "attack":
            damage = random.randint(player.attack-2, player.attack+2)
            enemy.health -= damage
            print(f"You deal {damage} damage!")

            if enemy.health > 0:
                enemy_damage = random.randint(enemy.attack-2, enemy.attack+2)
                actual_damage = player.take_damage(enemy_damage)
                print(f"{enemy.name} deals {actual_damage} damage!")

        elif action == "run":
            if random.random() < 0.5:
                print("You successfully ran away!")
                return True
            else:
                print("You couldn't escape!")
                enemy_damage = random.randint(enemy.attack-2, enemy.attack+2)
                actual_damage = player.take_damage(enemy_damage)
                print(f"{enemy.name} deals {actual_damage} damage!")
        else:
            print("Invalid action!")

    if player.health <= 0:
        print("You died!")
        return False
    else:
        print(f"You defeated the {enemy.name}!")
        return True

def rpg_game():
    print("Welcome to Simple RPG!")
    player = Player()

    enemies = [
        Enemy("Goblin", 30, 8),
        Enemy("Orc", 50, 12),
        Enemy("Dragon", 100, 20)
    ]

    for enemy in enemies:
        if not battle(player, enemy):
            print("Game Over!")
            return

    print("Congratulations! You completed the adventure!")

if __name__ == "__main__":
    rpg_game()
