from turtle import Turtle, Screen
import random
screen=Screen()

def randomc():
    screen.colormode(255)
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)
    tim.color((color1, color2, color3))
    pickcolors=[color1, color2, color3]
    return pickcolors
tim=Turtle()
tim.pensize(1)
screen.setup (width=600, height=600, startx=0, starty=0)
screen.screensize(600,600)
tim.penup()
tim.goto(600, 600)
tim.speed(9)
tim.setheading(270)
tim.forward(50)
tim.right(90)
tim.forward(50)
times=0
while times!=10:
    times+=1
    for i in range(0,10):
        
        tim.forward(50)
        
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        
        tim.color(randomc())