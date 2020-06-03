from turtle import forward, exitonclick, shape, left, right
shape('turtle')
for x in range(30):
    left(20)
    for x in range(4):
        forward(50)
        left(90)

exitonclick()