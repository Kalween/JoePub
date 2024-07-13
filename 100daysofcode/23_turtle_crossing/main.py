from turtle import Screen
from player import Player
from cars import Cars
import time


screen = Screen()
screen.bgcolor("white")
screen.setup(width=600,height=600,startx=2500, starty=300)
screen.title("Crossing turtle wurtle")
screen.tracer(0)

player = Player()
cars = Cars()

game_on = True
screen.listen()
screen.onkeypress(player.move,"Up")

while game_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() == 280:
        print("yes")

screen.exitonclick()