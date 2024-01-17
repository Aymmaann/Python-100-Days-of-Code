from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Collision with food
    if snake.head.distance(food) < 18:
        print(scoreboard.score)
        food.generate_food()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        scoreboard.reset()
        snake.reset()

    # Collision with itself
    for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 17:
                scoreboard.reset()
                snake.reset()






screen.exitonclick()