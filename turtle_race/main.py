from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

race_start = False

choice = screen.textinput("Make your bet", "Which turtle will win the race?\n(blue, orange, pink, green, red, purple)\nChoose a color:").lower()

colors = ["blue", "orange", "pink", "green", "red", "purple"]
turtles = []

y = -75
for turtle in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle)
    new_turtle.goto(-240, y)
    turtles.append(new_turtle)
    y += 30


if choice:
    race_start = True

while race_start:
    
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_start = False
            if choice == winner:
                print(f"Congrats! The {winner.upper()} turtle won the race!")
            else: 
                print(f"Oh oh! The {choice.upper()} turtle lost the race to the {winner.upper()} turtle!")

        speed = random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()