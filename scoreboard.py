from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(align="center",arg=f"Score : {self.score}",font=("Arial", 12 , "normal"))
        self.hideturtle()
        
    def increse_score(self):
        self.score += 1
        self.clear()
        self.write(align="center",arg=f"Score : {self.score}",font=("Arial", 12 , "normal"))


    def game_over(self):    
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.write(align="center",arg="GAME OVER",font=("Arial", 12 , "normal"))
        

        
