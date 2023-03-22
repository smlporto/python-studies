from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_paddle_1 = 0
        self.score_paddle_2 = 0
        self.color("white")
        self.penup()
        self.setposition(0, 265)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"{self.score_paddle_2} x {self.score_paddle_1}", move=False, align="center", font=('Courier', 24, 'bold'))


    def increase_score(self, paddle):
        if paddle == 1:
            self.score_paddle_1 += 1
        elif paddle == 2:
            self.score_paddle_2 += 1
        self.clear()
        self.update_scoreboard()