# Drawing and Loops
# Author: Audrey
# 14 October 2025



import turtle
import random

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightblue")
# TMNT - turtles

# create a turtle named mike
mike = turtle.Turtle()
mike.turtlesize(3) # set size
mike.shape("circle") # shape
mike.color("white") # colour

# move mike around

# mike.left(90)
# mike.speed(3)

# mike.circle(130)
# mike.penup()
# mike.goto(-135,125,)
# mike.pendown()
# mike.right(90)
# mike.circle(90)

# mike.penup()
# mike.goto(-135,50)
# mike.begin_fill()
# mike.circle(20)
# mike.shapesize(1)

# create a function to make cookies
def make_cookies(x:int, y:int):
# Cookie Making
# Set the colour of our choco chip cookie
    mike.color("brown")
# Draw a circle to represent our cookie
    mike.shapesize(0.5)
    mike.pu()
    mike.setheading(0) # mike points east
    mike.goto(-5 + x, -30 + y) # every goto needs a + counter
    mike.pd()
    mike.circle(30)
    # Put a chocolate chip at the top-right
    mike.pu()
    mike.goto(10 + x,10 + y)
    mike.stamp()
    # Put a chocolate chip at the bottom-right
    mike.goto(10 + x,-10 + y)
    mike.stamp()
    # Put a choco chip at the bottom-left
    mike.pd()
    mike.goto(-10 + x,10 + y)
    mike.stamp()
    # Choco chip at the top-left
    mike.goto(0 + x ,0 + y)
    mike.stamp()
    mike.goto(-10 + x,-10 + y)
    mike.stamp()

    # Make cookies randomly on the screen
    # make 500 of them
    for _ in range(500):
        x = random.randrange(-500,500)
        y = random.randrange(500,500)
        mike.speed(0)
        make_cookies(x, y)
# # make cookies in a diagonal line
make_cookies(0,0) # origin
make_cookies(100,100) # (100,100)
make_cookies(-100,-100)
make_cookies(-100,100)
make_cookies(100,-100)

# make cookies in an x
for counter in range(50):
    counter = counter * 50
    make_cookies(-counter, -counter) # need all 4 quadrants (-,- +,- +,+ -,+)
    make_cookies(counter, -counter)
    make_cookies(-counter, counter)
    make_cookies(counter, counter)
window.exitonclick()
