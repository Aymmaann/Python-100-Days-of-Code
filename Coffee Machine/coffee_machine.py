import random
import os
from coffee_data import MENU, resources 

choice = ""
money = 0
total = 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def return_resources():
    return resources


def format_resource(account):
    global money
    water = account['water']
    milk = account['milk']
    coffee = account['coffee']
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}$"


def process_coins():
    global total
    print("Please insert coins: ")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_resources(choice):
    if (resources['water'] - MENU[choice]['ingredients']['water']) < 0:
        return 1
    elif (resources['milk'] - MENU[choice]['ingredients']['milk']) < 0:
        return 2
    elif (resources['coffee'] - MENU[choice]['ingredients']['coffee']) < 0:
        return 3
    
    
def status(number):
    if number == 1:
        print(" Sorry there is not enough water.")
    elif number == 2:
        print(" Sorry there is not enough milk.")
    elif number == 3:
        print(" Sorry there is not enough coffee.")


def process_customer_request(choice):
    global money
    total = process_coins()
    bill = MENU[choice]['cost']
    money += MENU[choice]['cost']

    if bill > total:
        print("Sorry that's not enough money. Money refunded.")
    else: 
        change = total - bill
        print(f"Here is ${round(change, 2)} in change")
        print(f"Here is your {choice} ☕️. Enjoy!")
        checking = check_resources(choice)
        if checking == 1 or checking == 2 or checking == 3:
            status(checking)
        else:
            resources['water'] -= 50
            resources['coffee'] -= 18


clear_screen()
while True:
    total = 0
    choice = input(" What would you like? (espresso/latte/cappuccino): ")

    if choice == 'report':
        resource = format_resource(return_resources())
        print(resource)

    elif choice in ['espresso', 'latte', 'cappuccino']:
        process_customer_request(choice)

    else:
        print("Invalid Choice")