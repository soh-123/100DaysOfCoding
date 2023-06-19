from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score_Board
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score_Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#when shnake collide with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#when snake collide with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset_snake()

#when snake collide with the tail
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            # is_game_on = False
            # scoreboard.game_over() 
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()