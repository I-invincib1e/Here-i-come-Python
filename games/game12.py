#!/usr/bin/env python3
"""
Game 12: Simple Breakout Game
A basic breakout game using tkinter.
"""

import tkinter as tk
import random

class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Breakout Game")
        self.canvas = tk.Canvas(root, width=400, height=500, bg="black")
        self.canvas.pack()

        # Paddle
        self.paddle = self.canvas.create_rectangle(150, 470, 250, 480, fill="white")

        # Ball
        self.ball = self.canvas.create_oval(190, 230, 210, 250, fill="white")
        self.ball_dx = 2
        self.ball_dy = 2

        # Bricks
        self.bricks = []
        for i in range(5):
            for j in range(8):
                brick = self.canvas.create_rectangle(j*50, i*20+50, (j+1)*50, (i+1)*20+50, fill="red")
                self.bricks.append(brick)

        # Score
        self.score = 0
        self.score_text = self.canvas.create_text(200, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

        # Bind keys
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.game_loop()

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
        coords = self.canvas.coords(self.paddle)
        if coords[0] < 0:
            self.canvas.move(self.paddle, -coords[0], 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
        coords = self.canvas.coords(self.paddle)
        if coords[2] > 400:
            self.canvas.move(self.paddle, 400 - coords[2], 0)

    def game_loop(self):
        self.move_ball()
        self.root.after(10, self.game_loop)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        ball_coords = self.canvas.coords(self.ball)

        # Wall collisions
        if ball_coords[0] <= 0 or ball_coords[2] >= 400:
            self.ball_dx = -self.ball_dx
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy

        # Paddle collision
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_coords[3] >= paddle_coords[1] and
            ball_coords[2] >= paddle_coords[0] and
            ball_coords[0] <= paddle_coords[2]):
            self.ball_dy = -self.ball_dy

        # Brick collisions
        ball_center_x = (ball_coords[0] + ball_coords[2]) / 2
        ball_center_y = (ball_coords[1] + ball_coords[3]) / 2

        for brick in self.bricks[:]:
            brick_coords = self.canvas.coords(brick)
            if (brick_coords[0] <= ball_center_x <= brick_coords[2] and
                brick_coords[1] <= ball_center_y <= brick_coords[3]):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy = -self.ball_dy
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                break

        # Ball falls off
        if ball_coords[3] >= 500:
            self.canvas.create_text(200, 250, text="Game Over", fill="red", font=("Arial", 30))
            self.root.after(2000, self.root.quit)

        # Win condition
        if not self.bricks:
            self.canvas.create_text(200, 250, text="You Win!", fill="green", font=("Arial", 30))
            self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    game = BreakoutGame(root)
    root.mainloop()
