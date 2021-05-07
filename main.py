import turtle
from pitch import *
from players import *
import time


stop = False


turtle.listen()
turtle.onkey(moveUp_1_A,'w')
turtle.onkey(moveDown_1_A,'s')
turtle.onkey(moveUp_2_A,'i')
turtle.onkey(moveDown_2_A,'k')

turtle.onkey(moveUp_1_B,'Up')
turtle.onkey(moveDown_1_B,'Down')
turtle.onkey(moveUp_2_B,'8')
turtle.onkey(moveDown_2_B,'2')


start = time.time()

while stop == False:
    turtle.update()
    duration = time.time() - start
    if duration > 60:
        stop = True


turtle.write("Game is OVER", align = 'center', font = ("Arial",24,"bold"))
turtle.ht()
turtle.done()