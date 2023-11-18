from turtle import *

bgcolor('black')
pencolor('yellow')
speed(0)
pensize(3)
fillcolor('red')
begin_fill()
for j in range(20):
    for i in range(20):
        fd(40)
        rt(18)
    fd(20)    
    rt(18)    
end_fill()       
    
hideturtle()    
done()    