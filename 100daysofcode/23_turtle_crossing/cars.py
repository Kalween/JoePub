from turtle import Turtle
import random

colors = [
    "red", "blue", "green", "yellow", "orange",
    "purple", "pink", "brown", "black", "white",
    "gray", "cyan", "magenta", "teal", "lime",
    "maroon", "navy", "olive", "coral", "indigo",
    "violet", "turquoise", "gold", "silver"
]

class Cars(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(colors))
        self.penup()


    def generate(self):
        self