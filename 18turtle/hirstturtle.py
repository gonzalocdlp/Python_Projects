from turtle import Turtle, Screen
import random
from PIL import Image
import colorgram
# rgb_colors=[]
# colors = colorgram.extract("18turtle\picart.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

colors=[(194, 0, 2), (37, 29, 32), (247, 228, 32), (39, 31, 21), (206, 73, 157), (18, 146, 43), (252, 224, 1), (119, 223, 251), (251, 154, 180), (6, 183, 240), (12, 230, 49), (235, 157, 37), (65, 34, 241), (165, 82, 41), (26, 33, 43), (13, 246, 16), (21, 40, 25), (216, 153, 22), (93, 113, 133), (189, 7, 4), (246, 252, 251), (2, 114, 67), (57, 173, 226),  (113, 68, 111), (198, 233, 246), (183, 175, 243), (249, 25, 10), (53, 40, 185)]

screen=Screen()
length=len(colors)-1
def randomc():
    screen.colormode(255)
    color1=random.randint(0,length)

    
    pickcolors= colors[color1]
    return pickcolors
tim=Turtle()
tim.pensize(1)
screen.setup (width=600, height=600, startx=0, starty=0)
screen.screensize(600,600)
tim.penup()

tim.speed(9)
x=50
times=0
while times!=10:
    times+=1
    for i in range(0,10):
        
        
        tim.forward(x)
        
        tim.dot(20)
        
        
        
        tim.color(randomc())
  
    tim.setheading(90)
    tim.forward(x)
    tim.setheading(180)
    tim.forward(x*10)
    tim.setheading(0)