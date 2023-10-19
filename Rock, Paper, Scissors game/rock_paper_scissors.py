import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("You entered an invalid number :(\n")  

computer = random.randint(0,2)
print(f"Computer chose {computer}")
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)


if user==computer:
    print("Its a draw!!")
elif user==0 and computer==2:
    print("You won")
elif user==2 and computer==0:
    print("You lost")

elif user==1 and computer==0:
    print("You won")
elif user==0 and computer==1:
    print("You lost")

elif user==2 and computer==1:
    print("You won")
elif user==1 and computer==2:
    print("You lost")