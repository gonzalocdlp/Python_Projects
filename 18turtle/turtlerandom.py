from turtle import Turtle, Screen
import random
def randomd():
    directions=[0,90,180,270]
    picksides=directions[random.randint(0,3)]
    return picksides
def randomt():
    sides= ["left", "right"]
    pickturn=sides[random.randint(0,1)]
    return pickturn
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
tim.pensize(15)
tim.speed(9)
for i in range(1,1000):
    randomt()
    pickcolors=randomc()
    tim.color(pickcolors)
    picksides=randomd()
    if randomt()=='right':
        tim.right(picksides)
        tim.forward(30)
    if randomt()=='left':
        tim.left(picksides)
        tim.forward(30)

