import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
red_right_flag = 0
blue_right_flag = 0
red_left_flag = 0
blue_left_flag = 0
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title='Turtle Race', prompt="Who will win the race? Enter a colour(red/blue): ")
turtle_initial_position = [125, 75]
turtle_colors = ['red', 'blue']
all_turtles = []

def race_path(x=290, y=150):
    tom = Turtle()
    tom.speed('fastest')
    tom.pensize(6)
    tom.penup()
    tom.goto(x=-250, y=y)
    tom.pendown()
    tom.forward(x)
    tom.right(90)
    tom.forward(220)
    tom.left(90)
    tom.forward(300)
    tom.hideturtle()

def turn_right():
    global red_right_flag, blue_right_flag
    if red_turtle.xcor() > 0 and red_right_flag == 0:
        red_turtle.right(90)
        red_right_flag+=1
    if blue_turtle.xcor() > -40 and blue_right_flag == 0:
        blue_turtle.right(90)
        blue_right_flag+=1

def turn_left():
    global red_left_flag, blue_left_flag, red_right_flag, blue_right_flag
    if red_turtle.ycor() < -90 and red_left_flag == 0 and red_right_flag == 1:
        red_turtle.left(90)
        red_left_flag+=1
    if blue_turtle.ycor() < -140 and blue_left_flag == 0 and blue_right_flag == 1:
        blue_turtle.left(90)
        blue_left_flag+=1

def winner(turtle):
    global is_race_on
    if turtle.xcor() > 220:
        is_race_on = False
        winner_color = turtle.pencolor()
        if winner_color.lower() == user_choice.lower():
            print(f"You've won! The {winner_color} turtle is the winner")
        else:
            print(f"You've lost! The {winner_color} turtle is the winner")


if user_choice:
    race_path()
    race_path(x=190, y=50)
    is_race_on = True


red_turtle = Turtle(shape='turtle')
red_turtle.color(turtle_colors[0])
red_turtle.penup()
red_turtle.goto(x=-240, y=turtle_initial_position[0])
all_turtles.append(red_turtle)

blue_turtle = Turtle(shape='turtle')
blue_turtle.color(turtle_colors[1])
blue_turtle.penup()
blue_turtle.goto(x=-240, y=turtle_initial_position[1])
all_turtles.append(blue_turtle)

while is_race_on:
    red_turtle.forward(random.randint(0,10))
    blue_turtle.forward(random.randint(0,10))
    turn_right()
    turn_left()
    winner(red_turtle)
    winner(blue_turtle)

    
screen.exitonclick()