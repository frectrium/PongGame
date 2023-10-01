from turtle import Turtle, Screen

class NewScreen:
    """Creates a new screen for pong"""


    def __init__(self):
        self.screen = Screen()
        self.create_screen()


    def create_screen(self):
        """Sets up the screen with attributes"""

        self.screen.setup(height=480, width=640)
        self.screen.bgcolor('black')
        self.screen.title('PONG')
        self.screen.tracer(0)

        self.turt = Turtle()
        self.turt.speed('fastest')
        self.turt.goto(x=0, y=-240)
        self.turt.pensize(5)
        self.turt.setheading(90)
        self.turt.pencolor('white')
        self.turt.hideturtle()

        while self.turt.ycor() < 240:
            self.turt.forward(10)
            self.turt.penup()
            self.turt.forward(10)
            self.turt.pendown()

        self.screen.update()

class NewPaddle(Turtle):
    """Creates two new paddles"""

    def __init__(self, xcoord, ycoord):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcoord, ycoord)

    def pup(self):
        if self.ycor() < 180:
            self.goto(self.xcor(), self.ycor()+10)

    def pdown(self):
        if self.ycor() > -180:
            self.goto(self.xcor(), self.ycor()-10)
