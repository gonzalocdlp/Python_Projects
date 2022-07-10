from turtle import Turtle, Screen
import random


def randomc():
    screen.colormode(255)
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)
    tim.color((color1, color2, color3))
    pickcolors=[color1, color2, color3]
    return pickcolors
tim=Turtle()
screen= Screen()
tim.color('blue')
tim.pensize(1)
tim.speed(100900)
for move in range(1,360):
    pickcolors=randomc()
    tim.color(pickcolors)
    tim.right(3)
    tim.forward(1)
    tim.circle(200)
        
        

