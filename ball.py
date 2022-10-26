import math
from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.angle = 0
        self.ball_speed = 0
        self.traj_left = 0
        self.traj_right = 0
        self.angle_generator()
        self.to_center()

    def angle_generator(self):
        test1 = [j for j in range(128, 232)]
        test2 = [j2 for j2 in range(308, 53)]
        angles = [*test1, *test2]
        self.angle = choice(angles)
        self.setheading(self.angle)

    def to_center(self):
        self.angle_generator()
        self.goto(0, 0)
        self.ball_speed = 2
        self.traj_left = -350 * math.tan(self.angle * math.pi / 180)
        self.traj_right = 350 * math.tan(self.angle * math.pi / 180)

    def move(self):
        self.forward(self.ball_speed)

    def after_wall(self):
        self.angle = -self.angle
        self.setheading(self.angle)
        f = self.traj_left - self.ycor()
        self.traj_left = self.ycor() - f

        g = self.traj_right - self.ycor()
        self.traj_right = self.ycor() - g

    def wall_collision(self):
        b = 300 - 10
        return not (-b < self.ycor() < b)

    def score_left(self):
        return self.xcor() < -400

    def score_right(self):
        return self.xcor() > 400

    def paddle_angle(self, paddle):
        p = paddle.ycor()
        x = paddle.xcor()
        print(self.angle)

        # TODO: Fix the math behind
        if -16 < (self.ycor()-p) < 16:
            if x > 0:
                self.angle = abs(180 - self.angle/3)
            else:
                self.angle = 0 + (180-abs(self.angle))/3

            self.setheading(self.angle)
            self.ball_speed *= 1.01
            self.traj_left = self.ycor() - 680 * math.tan(self.angle * math.pi / 180)
            self.traj_right = self.ycor() + 680 * math.tan(self.angle * math.pi / 180)
        elif (self.ycor()-p) >= 16:
            if x > 0:
                self.angle = 150 - abs(self.angle)/2
            else:
                self.angle = 30 + (180-abs(self.angle))/2
            self.setheading(self.angle)
            self.ball_speed *= 1.03
            self.traj_left = self.ycor() - 680 * math.tan(self.angle * math.pi / 180)
            self.traj_right = self.ycor() + 680 * math.tan(self.angle * math.pi / 180)
        else:
            if x > 0:
                self.angle = 210 - abs(self.angle)/2
            else:
                self.angle = 330 - (180-abs(self.angle))/2
            self.setheading(self.angle)
            self.ball_speed *= 1.03
            self.traj_left = self.ycor() - 680 * math.tan(self.angle * math.pi / 180)
            self.traj_right = self.ycor() + 680 * math.tan(self.angle * math.pi / 180)




