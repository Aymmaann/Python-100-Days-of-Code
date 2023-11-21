import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("Welcome to the secret auction program\n")
bids = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bids):
    highest_bid, duplicates = 0, 0
    winner = ""
    for key in bids:
        current_bid = bids[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            duplicates = 1
            winner = key
        elif current_bid == highest_bid:
            duplicates+=1

    if duplicates > 1:
        print("\nIt's a tie!")
    else:
        print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")

while True:
    name = input("\nWhat is your name? ")
    amount = int(input("What's your bid? $"))
    bids[name] = amount
    choice = input("\nAre there any bidders? Type 'yes' or 'no'\n")
    if choice == 'no':
        highest_bidder(bids)
        break
    elif choice != 'yes':
        print("\nInvalid Choice")
        break
    clear_screen()