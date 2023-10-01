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
        self.screen.exitonclick()
