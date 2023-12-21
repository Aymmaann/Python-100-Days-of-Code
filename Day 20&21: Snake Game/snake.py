from turtle import Turtle, Screen
screen = Screen()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


def create_snake():
    tom = Turtle(shape='square')
    tom.color('white')
    return tom


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)


    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    
    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[seg_num - 1].xcor()
            y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x=x, y=y)
        self.head.forward(move_distance)


    def extend(self):
        self.add_segment(self.snake_body[-1].position())
            
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)