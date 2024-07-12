from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.scoreleft = 0
        self.scoreright = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()
        

    def update_score(self):
        self.write(arg=f"Current Score \n {self.scoreleft} | {self.scoreright}",align="center",font=("Arial",10, "normal"))

    def score_left(self):
        self.scoreleft += 1
        self.clear()
        self.update_score()

    def score_right(self):
        self.scoreright += 1
        self.clear()
        self.update_score()
           