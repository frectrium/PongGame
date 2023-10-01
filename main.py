from screen import NewScreen, NewPaddle

scr = NewScreen()
paddle1 = NewPaddle(300, 0)
paddle2 = NewPaddle(-300, 0)

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

scr.screen.onkey(p1up, "Up")
scr.screen.onkey(p1dwn, "Down")
scr.screen.onkey(p2up, "w")
scr.screen.onkey(p2dwn, "s")


scr.screen.exitonclick()
