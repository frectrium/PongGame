from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('yellow')
        self.xshift = 10
        self.yshift = 10

    def move(self):
        self.goto(self.xcor() + self.xshift, self.ycor() + self.yshift)

    def bouncedown(self):
        self.yshift = -10

    def bounceup(self):
        self.yshift = 10

    def bounceleft(self):
        self.xshift = -10

    def bounceright(self):
        self.xshift = 10
