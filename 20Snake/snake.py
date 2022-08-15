from turtle import Turtle
DISTANCE=20
class Snake:
    def __init__(self):
        self.snakebody=[]
        self.createSnake()
        self.head =self.snakebody[0]
    
    def createSnake(self):
        for i in range(0,3):
            position= i*-20,0
            self.addSegment(position)
            
    def addSegment(self, position):
        snake=Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakebody.append(snake)        
    def extend(self):
        self.addSegment(self.snakebody[-1].position())

    def move(self):
        for snak in range(len(self.snakebody)-1, 0 ,-1):
            new_x=self.snakebody[snak-1].xcor()
            new_y=self.snakebody[snak-1].ycor()
            self.snakebody[snak].goto(new_x,new_y)  
        self.snakebody[0].forward(DISTANCE) 

    def move_forward(self):
        self.snakebody[0].forward(10)

    def turn_right(self):
        if self.snakebody[0].heading() != 180:
            self.snakebody[0].setheading(0)
    def turn_left(self):
        if self.snakebody[0].heading() != 0:
            self.snakebody[0].setheading(180)
    def turn_down(self):
        if self.snakebody[0].heading() != 90:
            self.snakebody[0].setheading(270)
    def turn_up(self):
        if self.snakebody[0].heading() != 270:
            self.snakebody[0].setheading(90)
    def clear(self):
        self.snakebody[0].home()
        self.snakebody[0].clear()