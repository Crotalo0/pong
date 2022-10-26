from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(2, 210)
        self.score_left = 0
        self.score_right = 0
        self.updater()

    def updater(self):
        self.write(f"{self.score_left}      {self.score_right}", align="center", font=("ArcadeClassic", 60, 'normal'))

    def point_left(self):
        self.score_left += 1
        self.clear()
        self.updater()

    def point_right(self):
        self.score_right += 1
        self.clear()
        self.updater()
