import turtle
import math
import random
scr = turtle.Screen()
scr.bgcolor('black')
turtle.pensize(3)
turtle.shape('turtle')
turtle.color('white')
turtle.penup()
turtle.setposition(-100,0)
turtle.pendown()

colors = ['white','blue','red','yellow','lightgreen','pink','lightyellow']
def octagon(lenght) :
    for k in range(8) :
        turtle.color(random.choice(colors))
        turtle.forward(lenght)
        turtle.left(45)
def space(y) :
    turtle.penup()
    turtle.forward(y)
    turtle.pendown()
    
def one(x) :
    turtle.left(90)
    turtle.forward(x)
    
def two(x) :
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x)
    
def three(x) :
    for i in range(2) :
        
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x/2)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(180)
        
def star(size) :
    for i in range(5) :
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.right(144)
        
turtle.speed(50)
#run them each seperatly

#1

'''
for i in range(4) :
    turtle.forward(100)
    turtle.right(90)
    


#2

for j in range(3) :
    turtle.right(120)
    turtle.forward(100)
    


#3
    
turtle.circle(100,360)

#4


for l in range(3) :
    turtle.begin_fill()
    for m in range(4) :
        turtle.forward(50)
        turtle.right(90)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    if l == 0 :
        turtle.color('black','red')
    elif l == 1 :
        turtle.color('black','blue')
    elif l == 2 :
        turtle.color('black','pink')
    turtle.end_fill()


#5


star(100)
            
    

#6

one(100)
turtle.right(90)
space(50)
two(100)
space(50)
three(100)
#7

octagon(100)
    

#8
turtle.penup()
turtle.setposition(0,0)
turtle.pendown()
for l in range(12) :
    octagon(90)
    turtle.left(30)
    

#9

while True :
    turtle.forward(random.randint(0,100))
    turtle.right(random.randint(0,360))
    turtle.color(random.choice(colors))
'''
    
turtle.exitonclick()
