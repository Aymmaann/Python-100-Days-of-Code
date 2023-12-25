from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from divider import Divider
import time

screen = Screen()

screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l =  Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
divider = Divider()
speed = 0.1

screen.listen()

if paddle_r.ycor() < 300 and paddle_r.ycor() > -300:
    screen.onkey(key="Up", fun=paddle_r.up)
    screen.onkey(key="Down", fun=paddle_r.down)


if paddle_l.ycor() < 300 and paddle_l.ycor() > -300:
    screen.onkey(key="w", fun=paddle_l.up)
    screen.onkey(key="s", fun=paddle_l.down)



game_on = True
while game_on:
    screen.update()

    time.sleep(ball.moving_speed)
    ball.move()

    # Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Ball missed by right paddle
    if ball.xcor() > 380:
        ball.reset()
        score.update_left_score()
        time.sleep(0.2)

    # Ball missed by left paddle
    if ball.xcor() < -380:
        ball.reset()
        score.update_right_score()
        time.sleep(0.2)

    # Collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x() 



screen.exitonclick()
