import turtle as t
import random

def setup_turtle():
    screen = t.Screen()
    h = t.Turtle()
    screen.colormode(255)
    screen.bgcolor("lightgrey")
    h.pensize(2)
    h.speed("fastest")
    start_x = -screen.window_width() // 2 +50
    start_y = -screen.window_height() // 2 +50
    h.teleport(start_x,start_y)
    return screen, h

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

def draw_line(h,screen):
    height_offset = 50
    for i in range(15):
        height_offset += 120
        for i in range(17):
            h.color(change_color())
            h.dot(50)
            h.penup()
            h.forward(100)
            h.pendown()
            print(h.position())
        h.teleport(-screen.window_width() // 2 +50, -screen.window_height() // 2 + height_offset)


def main():
    screen, h= setup_turtle()
    draw_line(h,screen)
    draw_line(h,screen)
    screen.exitonclick()
    print(screen.canvheight)

if __name__ == "__main__":
    main()