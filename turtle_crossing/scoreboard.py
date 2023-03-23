from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.setposition(-290, 265)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER!", move=False, align="center", font=FONT)
        self.setposition(0, -30)
        self.write(f"Final score: {self.level}", move=False, align="center", font=("Courier", 16, "bold"))
        
