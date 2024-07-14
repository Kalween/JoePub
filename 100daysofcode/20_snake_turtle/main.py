from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600,startx=2500, starty=300)
screen.bgcolor("black")
screen.title("snakeola")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down" )
screen.onkey(snake.left,"Left" )
screen.onkey(snake.right,"Right")

    
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inscrease_score()

    # Detection with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280  or snake.head.ycor() <-280:
        score.reset()
        snake.reset()


    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

        


screen.exitonclick()






