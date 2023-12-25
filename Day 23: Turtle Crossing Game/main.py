from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from car import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car = Car()
speed = 0.1

screen.listen()

screen.onkey(player.move_up, "Up")


game_on = True
while game_on:
    time.sleep(speed) 
    screen.update()
    car.create_car()
    car.move()

    # Cleared the level
    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset_position()
        speed *= 0.8

    # Collision with a car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            print("GA")
            game_on = False
            scoreboard.game_end()

screen.exitonclick()
