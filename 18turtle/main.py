from turtle import Turtle, Screen
tim=Turtle()
screen= Screen()
tim.shape('turtle')
tim.color('blue')
number=4
color=40
is_on="y"
screen.colormode(255)
tim.pencolor((240, 40, 40))
while is_on=='y':
    for i in range(0,number):
        tim.pencolor((color, color, 0))
        tim.right(360/number)
        tim.forward(100)
    if number<30:
        number+=1
        color=number*12
    else:
        is_on="n"
        















screen.exitonclick()