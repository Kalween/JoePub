from turtle import Turtle
SPEED = 10


class Paddle(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.x = x
        self.y = y
        self.setposition(x,y)

    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)