from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_i = random.randint(1, 6)
        if random_i == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setposition(310, random.randint(-250, 250))
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)
        
    def increase_difficulty(self):
        self.car_speed += MOVE_INCREMENT
