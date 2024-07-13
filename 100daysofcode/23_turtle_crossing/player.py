from turtle import Turtle


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.reset()


    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0,-280)