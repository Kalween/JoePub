from turtle import Turtle
from snake import Snake



    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.clear
        self.color("White")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Current Score: {self.score} High Score: {self.high_score} ",align="center", font=("Arial",20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Gam3 Ov3r",align="center", font=("Arial",20, "normal"))

    def inscrease_score(self):
        self.score +=1
        self.update_score()