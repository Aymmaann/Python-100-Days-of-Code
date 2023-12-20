import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_choice = screen.textinput(title="Turtle Race", prompt="Who will win the race? Enter a colour: ")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
y_positions = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []

if user_choice:
    race_on = True

for index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[index])
    all_turtles.append(new_turtle)

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color.lower() == user_choice.lower():
                print(f"You've won! The {winner_color} turtle is the winner")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner")

        turtle.forward(random.randint(0,10))


screen.exitonclick()
