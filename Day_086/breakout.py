from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from blocks import Bricks
from ball import Ball
import time

game_paused = False
is_game_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

scoreboard = Scoreboard()
player = Paddle((0, -270))
bricks = Bricks()
ball = Ball()

def brick_collision(bricks, ball):
    """Check for brick collision and eleminate the brick and bounce the ball somewhere else"""
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.clear()
            brick.goto(3000, 3000)
            bricks.bricks.remove(brick)
            scoreboard.increase_score()

            # detect collision from left and right
            if ball.xcor() < brick.left_wall:
                ball.bounce_x()
            elif ball.xcor() > brick.right_wall:
                ball.bounce_x()

            # detect collision from bottom and top
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce_y()
            elif ball.ycor() > brick.upper_wall:
                ball.bounce_y()
   

def wall_collision(ball):
    """Detect the four walls to collide and bounce back except for bottom as the user will lose"""
    if ball.ycor() > 250:
        ball.bounce_y()
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() < -270:
        ball.reset()
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:
            scoreboard.reset()

def paddle_collision(ball, player):
    """Detect whenever the ball collide with paddle from anyside to make the game smooth"""
    if ball.distance(player) < 60 and ball.ycor() < -250:   

        # If ball hits paddles right side it should go back to right
        if player.xcor() > 0:
            if ball.xcor() > player.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()
        # If ball hits paddles left side it should go back to left
        elif player.xcor() < 0:
            if ball.xcor() < player.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkey(key='space', fun=pause_game)

while is_game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    wall_collision(ball)
    brick_collision(bricks, ball)
    paddle_collision(ball, player)


screen.exitonclick()
