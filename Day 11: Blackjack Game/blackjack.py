import os
import random

max_score = 21
your_cards = []
computer_cards = []
score = computer_score = 0
choice = ""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_screen():
    os.system('cls' if  os.name == 'nt' else 'clear')

def winner(user_score, computer_score):
    if user_score == computer_score:
        print("It's a Draw!")
        return
    user = max_score - user_score
    computer = max_score - computer_score
    if 0 <= user < computer or computer_score > 21:
        print("You win 🤩")
    elif computer < user:
        print("You lose 😤")
    else:
        print("You went over. You lose 😤")
    return False

def ace(your_cards, score):
    score = sum(your_cards)
    if score > max_score and 11 in your_cards:
        index_11 = your_cards.index(11)
        your_cards[index_11] = 1
        score -= 10
    return score  
    
def hit(your_cards, computer_cards, computer_score):
    your_cards.append(random.choice(cards))
    score = 0
    score = sum(your_cards)
    score = ace(your_cards, score)

    if score > max_score:   
        print(f"    Your cards: {your_cards}, current score: {score}")
        print("You went over. You lost 😕")
        return False
    
    print(f"    Your cards: {your_cards}, current score: {score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    return True

def stand(your_cards, computer_cards):
    score, computer_score = 0, 0
    score = sum(your_cards)
    print(f"    Your final hand: {your_cards}, final score: {score}")

    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = 0
        computer_score = sum(computer_cards)
        computer_score = ace(computer_cards, computer_score)

    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    winner(score, computer_score)

def loop():
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    draw = True
    if user_choice == 'y':
        draw = hit(your_cards, computer_cards, computer_score)
        return draw
    elif user_choice == 'n':
        stand(your_cards, computer_cards)
        return False

while True:
    choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        clear_screen()
        print(logo)
        game = True
        score = 0
        your_cards = [random.choice(cards), random.choice(cards)]
        score = sum(your_cards)
        score = ace(your_cards, score)

        computer_cards = [random.choice(cards), random.choice(cards)]
        computer_score = sum(computer_cards)
        computer_score = ace(computer_cards, computer_score)

        print(f"    Your cards: {your_cards}, current score: {score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if computer_score == 21:
            print(f"    Computer's final cards: {computer_cards}")
            print("Computer got a Blackjack, You lose 😤")
            game = False
        if score == 21:
            print("You got a Blackjack, you win 🤩")
            game = False

    elif choice == 'n':
        print("See you later 👋")
        game = False
        break

    else:
        print("Invalid Choice\n")
        break

    while game and choice == 'y':
        result = loop()
        if result == False:
            break