from turtle import Turtle, Screen
import time

screen= Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()
def move_forward():
    snakebody[0].forward(10)

def turn_right():
    snakebody[0].setheading(0)
    snakebody[0].forward(10)
def turn_left():
    snakebody[0].setheading(180)
    snakebody[0].forward(10)
def turn_down():
    snakebody[0].setheading(270)
    snakebody[0].forward(10)
def turn_up():
    snakebody[0].setheading(90)
    snakebody[0].forward(10)
def clear():
    snakebody[0].home()
    snakebody[0].clear()








snakebody=[]
for i in range(0,3):
    snake=Turtle()
    snake.shape('square')
    snake.color('white')
    snake.penup()
    snake.goto(x=i*-20,y=0)
    snakebody.append(snake)

gamePlaying= True
while gamePlaying:
    screen.update()
    time.sleep(0.1)
    for snak in range(len(snakebody)-1, 0 ,-1):
        new_x=snakebody[snak-1].xcor()
        new_y=snakebody[snak-1].ycor()
        snakebody[snak].goto(new_x,new_y)   
    screen.listen()
    screen.onkey(key="space", fun=move_forward)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="s", fun=turn_down)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="w", fun=turn_up)
    screen.onkey(key="z", fun=clear)





screen.exitonclick()