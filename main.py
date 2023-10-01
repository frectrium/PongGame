from turtle import Turtle
from screen import NewScreen, NewPaddle
from ball import Ball
from time import sleep

scr = NewScreen()
paddle1 = NewPaddle(300, 0, 'blue')
paddle2 = NewPaddle(-300, 0, 'red')

scr.screen.update()

scr.screen.listen()

def p1up():
    paddle1.pup()
    scr.screen.update()

def p2up():
    paddle2.pup()
    scr.screen.update()

def p1dwn():
    paddle1.pdown()
    scr.screen.update()

def p2dwn():
    paddle2.pdown()
    scr.screen.update()

def ballcollidedup():
    if ball.ycor() > 200:
        return True
    else:
        return False

def ballcollideddown():
    if ball.ycor() < -200:
        return True
    else:
        return False


scr.screen.onkey(p1up, "Up")
scr.screen.onkey(p1dwn, "Down")
scr.screen.onkey(p2up, "w")
scr.screen.onkey(p2dwn, "s")

ball = Ball()
scr.screen.update()

game_running = True

while game_running:
    sleep(0.1)
    scr.screen.update()
    ball.move()
    if ballcollidedup():
        ball.bouncedown()
    if ballcollideddown():
        ball.bounceup()
    if ball.xcor() > 275 and ball.xcor() < 285:
        if ball.ycor() > paddle1.ycor() - 50 and ball.ycor() < paddle1.ycor() + 50:
            ball.bounceleft()
    if ball.xcor() < -275 and ball.xcor() > -285:
        if ball.ycor() > paddle2.ycor() - 50 and ball.ycor() < paddle2.ycor() + 50:
            ball.bounceright()
    if ball.xcor() > 290 or ball.xcor() < -290:
        game_running = False

scr.screen.exitonclick()
