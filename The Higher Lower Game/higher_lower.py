import random
import os
from hl_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score = 0
choice = ""
play = True
a_followers = b_followers = 0
choice_a = choice_b = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_data():
    return random.choice(data)


def format_data(account):
    Name = account['name']
    Description = account['description']
    Country = account['country']
    return f"{Name}, a {Description}, from {Country}"


def print_data():
    global choice_a, choice_b, a_followers, b_followers 
    print(f"Compare A: {choice_a}")
    print(vs)
    print(f"Against B: {choice_b}")

def reset_choice():
    global choice_a, choice_b, a_followers, b_followers 
    choice_a = choice_b
    a_followers = b_followers

def new_choice():
    global choice_b, b_followers 
    choice_b = get_random_data()
    b_followers = choice_b['follower_count']
    choice_b = format_data(choice_b)

def check_duplicate_choice():
    global choice_a, choice_b, a_followers, b_followers 
    while choice_b == choice_a:
        choice_b = new_choice()
        b_followers = choice_b['follower_count']

def game_should_continue():
    reset_choice()
    new_choice()
    check_duplicate_choice()

def game():
    global play, score, choice_a, choice_b, a_followers, b_followers
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear_screen()
    print(logo)
    if (choice == 'A' and a_followers > b_followers) or (choice == 'B' and a_followers < b_followers):
        score += 1
        print(f"You're right! Current score: {score}.")
        game_should_continue()
        print_data()
    elif (choice == 'A' and a_followers < b_followers) or (choice == 'B' and a_followers > b_followers):
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False
    else:
        print("Invalid Choice")


def initialize_game():
    global choice_a, choice_b, a_followers, b_followers 
    clear_screen()
    print(logo)
    choice_a = get_random_data()
    a_followers = choice_a['follower_count']
    choice_a = format_data(choice_a)
    print(f"Compare A: {choice_a}")

    print(vs)
    choice_b = get_random_data()
    b_followers = choice_b['follower_count']
    choice_b = format_data(choice_b)
    print(f"Against B: {choice_b}")


initialize_game()
while play:
    game()