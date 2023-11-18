from turtle import *


from turtle import *

speed(0)
colors = ['red','yellow','green','blue']
pensize(2)

for x in range(4):
    pencolor(colors[x % 4])
    for i in range(1,100,5):
        
        circle(i)
    rt(90)    
    
hideturtle()
done()