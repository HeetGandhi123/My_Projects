from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 280)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 280)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def user_1(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def user_2(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def winner_user1(self):
        self.goto(0,0)
        self.write("Winner is User1", align=ALIGN, font=FONT)

    def winner_user2(self):
        self.goto(0,0)
        self.write("Winner is User2", align=ALIGN, font=FONT)
