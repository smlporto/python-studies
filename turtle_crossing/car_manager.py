from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setposition(0, random.randint(-240, 240))

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.setposition(new_x, self.ycor())
