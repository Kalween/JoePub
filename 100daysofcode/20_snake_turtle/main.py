from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
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
    if abs(snake.head.xcor() > 280) or abs(snake.head.ycor()) > 280 :
        score.game_over()
        game_on = False

    #Detect collision with head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

        


screen.exitonclick()






