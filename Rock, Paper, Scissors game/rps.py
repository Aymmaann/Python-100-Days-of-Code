import random

def play():
    user = input("Enter your choice... 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    if user == computer:
        print("It's a tie!")
    elif win(user, computer):
        print("You won!")
    elif lost(user, computer):
        print("You lost :(")
    else:
        print("Invalid input")


def win(player, opponent):
    if (player == 'r' and opponent == 's'):
        print("Your rock beat my scissors!")
        return True
    elif (player == 'p' and opponent == 'r'):
        print("Your paper covered my rock")
        return True
    elif (player == 's' and opponent == 'p'):
        print("Your scissor cut my paper :(")
        return True
        
def lost(player, opponent):
    if (player=='r' and opponent=='p'):
        print("Your rock got covered by my paper")
        return True
    elif (player=='p' and opponent=='s'):
        print("I cut your paper")
        return True
    elif (player=='s' and opponent=='r'):
        print("You couldn't cut my rock")
        return True

play()
