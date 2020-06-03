from turtle import forward, exitonclick, shape, left, right
shape('turtle')
n = input(int("Zaděj číslo"))
p = (180-(180*(1-2/n)))
y = 200/n
for x in range(n):
    forward(y)
    left(p)
    


exitonclick ()