# Guess the US States
## Overview
Welcome to the "Guess the US States" game! This Python program, using the Turtle graphics library, challenges players to identify and guess the names of all 50 states in the United States. The game interface showcases a map of the US states, with the challenge to fill in the blank states by correctly guessing their names.

## Instructions
1. Run the Python script in an environment that supports Turtle graphics.
2. A window will appear with a blank map of the US states.
3. Enter the name of a state when prompted and see if you can correctly identify it on the map.
4. If correct, the state name will be added to the map, and your score will be updated.
5. Repeat the process until you've identified all 50 states or choose to exit by typing "Exit."


## Features
- Interactive Interface: The Turtle graphics window provides an interactive platform to engage with the US map.
- Realistic State Placement: The program uses coordinates to accurately position each state on the map.
- Score Tracking: The game keeps track of your progress, displaying the number of correctly guessed states.


## Completion and Exiting
Once you successfully guess all 50 states, a congratulatory message will appear. If you choose to exit the game prematurely by typing "Quit," the program will generate a CSV file named "states_to_learn.csv." This file lists the states you have yet to guess, offering a learning opportunity for future gameplay.


## Acknowledgments
This program utilizes data from the provided CSV file, containing information about each state's name and coordinates.


## Files
- main.py: The main Python script containing the game logic.
- 50_states.csv: CSV file with the names and coordinates of the 50 US states.
- blank_states_img.gif: Image file used as the background for the turtle graphics.


## CSV File Structure
The CSV file includes the following columns:
- state: The name of the state.
- x: The x-coordinate for placing the state on the map.
- y: The y-coordinate for placing the state on the map.


*Enjoy the challenge and have fun exploring the geography of the United States!*
