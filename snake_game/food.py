from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") 
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.setposition(random_x, random_y)