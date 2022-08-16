from turtle import Turtle, circle
class Ball(Turtle):
    def __init__(self, a):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 10*a
        self.y_move = 10
        self.movespeed=0.1

    def moveBall(self):
        new_y= self.ycor()+self.y_move
        new_x= self.xcor()+self.x_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_move*=-1

    def hit(self):
        self.x_move*=-1
        self.y_move*=-1
        self.movespeed*=0.9