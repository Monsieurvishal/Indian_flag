import turtle 
obj=turtle.Turtle()

for i in range (24):#To represent All the 24 spokes of the Dharma chakra
    obj.forward(100)
    obj.penup()
    obj.setposition(0,0)
    obj.pendown()
    obj.right(15)
    # 360=24*15 
    
obj.setposition(0,-101)
obj.circle(102)
obj.penup()

#Costomize below code according to your system
#Orange Rectangle
obj.setposition(-450,150)
obj.pendown()
obj.fillcolor('Orange')
obj.begin_fill()
obj.forward(1000)
obj.left(90)
obj.forward(300)
obj.left(90)
obj.forward(1000)
obj.left(90)
obj.forward(300)
obj.end_fill()
obj.penup()

#Green Rectangle
obj.setposition(-450,-150)
obj.pendown()
obj.fillcolor('green')
obj.begin_fill()
obj.right(270)
obj.forward(1000)
obj.right(90)
obj.forward(300)
obj.right(90)
obj.forward(1000)
obj.right(90)
obj.forward(300)
obj.end_fill()
obj.penup()

turtle.done()
