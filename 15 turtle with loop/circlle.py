from turtle import *

speed(0)

# colors = ['red','yellow','green','blue','gray','aqua',
#           'red','yellow','green','blue','gray','aqua',
#           'red','yellow','green','blue','gray','aqua',
#           'red','yellow','green','blue','gray','aqua',
#           'red','yellow', 'green','blue','gray','aqua',
#           'red','yellow','green','blue','gray','aqua',]

colors = ['red','yellow','green','blue','gray','aqua']
pensize(3)

for i in range(36):
    pencolor(colors[i % 6])
    circle(100)
    rt(10)




hideturtle()
done()