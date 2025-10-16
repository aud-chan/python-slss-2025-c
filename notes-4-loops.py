# Drawing and Loops
# Author: Audrey
# 14 October 2025



import turtle

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

# Make 100 cookies
for counter in range(100):
    counter = counter * 50

# Cookie Making
# Set the colour of our choco chip cookie
    mike.color("brown")
# Draw a circle to represent our cookie
    mike.shapesize(0.5)
    mike.pu()
    mike.setheading(0) #mike points east
    mike.goto(-5 + counter, -30 + counter)
    mike.pd()
    mike.circle(30)
    # Put a chocolate chip at the top-right
    mike.pu()
    mike.goto(10 + counter,10 + counter)
    mike.stamp()
    # Put a chocolate chip at the bottom-right
    mike.goto(10 + counter,-10 + counter)
    mike.stamp()
    # Put a choco chip at the bottom-left
    mike.pd()
    mike.goto(-10 + counter,10 + counter)
    mike.stamp()
    # Choco chip at the top-left
    mike.goto(0 + counter ,0 + counter)
    mike.stamp()
    mike.goto(-10 + counter,-10 + counter)
    mike.stamp()

window.exitonclick()
