from turtle import Turtle
initial_position = (0, 270)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.goto(initial_position)
        self.write(arg=f"Score: {self.score}", align='center', font=('Cambria', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER.", align='center', font=('Courier', 20, 'normal'))