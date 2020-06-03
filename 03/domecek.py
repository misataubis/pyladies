from turtle import forward, exitonclick, shape, left, right
from math import sqrt
shape('turtle')
X=100
for cislo in range(4):
    forward(X)
    left(90)
    forward(X)
    left(135)
    forward (sqrt(X**2+X**2))
    right(135)
    forward(X)
    right(45)
    forward (sqrt(X**2+X**2)/2)
    right(90)
    forward (sqrt(X**2+X**2)/2)
    right(135)
    forward(X)
    left(135)
    forward (sqrt(X**2+X**2))
    left(45)

exitonclick ()