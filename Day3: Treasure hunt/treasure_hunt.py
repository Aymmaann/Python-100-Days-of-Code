print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure")
print('You' + "'" + 're at a cross road. Where do you want to go? Type "left" or "right"')
direction = input("What's your choice: ")
if direction == 'left':
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across')
elif direction == 'right':
    print('You reach a gloomy jungle. Type "ride" to ride the dune buggy or "walk" to walk across the jungle.')
else:
    print("Invalid choice. Game Over")

if direction=='left' or direction == 'right':
    next_step = input("What's your choice: ")
    if next_step == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one orange and one blue. Which colour do you choose?")
    elif next_step == 'swim':
        print("You tried to swim across the deadly sea. A hungry shark came across to kill you. Wrong choice :(")
    elif next_step == 'ride':
        print("You ride across the jungle in your buggy unharmed. There is a house with 3 doors. One red, one orange and one blue. Which colour do you choose?")
    elif next_step == 'walk':
        print("You tried to walk across the jungle. A hungry tiger set it's eyes on you and prowled on you as soon as it got a chance. Wrong choice :(")
    else:
        print("Invalid choice. Game Over")

if next_step == 'wait' or next_step == 'ride':
    colour = input("What's your choice: ")
    if colour == 'red':
        print("It's a room full of fire. Game Over.")
    elif colour == 'orange':
        print("You have found the treasure!! Congrats on beating the game. :)")
    elif colour == 'blue':
        print("It's a room full of mystery traps to harm you. Game Over.")
    else:
        print("Invalid choice. Game Over")
