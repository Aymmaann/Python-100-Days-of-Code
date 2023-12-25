# Turtle Crossing Game

This is a simple Turtle Crossing game where the player, represented by a turtle, needs to navigate across the screen while avoiding cars. The game has multiple levels, and the player's objective is to clear each level by reaching the top of the screen.

## How to Play
- Use the Up arrow key to move the turtle upwards.
- Avoid colliding with the moving cars.
- Successfully cross the road to clear a level.
- The game gets progressively faster as you clear each level.
- If you collide with a car, the game ends.

## Instructions
### Dependencies: 
This game requires the turtle module. Ensure that you have it installed or available in your Python environment.

### Run the Game: 
Execute the main.py script to start the Turtle Crossing game. The game window will appear, and you can control the turtle using the Up arrow key.

## Game Elements:
- Turtle (Player): Represented by a green turtle, navigate it upwards to clear levels.
- Cars: Colored squares moving horizontally across the screen. Avoid colliding with them.
- Scoreboard: Displays the current level. The game ends when you collide with a car.
- Game Logic:As you successfully cross each level, the game becomes faster. Colliding with a car ends the game.

## Code Structure:
- main.py: The main script to run the game loop.
- car.py: Manages the creation and movement of cars.
- scoreboard.py: Handles the game's scoring and displays the level.
- player.py: Represents the player (turtle) and handles its movement.


## Run the game:
```bash
python main.py
```

*Feel free to explore the code and make modifications for a more customized gaming experience. Enjoy playing Turtle Crossing!*