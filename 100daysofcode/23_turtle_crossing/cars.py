from turtle import Turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
colors = [
    "red", "blue", "green", "yellow", "orange",
    "purple", "pink", "brown", "black",
    "gray", "cyan", "magenta", "teal", "lime",
    "maroon", "navy", "olive", "coral", "indigo",
    "violet", "turquoise", "gold", "silver"
]

class Cars(Turtle):

    def __init__(self):      
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT