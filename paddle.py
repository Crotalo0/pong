from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.setheading(90)
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 300:
            self.forward(10)

    def down(self):
        if self.ycor() > -300:
            self.backward(10)

    def cpu_move(self, ball_traj):
        if ball_traj > self.ycor() and self.ycor() < 300:
            self.forward(1.5)
        elif self.ycor() > -300:
            self.backward(1.5)




