from turtle import *

shape('turtle')

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
        
def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)
#triangle()

def polygon(sidelength=100, sides=4):
    angle=360/sides
    for i in range(sides):
        forward(sidelength)
        right(angle)

def star(sidelength=100, sides=4):
    angle=(360/sides)*2
    for i in range(sides):
        forward(sidelength)
        right(angle)

for a in range(60):
    star(a*10,5)
    right(10)
    forward(10)
#star(100,5)

#square(50)
#square(30)
#square()