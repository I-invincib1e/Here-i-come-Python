#!/usr/bin/env python3
"""
Game 11: Simple Pong Game
A basic pong game using tkinter.
"""

import tkinter as tk
import random

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack()

        # Paddle
        self.paddle = self.canvas.create_rectangle(250, 350, 350, 360, fill="white")

        # Ball
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.ball_dx = 3
        self.ball_dy = 3

        # Score
        self.score = 0
        self.score_text = self.canvas.create_text(300, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

        # Bind keys
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.game_loop()

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
        # Keep paddle in bounds
        coords = self.canvas.coords(self.paddle)
        if coords[0] < 0:
            self.canvas.move(self.paddle, -coords[0], 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
        # Keep paddle in bounds
        coords = self.canvas.coords(self.paddle)
        if coords[2] > 600:
            self.canvas.move(self.paddle, 600 - coords[2], 0)

    def game_loop(self):
        self.move_ball()
        self.root.after(20, self.game_loop)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        # Ball collision with walls
        ball_coords = self.canvas.coords(self.ball)
        if ball_coords[0] <= 0 or ball_coords[2] >= 600:
            self.ball_dx = -self.ball_dx
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddle
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_coords[3] >= paddle_coords[1] and
            ball_coords[2] >= paddle_coords[0] and
            ball_coords[0] <= paddle_coords[2]):
            self.ball_dy = -self.ball_dy
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        # Ball falls off screen
        if ball_coords[3] >= 400:
            self.canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 30))
            self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
