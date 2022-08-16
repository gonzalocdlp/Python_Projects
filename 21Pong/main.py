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
ball=Ball()
screen.tracer(0)
score=Scoreboard()



screen.listen()
screen.onkey(paddle.goUp,"Up")
screen.onkey(paddle.goDown,"Down")
screen.onkey(paddle2.goUp,"w")
screen.onkey(paddle2.goDown,"s")
gameLive=True
while gameLive:
    screen.update()
    time.sleep(0.1)
    ball.moveBall()
    if ball.ycor()==300 or ball.ycor()==-300:
        ball.bounce()
    if ball.distance(paddle) <10:
        ball.hit()
    if ball.distance(paddle2) <10:
        ball.hit()
    if ball.xcor()==350:
        score.gameOver1()
    if ball.xcor()==-350:
        score.gameOver2()


screen.exitonclick()
