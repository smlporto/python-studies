from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 16, 'normal'))
        self.setposition(self.xcor(), 250)
        self.write(f"High score: {self.high_score}", move=False, align="center", font=('Courier', 12, 'normal'))
        self.setposition(self.xcor(), 270)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(f"GAME OVER!", move=False, align="center", font=('Courier', 32, 'normal'))
    #     self.setposition(0, -30)
    #     self.write(f"Final score: {self.score}", move=False, align="center", font=('Courier', 16, 'normal'))
        