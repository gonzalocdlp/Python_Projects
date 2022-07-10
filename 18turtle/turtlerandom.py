from turtle import Turtle, Screen
import random
def randomt():
    sides= ["left", "right"]
    pickturn=sides[random.randint(0,1)]
    return pickturn
tim=Turtle()
screen= Screen()
tim.shape('turtle')
tim.color('blue')
number=4
tim.speed(2)
for i in range(1,100):
    randomt()
    if randomt()=='right':
        tim.right(random.randint(1,180))
        tim.forward(random.randint(1,40))
    if randomt()=='left':
        tim.left(random.randint(1,180))
        tim.forward(random.randint(1,40))

