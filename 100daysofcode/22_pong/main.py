from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with bounce wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #detect collision with paddle.
    if  ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) <50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    #detect collision with point wall
    if ball.xcor() >380:
        score.score_right()
        screen.update()
        ball.move_speed = 0.1
        ball.goto(0,0)
    elif ball.xcor() < -380:
        score.score_left()
        screen.update()
        ball.move_speed = 0.1
        ball.goto(0,0)
    
screen.exitonclick()

