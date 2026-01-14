import colorgram
import turtle as t
import random

colors = colorgram.extract('D:/python/!00 days project/100days-of-Python/Day 18/OIP.jpg', 100)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

timmy = t.Turtle()
t.colormode(255)
x= -200
y = -200
timmy.pensize(16)

for _ in range(10):
    timmy.penup()
    timmy.setpos(x, y)
    timmy.pendown()
    y += 50
    for _ in range(10):
        timmy.pencolor(random.choice(rgb_colors))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()



screen = t.Screen()
screen.exitonclick()

