from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=700, height= 700)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake= Snake()
food = Food()
food2 = Food()
scoreboard=Scoreboard()
gamePlaying= True
while gamePlaying:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scorePoint()
        snake.extend()
    if snake.head.distance(food2) < 15:
        food2.refresh()
        scoreboard.scorePoint()
        snake.extend()
    if snake.head.xcor()> 350 or snake.head.xcor()< -350 or snake.head.ycor()>350 or snake.head.ycor()< -350:
        scoreboard.gameOver()
        gamePlaying=False
    for snak in snake.snakebody[1:]:
            if snake.head.distance(snak)<8:
                scoreboard.gameOver()
                gamePlaying=False
    screen.listen()
    screen.onkey(key="space", fun=snake.move_forward)
    screen.onkey(key="d", fun=snake.turn_right)
    screen.onkey(key="s", fun=snake.turn_down)
    screen.onkey(key="a", fun=snake.turn_left)
    screen.onkey(key="w", fun=snake.turn_up)
    screen.onkey(key="z", fun=snake.clear)





screen.exitonclick()