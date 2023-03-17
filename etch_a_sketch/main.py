from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()


def move_forwards():
    pencil.fd(10)


def move_backwards():
    pencil.bk(10)


def move_right():
    pencil.rt(10)


def move_left():
    pencil.lt(10)


def clean_screen():
    pencil.setposition(0, 0)
    pencil.clear()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_right, 'd')
screen.onkey(move_left, 'a')
screen.onkey(move_backwards, 's')
screen.onkey(clean_screen, 'c')

screen.exitonclick()