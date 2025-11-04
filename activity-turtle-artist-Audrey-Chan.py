# Turtle Artist
# Author:
# 28 October

import turtle
import random

# A one-of-a-kind drawing

wn = turtle.Screen()
t = turtle.Turtle()
t.color("yellow")
t.pensize(5)
wn.bgcolor("#364652")
t.speed(0)

# draw buildings
def draw_city (x: int, y: int):
    t.pu()
    t.left(90)
    t.goto(-600 + x ,-600 + y)
    t.pd()
    t.forward(600)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(600)
    t.pu()
    t.goto(-200 + x, -600 + y)
    t.pd()
    t.right(180)
    t.forward(300)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(300)
    t.pu()
    t.goto(100 + x,-600 + y)
    t.pd()
    t.right(180)
    t.forward(450)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(450)
    t.pu()
    t.goto(400 + x, -600 + y)
    t.pd()
    t.right(180)
    t.forward(600)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(600)
    t.pu()
    t.goto(-575 + x, -575 + y)
    t.pd()
    t.right(180)

    # draw windows
    for _ in range(5):
        for _ in range (4):
            t.pendown()
            t.forward(85)
            t.right(90)

        t.penup()
        # move up to the next window
        t.forward(85 + 30) # 30 is the gap between the windows

    t.goto(-465 + x, -575 + y)
    for _ in range(5):
        t.begin_fill()
        for _ in range (4):
             t.pendown()
             t.forward(85)
             t.right(90)
             t.end_fill()


        t.penup()
             # move up to the next window
        t.forward(85 + 30) # 30 is the gap between the windows

    t.goto(-180 + x, -590 + y)
    for _ in range(3):
        for _ in range (4):
                 t.pendown()
                 t.forward(50)
                 t.right(90)

        t.penup()
                 # move up to the next window
        t.forward(85 + 20) # 30 is the gap between the windows

    t.goto(-115 + x, -590 + y)
    for _ in range(3):
        for _ in range (4):
            t.pendown()
            t.forward(50)
            t.right(90)

        t.penup()
                     # move up to the next window
        t.forward(85 + 20) # 30 is the gap between the windows

    t.goto(115 + x, -580 + y)
    for _ in range(4):
        for _ in range (4):
            t.pendown()
            t.forward(70)
            t.right(90)

        t.penup()
         # move up to the next window
        t.forward(85 + 28) # 30 is the gap between the windows

    t.goto(210 + x, -580 + y)
    for _ in range(4):
        for _ in range (4):
            t.pendown()
            t.forward(70)
            t.right(90)

        t.penup()
         # move up to the next window
        t.forward(85 + 28) # 30 is the gap between the windows

    t.goto(420 + x, -575 + y)
    for _ in range(5):
       for _ in range (4):
           t.pendown()
           t.forward(78)
           t.right(90)

       t.penup()
       # move up to the next window
       t.forward(85 + 30) # 30 is the gap between the windows

    t.goto(510 + x, -575 + y)
    for _ in range(5):
       for _ in range (4):
            t.pendown()
            t.forward(78)
            t.right(90)

       t.penup()
            # move up to the next window
       t.forward(85 + 30) # 30 is the gap between the windows


t.pd()
    # draw stars
def draw_star(level: int):
    t.goto(-300,500)
    t.pd()
    if level == 0:
        return
    for _ in range (3):
        x = random.randrange(-600,600)
        y = random.randrange(200,500)
        draw_star(level - 1)
        t.dot(10)
        t.pencolor("white")
        t.penup()
        t.goto(x,y)
        t.pu()


draw_city(3,100)
draw_star(4)

wn.exitonclick()
