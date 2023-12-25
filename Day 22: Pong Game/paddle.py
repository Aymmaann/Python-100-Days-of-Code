from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.goto(position)

    def up(self):
        y = self.ycor() + 30
        self.goto(self.xcor(), y)
    

    def down(self):
        y = self.ycor() - 30
        self.goto(self.xcor(), y)

