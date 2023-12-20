import turtle
from turtle import Turtle, Screen
import random

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tom = Turtle()
turtle.colormode(255)
tom.pensize(20)
tom.speed('fastest')


def start_position():
    tom.penup()
    tom.setheading(223)
    tom.forward(322)
    tom.setheading(0)


def reset_position():
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.right(180)

tom.hideturtle()
start_position()
for _ in range(10):
    for _ in range(10):
        tom.dot(20, random.choice(color_list))
        tom.forward(50)
    reset_position()

screen = Screen()
screen.exitonclick()
