from turtle import Screen, Turtle
from scoreboard import Scoreboard
from aliens import Aliens
import time
import math

is_game_on = True
IMAGE = "Day_094/img/ship.gif"
SHIP_DISTANCE = 30

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Alien Invasion")
screen.tracer(0)


scoreboard = Scoreboard()
aliens = Aliens()

#------------------------------------SHIP-------------------------------------#
ship = Turtle()
ship.screen = Screen()
ship.screen.addshape(IMAGE)
ship.shape(IMAGE)
ship.penup()
ship.goto((0, -240))

def right():
    new_x_position = ship.xcor() + SHIP_DISTANCE
    if new_x_position < 380:
        ship.goto(new_x_position, ship.ycor())

def left():
    new_x_position = ship.xcor() - SHIP_DISTANCE
    if new_x_position > -380:
        ship.goto(new_x_position, ship.ycor())

#------------------------------------BULLET-------------------------------------#
bullet = Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.shapesize(stretch_wid=0.1, stretch_len=1)
bullet.speed(0)
bullet.setheading(90)
bullet.hideturtle()
bulletspeed = 10
#Define bullet state
#ready- ready to fire
#fire- bullet is firing
bulletstate = "ready"


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.setposition(ship.xcor(), ship.ycor() + 20)
        bullet.showturtle()
        # bullet.forward(bulletspeed)

def isCollision_alien_bullet(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False
    
#------------------------------------MAIN GAME-------------------------------------#
screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire_bullet, "space")
alien_speed = 0.5
alien_direction = -1
while is_game_on:
    screen.update()
    time.sleep(0.01)
    
    for alien in aliens.alien_row:
        x = alien.xcor()
        x += alien_speed * alien_direction
        alien.setx(x)

        # Check if aliens hit the left or right boundary
        if x > 370 or x < -370:
            for a in aliens.alien_row:
                y = a.ycor()
                y -= 20
                a.sety(y)
            alien_direction *= -1

        # Check if any alien reaches the player
        if ship.distance(alien) < 40 or alien.ycor() < -180:
            is_game_on = False
            screen.clear()
            screen.bgcolor("black")
            game_over = Turtle()
            game_over.speed(0)
            game_over.color("yellow")
            game_over.penup()
            game_over.hideturtle()
            game_over.goto(0, 0)
            game_over.write(f"Game Over\nYour score is {scoreboard.score}", align="center", font=("Arial", 24, "bold"))


    for alien in aliens.alien_row:
        if bulletstate == "fire" and isCollision_alien_bullet(alien, bullet):
            aliens.alien_row.remove(alien)
            bullet.hideturtle()
            alien.hideturtle()
            bulletstate = "ready"
            scoreboard.increase_score()


    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

screen.exitonclick()
