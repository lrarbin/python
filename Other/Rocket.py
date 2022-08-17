from typing import AbstractSet
import pgzrun

myrocket = Actor('rocket', center = (400, 500))

def draw():
    screen.clear()
    myrocket.draw()

def update():
    myrocket.y -=1

pgzrun.go()