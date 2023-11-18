from turtle import *


pensize(3)
speed(0)
pencolor('red')
fillcolor('yellow')


for i in range(18):
    begin_fill()
    for j in range(3):
        fd(150)
        rt(120)
        circle(10)
    end_fill()
    lt(20)

hideturtle()
done()