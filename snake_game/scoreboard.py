from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 275)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 16, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER!", move=False, align="center", font=('Courier', 32, 'normal'))
        self.setposition(0, -30)
        self.write(f"Final score: {self.score}", move=False, align="center", font=('Courier', 16, 'normal'))
        