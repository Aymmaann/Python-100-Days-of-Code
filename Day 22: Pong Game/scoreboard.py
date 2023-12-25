from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 220)
        self.write(arg=f"{self.l_score}", align="center", font=("Courier", 70, "normal"))
        self.goto(100, 220)
        self.write(arg=f"{self.r_score}", align="center", font=("Courier", 70, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(arg=f"{self.l_score}", align="center", font=("Courier", 70, "normal"))
        self.goto(100, 220)
        self.write(arg=f"{self.r_score}", align="center", font=("Courier", 70, "normal"))

    def update_left_score(self):
        self.l_score += 1
        self.update_score()

    def update_right_score(self):
        self.r_score += 1
        self.update_score()