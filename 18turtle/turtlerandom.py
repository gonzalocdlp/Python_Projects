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
    colors= ["blue","red","cyan", "purple", "green", "yellow", "orange"]
    lengthcolors=len(colors)-1
    pickcolors=colors[random.randint(0,lengthcolors)]
    return pickcolors
tim=Turtle()
screen= Screen()
tim.color('blue')
number=4
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

