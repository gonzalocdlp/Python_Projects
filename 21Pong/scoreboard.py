from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.color("white")
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(coord)
        self.updateBoard()

    def updateBoard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Courier', 24, 'normal') ) 
        
    def scorePoint(self):
        self.score+=1
        self.updateBoard()

    def gameOver1(self):
        self.goto(0,0)
        self.write(f"Score: {self.score}. Game Over. Left wins", move=False, align='center', font=('Arial', 24, 'normal') ) 
    def gameOver2(self):
        self.goto(0,0)
        self.write(f"Score: {self.score}. Game Over. Right wins", move=False, align='center', font=('Arial', 24, 'normal') ) 