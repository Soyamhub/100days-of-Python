import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

directions = [0, 90, 180, 270]

timmy.pensize(5)
timmy.speed(10)

def random_move():
    for _ in range(200):
        timmy.pencolor(random_color())    
        timmy.forward(20)
        timmy.setheading(random.choice(directions))
    

random_move()

    













screen = Screen()
screen.exitonclick()