from turtle import Turtle, Screen
import time
from snake import Snake

screen= Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake= Snake()
screen.listen()
def move_forward():
    snake.snakebody[0].forward(10)

def turn_right():
    snake.snakebody[0].setheading(0)
    snake.snakebody[0].forward(10)
def turn_left():
    snake.snakebody[0].setheading(180)
    snake.snakebody[0].forward(10)
def turn_down():
    snake.snakebody[0].setheading(270)
    snake.snakebody[0].forward(10)
def turn_up():
    snake.snakebody[0].setheading(90)
    snake.snakebody[0].forward(10)
def clear():
    snake.snakebody[0].home()
    snake.snakebody[0].clear()











gamePlaying= True
while gamePlaying:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    screen.listen()
    screen.onkey(key="space", fun=move_forward)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="s", fun=turn_down)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="w", fun=turn_up)
    screen.onkey(key="z", fun=clear)





screen.exitonclick()