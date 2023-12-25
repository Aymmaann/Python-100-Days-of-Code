from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-280, 250)
        self.write(arg=f"Level: {self.level}", align='left', font=('Courier', 22, 'normal'))

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align='left', font=('Courier', 22, 'normal'))

    def game_end(self):
        self.goto(0,0)
        self.write(arg="GAME OVER.", align='center', font=('Courier', 22, 'normal'))

