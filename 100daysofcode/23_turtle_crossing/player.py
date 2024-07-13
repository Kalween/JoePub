from turtle import Turtle


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(0,-280)


    def move(self):
        self.forward(10)