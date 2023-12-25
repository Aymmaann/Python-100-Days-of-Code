from turtle import Turtle, TurtleScreen
import random
import time

colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']

class Car():
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        chance = random.randint(1, 3)
        if chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(colors))
            new_car.goto(320, random.randint(-200, 200))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(10)