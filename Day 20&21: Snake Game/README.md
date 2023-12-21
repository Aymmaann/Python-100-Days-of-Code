# Snake Game
Classic Snake Game built using Python's Turtle graphics.

## Table of Contents
- Description
- Features
- How to Play
- Installation
- Controls
- Class Description

## Description
This Snake Game is a simple implementation of the classic snake game using Python's Turtle graphics. The snake moves around the screen, eating food to grow longer. The game ends if the snake collides with the wall or itself.

## Features
- Simple and intuitive gameplay.
- Colorful turtle-shaped food.
- Scoreboard to keep track of the player's score.

## How to Play
- Clone or download the repository to your local machine.
- Run the main.py file using a Python interpreter.
- Use the arrow keys to control the snake's direction.
- Eat the colorful turtle-shaped food to grow longer and increase your score.
- Avoid colliding with the walls or the snake's own body.
- The game ends when the snake collides, and the final score is displayed.

# Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/Snake-Game.git
```

Navigate to the project directory:
```bash
cd Snake-Game
```

Run the game:
```bash
python main.py
```

## Controls
- Up Arrow: Move the snake up
- Down Arrow: Move the snake down
- Left Arrow: Move the snake left
- Right Arrow: Move the snake right

## Class Description
1. *Snake Class (snake.py)*
The Snake class manages the behavior and attributes of the snake in the game. It includes methods for creating the snake, moving it, extending its length, and handling user input for direction changes. The class uses the Turtle graphics library to represent the snake on the screen.

2. *Food Class (food.py)*
The Food class represents the food items that the snake consumes to grow longer. Each food item is a colored turtle-shaped object that appears at random positions on the screen. The class includes a method (generate_food()) to randomly position the food on the screen.

3. *Scoreboard Class (scoreboard.py)* It keeps track of the player's score, updates the score when the snake eats food, and displays the final score when the game ends. The scoreboard is displayed at the top of the game window.

4. *Main Script (main.py)*
It initializes the game window using the Turtle graphics library, creates instances of the Snake, Food, and Scoreboard classes, and sets up the game loop. The script handles user input for controlling the snake, updates the game state, and checks for collisions with walls and the snake's body.

These classes work together to create a modular and organized structure for the Snake Game, making it easier to understand, maintain, and extend the code. 



*Feel free to customize it further based on your specific project details and preferences! Enjoy slithering!*   