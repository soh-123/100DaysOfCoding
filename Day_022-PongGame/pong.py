from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from dash import DashedDot
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()
dash_line = DashedDot()

screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")

screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_1) < 60 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.p1score()

    if ball.distance(player_2) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.p2score()
    #player one missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p2score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p1score()

        



screen.exitonclick()