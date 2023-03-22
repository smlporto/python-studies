from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_1.up, "Up")
screen.onkeypress(paddle_1.down, "Down")
screen.onkeypress(paddle_2.up, "w")
screen.onkeypress(paddle_2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 330 or ball.distance(paddle_2) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Check goal
    if ball.xcor() > 400:
        scoreboard.increase_score(2)
        paddle_1.reset_position()
        paddle_2.reset_position()
        ball.reset_position()
    elif ball.xcor() < -400:
        scoreboard.increase_score(1)
        paddle_1.reset_position()
        paddle_2.reset_position()
        ball.reset_position()
screen.exitonclick()