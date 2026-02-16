from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()


    def refresh(self):
        randx = random.randint(-280,280)
        randy = random.randint(-280,280)
        self.goto(randx,randx)