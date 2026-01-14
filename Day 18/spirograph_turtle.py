import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)



def spirograph_maker(no_of_gap):
    for _ in range(int(360 / no_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + no_of_gap)

spirograph_maker(5)
        



screen = t.Screen()
screen.exitonclick()