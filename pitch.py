import turtle
from turtle import Screen

t = turtle.Turtle()

def ScreenSetup():
    width = 900
    height = 700
    screen = Screen()
    screen.setup(width, height)
    # Setting up screen and background color
    turtle.title("Football")
    s = t.getscreen()
    turtle.bgcolor("#08F71D")


# White lanes
t.pen(pencolor="#FFFFFF", fillcolor="#FFFFFF", pensize=10, speed=8)

t.sety(-50)
t.circle(30)
t.left(90)
t.forward(450)
t.backward(800)
t.home()

t.up()
t.goto(380, -120)
t.down()

t.backward(100)
t.left(90)
t.forward(180)
t.right(90)
t.forward(100)

t.up()
t.goto(-391, -120)
t.down()

t.forward(100)
t.left(90)
t.forward(180)
t.left(90)
t.forward(100)
