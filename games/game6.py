#!/usr/bin/env python3
"""
Game 6: Simple Snake Game
A basic snake game using tkinter.
"""

import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0

        self.root.bind("<Key>", self.change_direction)
        self.game_loop()

    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)

        if (new_head[0] < 0 or new_head[0] >= 400 or
            new_head[1] < 0 or new_head[1] >= 400 or
            new_head in self.snake):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+20, segment[1]+20, fill="green")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+20, self.food[1]+20, fill="red")
        self.canvas.create_text(200, 20, text=f"Score: {self.score}", fill="white")

    def game_loop(self):
        self.move_snake()
        self.draw()
        self.root.after(200, self.game_loop)

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 30))
        self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
