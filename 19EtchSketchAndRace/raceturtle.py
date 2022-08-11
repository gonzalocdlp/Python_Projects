from turtle import Turtle, Screen
screen= Screen()
colors= ["red", "fuchsia" ,"gold", "pink", "black", "green"]
screen.setup(width=500, height=400)
screen.listen()
user_bet = screen.textinput(title="Make a bet", prompt=f"Pick a color of the turtle to win the race {colors}")
for i in range(0,6):
    tim= Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-250, y=-150+i*30)

screen.exitonclick()


