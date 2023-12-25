from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')    
        self.shapesize(stretch_len=0.2, stretch_wid=50)
