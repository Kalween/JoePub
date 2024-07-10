from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
        self.speed(10)


