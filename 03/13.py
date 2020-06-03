from turtle import forward, exitonclick, shape, left, right, pendown, penup, goto, speed
from random import randrange
shape('turtle')
pX = 0
pY = 0
pQ = 0
speed(0)
for i in range(200):
    pX = -300 + randrange(600)
    pY = -300 + randrange(600)
    pQ = 4 + randrange(5)
    penup()
    goto(pX, pY)
    pendown()
    for i in range(5):
        forward(pQ)
        right(144)

    


exitonclick ()