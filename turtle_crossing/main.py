import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()

    car_manager.move()

    #Detect collision with car
    for car in car_manager.cars:
         if turtle.distance(car) < 20:
             game_is_on = False
             score.game_over()

    #Detect the cross
    if turtle.ycor() > 250:
        score.increase_level()
        turtle.reset_position()
        car_manager.increase_difficulty()
    

screen.exitonclick()