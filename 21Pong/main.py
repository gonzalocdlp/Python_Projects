from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen= Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
paddle=Paddle((350,0))
paddle2=Paddle((-350,0))
ball=Ball(1)
screen.tracer(0)
scoreL=Scoreboard((-200,250))
scoreR=Scoreboard((200,250))



screen.listen()
screen.onkey(paddle.goUp,"Up")
screen.onkey(paddle.goDown,"Down")
screen.onkey(paddle2.goUp,"w")
screen.onkey(paddle2.goDown,"s")
gameLive=True
while gameLive:
    time.sleep(ball.movespeed)
    screen.update()
    ball.moveBall()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce()
    if ball.distance(paddle) <60 and ball.xcor()>=340:
        ball.hit()
    if ball.distance(paddle2) <60 and ball.xcor()<=-340:
        ball.hit()
    if ball.xcor()>=420:
        scoreL.scorePoint()
        ball=Ball(-1)
    if ball.xcor()<=-420:
        scoreR.scorePoint()
        ball=Ball(1)


screen.exitonclick()
