# Pong Game

## Overview
This is a simple implementation of the classic Pong game using the Turtle graphics library in Python. The game involves two paddles and a ball, where players control the paddles to hit the ball back and forth. The goal is to score points by making the ball pass the opponent's paddle.

## Components

### main.py
This script serves as the entry point for the Pong game. It initializes the game window, creates instances of the Paddle, Ball, Scoreboard, and Divider classes, and sets up the game loop. The script handles user input, updates the game state, and checks for collisions.

### paddle.py
The Paddle class defines the characteristics and behavior of the paddles in the game. Paddles can move up and down and are controlled by user input. They are represented as white square shapes on the screen.

### ball.py
The Ball class represents the ball in the game. The ball moves continuously and bounces off walls and paddles. The speed of the ball increases upon collision with paddles. The ball resets its position when it misses a paddle.

### scoreboard.py
The Scoreboard class manages the scoring system in the game. It keeps track of the left and right players' scores and updates the display accordingly. The scores are shown at the top of the game window.

### divider.py
The Divider class represents the center divider line on the game screen. It is a stationary white square that separates the left and right playing areas.

## How to Play
- Player on the right uses the Up and Down arrow keys to control their paddle.
- Player on the left uses the W and S keys to control their paddle.

## Game Rules
- The ball bounces off the top and bottom walls.
- If the ball passes the right paddle, the left player scores a point.
- If the ball passes the left paddle, the right player scores a point.
- The game continues until the players decide to exit.

## Run the game:
```bash
python main.py
```

*Enjoy playing the Pong game!*