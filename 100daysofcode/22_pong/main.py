from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("oh herro")
screen.tracer(0)





paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()


screen.listen()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.forward(10)

    if ball.xcor() == paddle1.xcor():
        game_on = False


screen.exitonclick()

