from turtle import Turtle
from snake import Snake
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear
        self.color("White")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        
    def update_score(self):
        self.write(arg=f"Current Score: {self.score} ",align="center", font=("Arial",20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Gam3 Ov3r",align="center", font=("Arial",20, "normal"))

    def inscrease_score(self):
        self.score +=1
        self.clear()
        self.update_score()