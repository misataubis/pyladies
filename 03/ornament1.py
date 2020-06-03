from turtle import forward, exitonclick, shape, left, right
shape('turtle')
n = 7
delka = 5
p = (180-(180*(1-2/n)))
left(p)
for x in range(190):
    forward(delka)
    left(p)
    delka = delka + 1





    


exitonclick ()