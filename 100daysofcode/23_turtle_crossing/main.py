from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time, random

difficulty = 5

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600,height=600,startx=2500, starty=300)
screen.title("Crossing turtle wurtle")
screen.tracer(0)

player = Player()
cars = Cars()
score = Scoreboard()

game_on = True
screen.listen()
screen.onkeypress(player.move,"Up")

while game_on:

    cars.create_car()
    cars.move()
    time.sleep(0.1)
    screen.update()

    # Detect goal
    if player.ycor() == 280:
        cars.increase_level()
        score.update_level()
        player.reset()

    # Detect collision
    for car in cars.all_cars:
        if player.distance(car) < 27:
            game_on = False


screen.exitonclick()