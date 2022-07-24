from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

screen.listen()
def move_forward():
    tim.forward(10)

def turn_right():
    tim.setheading(0)
    tim.forward(10)
def turn_left():
    tim.setheading(180)
    tim.forward(10)
def turn_down():
    tim.setheading(270)
    tim.forward(10)
def turn_up():
    tim.setheading(90)
    tim.forward(10)
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=turn_down)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=turn_up)
screen.exitonclick()