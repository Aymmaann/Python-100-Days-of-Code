# Blackjack Game

Welcome to the Blackjack game! This is a simple text-based implementation of the classic Blackjack card game in Python.

## Rules
- The goal of the game is to get a hand value as close to 21 as possible without exceeding it.
- The game is played with a standard deck of cards, and each card has a value.
- Number cards (2-10) are worth their face value, face cards (King, Queen, Jack) are worth 10, and Aces can be worth either 1 or 11.
- The player is initially dealt two cards, and they can choose to "hit" to get another card or "stand" to keep their current hand.
- The dealer also gets two cards but follows a set of rules: they must hit until their hand value is at least 17.
- If the player's hand exceeds 21, they lose the game. If the dealer's hand exceeds 21, the player wins.
- The player with a hand value closest to 21 without exceeding it wins. In case of a tie, it's a draw.

## How to Play
- Run the script in a Python environment.
- You will be prompted to enter 'y' if you want to play or 'n' if you want to exit.
- If you choose to play ('y'), you will be dealt two cards, and the dealer will show their first card.
- You can then choose to "hit" or "stand" to improve your hand value.
- If you choose to play again after the round ends, your cards will be reset for a new game.
- If you choose not to play ('n'), the game will exit, and you'll see a goodbye message.


## Dependencies
This game requires the following dependencies:

- Python 3
- Random module

## Running the Game
To run the game, open a terminal window and navigate to the directory containing the blackjack.py file. Then, type the following command:

```bash
python blackjack.py
```
The game will start and you will be prompted to enter your choice.


*Enjoy the game, and good luck at the Blackjack table! 🃏🎉*