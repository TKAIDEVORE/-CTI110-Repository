#TKAI DEVORE
#28APR24
#P4LAB1B
#INITIALS

import turtle

# Create a turtle object
t = turtle.Turtle()

# Set pen color and size
t.color("purple")
t.pensize(3)

# Draw initial "T"
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)


# Lift pen and move to draw next initial
t.penup()
t.goto(110, 0)
t.pendown()

# Draw initial "D"
t.right(90)
t.circle(50, -180)
t.left(90)
t.forward(100)

