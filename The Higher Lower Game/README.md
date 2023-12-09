
# The Higher Lower Game
Welcome to "The Higher Lower Game"! Test your intuition and see if you can guess which social media account has more followers.

## How to Play
- Run the code in a Python environment.
- You'll be presented with two social media accounts labeled 'A' and 'B'.
- Compare the number of followers each account has and input your guess by typing 'A' or 'B'.
- If your guess is correct, you'll earn a point, and a new round will begin.
- If your guess is incorrect, the game will end, and your final score will be displayed.

## Game Features
- Random Data: Social media account data is randomly selected for each round.
- Score Tracking: Your score is displayed after each correct guess.
- ASCII Art: Enjoy the visual appeal of ASCII art for a more engaging experience.
- Choice Validation: Invalid choices are handled gracefully.

## Code Structure
The code is organized into functions for better readability and maintenance:

- clear_screen(): Clears the console screen.
- get_random_data(): Retrieves random social media account data.
- format_data(account): Formats account data for display.
- print_data(): Prints the current choices and the VS graphic.
- reset_choice(), new_choice(), check_duplicate_choice(): Functions to manage the flow of the game.
- game(): The main game loop that takes user input and checks if the guess is correct.
- initialize_game(): Sets up the initial round of the game.


## Dependencies
This game requires the following dependencies:

- Python 3.x
- Random module

## Running the Game
- Save the code in a file with a .py extension.
- Open a terminal or command prompt.
- Navigate to the directory containing the file.
- Run the command: 

```bash
python higher_lower.py
```


*Enjoy "The Higher Lower Game" and see how many followers you can guess correctly!🎉*