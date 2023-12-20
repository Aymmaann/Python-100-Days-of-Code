# Number Guessing Game
This is a simple console-based Number Guessing Game implemented in Python. The game generates a random number between 1 and 100, and the player has to guess the correct number within a limited number of attempts.

## How to Play
- Run the code in a Python environment.
- Follow the on-screen instructions to choose the difficulty level: 'easy' or 'hard'.
- Guess the number within the specified number of attempts.

## Game Features
- Difficulty Levels: Choose between 'easy' and 'hard' difficulty levels. 'easy' gives you more attempts to guess the number.
- Attempts: The number of attempts is limited based on the chosen difficulty level.
- Feedback: After each guess, the game provides feedback on whether the guess is too low or too high.
- Win/Lose: The game ends when the player correctly guesses the number or runs out of attempts.

## Code Structure
- logo: ASCII art representing the game logo.
- clear_screen(): Function to clear the console screen.
- guess(attempts, number): Function to handle the guessing logic. Returns 1 if the guess is correct, 0 if attempts run out.
- game(): Main function to initiate and run the game. It displays the logo, welcomes the player, and manages the game flow.

## How to Run
- Save the code in a file with a .py extension.
- Open a terminal or command prompt.
- Navigate to the directory containing the file.

## Dependencies
This game requires the following dependencies:

- Python 3.x
- Random module

## Running the Game
To run the game, open a terminal window and navigate to the directory containing the number_guessing_game.py file. Then, type the following command:

```bash
python number_guessing_game.py
```


*Enjoy the game, and good luck! 🃏🎉*