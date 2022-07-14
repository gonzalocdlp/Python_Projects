from turtle import Turtle, Screen
import random
from PIL import Image
import colorgram
art= Image.open("18turtle\picart.jpg")
colors = ["blue", "red", "green", "cyan", "purple", "orange"]
screen=Screen()

def randomc():
    screen.colormode(255)
    color1=random.randint(0,5)

    
    pickcolors= colors[color1]
    return pickcolors
tim=Turtle()
tim.pensize(1)
screen.setup (width=600, height=600, startx=0, starty=0)
screen.screensize(600,600)
tim.penup()

tim.speed(9)

times=0
while times!=10:
    times+=1
    for i in range(0,10):
        
        
        
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.forward(80)
        
        tim.color(randomc())
    if times%2==0:
        tim.left(90)
        tim.forward(80)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(80)
        tim.right(90)