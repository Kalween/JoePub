import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
t.pensize(2)
tim.speed("fastest")
tim.pensize(2)


def draw_spirograph(size_of_gap):

    for _ in range(int(350 / size_of_gap)):
        my_tuple = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        tim.color(my_tuple[0],my_tuple[1],my_tuple[2])
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()