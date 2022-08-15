from turtle import Turtle
DISTANCE=20
class Snake:
    def __init__(self):
        self.snakebody=[]
        self.createSnake()
    
    def createSnake(self):
        for i in range(0,3):
            snake=Turtle()
            snake.shape('square')
            snake.color('white')
            snake.penup()
            snake.goto(x=i*-20,y=0)
            self.snakebody.append(snake)
    def move(self):
        for snak in range(len(self.snakebody)-1, 0 ,-1):
            new_x=self.snakebody[snak-1].xcor()
            new_y=self.snakebody[snak-1].ycor()
            self.snakebody[snak].goto(new_x,new_y)  
        self.snakebody[0].forward(DISTANCE) 