from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("brown")
        self.stage = 1
        self.penup()
        self.setposition(-280,280)
        self.hideturtle()
        self.level()
    
    def level(self):
        self.write(f"Level: {self.stage}",align="left", font=("arial", 10, "normal"))
        
    
    def update_level(self):
        self.stage += 1
        self.clear()
        self.level()