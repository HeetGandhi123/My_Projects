from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-250, 250)
        self.write(f"level: {self.score}", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
