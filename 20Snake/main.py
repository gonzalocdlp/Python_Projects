from turtle import Turtle, Screen

screen= Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snakebody=[]
for i in range(0,3):
    snake=Turtle()
    snake.shape('square')
    snake.color('white')
    snake.penup()
    snake.goto(x=i*-20,y=0)
    snakebody.append(snake)
screen.update()
gamePlaying= True
while gamePlaying:
    for snak in snakebody:
        snak.forward(20)




screen.exitonclick()