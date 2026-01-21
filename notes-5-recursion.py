# Recursion
# Author: Audrey
# 20 October

# Create a function that draws trees recursively
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)    # point the turtle up
t.penup()     # move the turtle a little lower
t.goto(0,-200)
t.color("brown")
t.width(8)
t.shape("arrow") # leaf shape

#  create a dictionary of leaf colours
LEAF_COLOURS = {
    "spring": "#efc3e6",
    "summer": "#4da167",
    "autumn": "#d36135",
    "winter": "#ddfff7",
}

def draw_tree(level: int, branch_length: float):
    """Draw a tree rcursively at a given level.
    level - the levels of branches
    branch_length - length of branches in pixel"""
    t.pd()
    # If the level is greater than zero
    if level > 0:
        # 1.Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(47)
        # 3. Turn right and draw a "smaller tree"
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.right(94)
        draw_tree(level - 1, branch_length * 0.8)
        # return to beginning
        t.left(47)
        t.backward(branch_length)
    else:
        # create a leaf
        t.color(LEAF_COLOURS["spring"])
        # t.color("#efc3e6") - harder to read
        t.stamp()
        t.color("brown")


def draw_complicated_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level.
    level - the levels of branches
    branch_length - length of branches in pixel"""
    t.pd()
    # If the level is greater than zero
    if level > 0:
        # 1.Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(47)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(47)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.right(47)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # return to beginning
        t.left(47)
        t.backward(branch_length)
        # branch straight up
    else: # base case
        # create a leaf
        t.color("green")
        t.stamp()
        t.color("brown")



def factorial(num: int) -> int:
    """Calculate the factorial of the given number recursively."""
    if num > 1:
       return num * factorial(num - 1)
    else:
        return 1


def fib(num: int) -> int:
    if num > 2:
        return fib(num - 2) + fib(num - 1)
    else:
        return 1
# print(fib(8))


# print(factorial(1))   # 1
# print(factorial(4))   # 24
# print(factorial(101)) # big num


# draw_complicated_tree(3,80)
draw_tree(3,100)
wn.exitonclick()
