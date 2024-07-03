from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def rotate_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=rotate_right)
screen.onkey(key='a', fun=rotate_left)

screen.exitonclick()