from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What color will win? :" )
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_pos[turtle_index])
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win!, {winning_color} won the race")
                is_race_on = False
            else:
                print(f"Ohhh nooo.. You lost , {winning_color} won the race")
                is_race_on = False
        rand_distance = randint(0,10 )
        turtle.forward(rand_distance)



screen.exitonclick()