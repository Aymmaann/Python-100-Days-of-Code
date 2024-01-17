from turtle import Turtle
import random
colors = ['red', 'blue', 'green', 'SpringGreen', 'yellow', 'LightSkyBlue', 'PeachPuff']

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed('fastest')
        self.generate_food()

    def generate_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 250)
        self.color(random.choice(colors))
        self.goto(x, y)
