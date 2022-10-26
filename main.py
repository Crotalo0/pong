import time
import math

from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball


def dotted_line(t, start, end, div):
    x0, y0 = start[0], start[1]
    x1, y1 = end[0], end[1]
    d_p1_p2 = math.sqrt(math.pow((x0 - x1), 2) + math.pow((y0 - y1), 2))
    segment = d_p1_p2 / div
    t.setheading(270)
    t.pendown()
    for i in range(div):
        if i % 2 == 0:
            t.pendown()
        else:
            t.penup()
        t.forward(segment)


def field(t):
    t.penup()
    t.color("white")
    t.hideturtle()
    t.goto(-400, 300)
    t.pendown()
    t.goto(400, 300)
    t.goto(400, -300)
    t.goto(-400, -300)
    t.goto(-400, 300)
    t.penup()
    t.goto(0, 300)


# SCREEN DEF ________
screen = Screen()
screen.setup(height=660, width=860)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# ____________________

# BORDERS ___________
y = Turtle()
field(y)
dotted_line(y, (0, 300), (0, -300), 21)
# ____________________


paddle_left = Paddle(-350)
paddle_right = Paddle(350)

scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.01)
    paddle_right.cpu_move(ball.traj_right)
    paddle_right.cpu_move(ball.traj_right)

    ball.move()

    if ball.wall_collision():
        ball.after_wall()

    if ball.score_left():
        scoreboard.point_right()
        ball.to_center()

    if ball.score_right():
        scoreboard.point_left()
        ball.to_center()

    if (paddle_right.ycor() - 53 < ball.ycor() < paddle_right.ycor() + 53) and (330 < ball.xcor() < 350):
        ball.paddle_angle(paddle_right)

    elif (paddle_left.ycor() - 53 < ball.ycor() < paddle_left.ycor() + 53) and (-350 < ball.xcor() < -330):
        ball.paddle_angle(paddle_left)

screen.mainloop()
