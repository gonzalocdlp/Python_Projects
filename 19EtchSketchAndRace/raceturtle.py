from turtle import Turtle, Screen
import random
screen= Screen()
colors= ["red", "fuchsia" ,"gold", "pink", "black", "green"]
screen.setup(width=500, height=400)
screen.listen()
user_bet = screen.textinput(title="Make a bet", prompt=f"Pick a color of the turtle to win the race {colors}")
turtles=[]
for i in range(0,6):
    newTurtle= Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colors[i])
    newTurtle.goto(x=-250, y=-150+i*30)
    turtles.append(newTurtle)
while user_bet:
    for turtle in turtles:
        if turtle.xcor()>230:
            winningColor=turtle.pencolor()
            if winningColor==user_bet:
                print(f"congrats {winningColor} won. You win")
            else:
                print(f"{winningColor} is the winner. You lost")
            user_bet=False
        randmove= random.randint(0,20)
        turtle.forward(randmove)
screen.exitonclick()


