from turtle import *

pensize(3)
speed(0)
pencolor('red')
fillcolor('yellow')


# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)

for i in range(18):
    begin_fill()
    for j in range(4):
        fd(150)
        lt(90)
    end_fill()
    lt(20)

hideturtle()
done()

