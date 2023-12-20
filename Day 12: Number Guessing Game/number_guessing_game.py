import random
import os

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess(attempts, number):
    while attempts!=0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        if guess == number:
            return 1
        elif guess < number:
            print("Too low.")
            print("Guess again.\n")
        else:
            print("Too high.")
            print("Guess again.\n")

        attempts-=1

    if attempts == 0:
        return 0

def game():
    clear_screen()
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number = random.randint(1,100)

    while True:
        if difficulty == 'easy':
            attempts = 10
            result = guess(attempts, number)
            if result == 1:
                print(f"\nYou got it! The answer was {number}.")
                break
            elif result == 0:
                print("\nYou've run out of guesses, you lose.")
                break

        elif difficulty == 'hard':
            attempts = 5
            result = guess(attempts, number)
            if result == 1:
                print(f"\nYou got it! The answer was {number}.")
                break
            elif result == 0:
                print("\nYou've run out of guesses, you lose.")
                break

        else:
            print("Invalid Choice")
            break

game()
