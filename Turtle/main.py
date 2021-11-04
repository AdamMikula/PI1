import random
import turtle
"""
t = turtle.Turtle()

t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.penup()
t.forward(150)
t.pendown()
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(180)
t.penup()
t.forward(300)
t.pendown()

def stvorec(dlzkaA):
    for i in range(4):
        t.forward(dlzkaA)
        t.right(90)
def stupen(stupenA):
    for i in range(3):
        stvorec(100)
        t.left(stupenA)
stupen(30)
"""




from random import randrange, uniform

randrange(-10,500)
uniform(-10,500)
print(randrange)

t = turtle.Turtle()
t.penup()
t.setpos(-10, 30)
t.pendown()

t.position_Y = random.randrange(10, 500)
t.position_X = random.randrange(10, 500)



def trojuhlnik(dlzkaA):
    for i in range(random.randrange(3, 15)):
        t.forward(dlzkaA)
        t.left(120)
trojuhlnik(randrange(50, 100))
t.penup()
t.setpos(-100, 100)
t.pendown()

t.position_Y = random.randrange(-100, 100)
t.position_X = random.randrange(-100, 100)



def stvorec(dlzkaB):
    for i in range(random.randrange(3, 15)):
        t.forward(dlzkaB)
        t.left(90)
stvorec(random.randrange(50, 100))












turtle.exitonclick()
