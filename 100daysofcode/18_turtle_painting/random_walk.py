import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

colors = ['red','green','blue','yellow','black','purple','orange']
random_walk = [tim.right,tim.left]
tim.pensize(10)
tim.speed(10)

def drawing(times):
    tim.forward(10)
    for _ in range(random.randint(1,4)):
        random.choice(random_walk)(90)
    tim.forward(10)

        
# for times in range(random.randint(50,200)):
#     drawing(times)
#     tim.color(random.choice(colors))


## Angelas solution

directions = [0, 90, 180, 270]

for _ in range(200):
    my_tuple = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    tim.color(my_tuple[0],my_tuple[1],my_tuple[2])
    tim.forward(30)
    tim.setheading(random.choice(directions))