from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align='center', font=('Courier', 20, 'normal'))


    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", align='center', font=('Courier', 20, 'normal'))

    
    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
