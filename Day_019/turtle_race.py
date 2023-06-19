from turtle import *
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500,height= 400)
user_bet = screen.textinput("Make your bet", "Who will win this race? enter a color")

color_list = ["salmon", "goldenrod", "red", "brown", "purple", "olive"]
y_cordinate = -100
all_turtle = []
for t in range(0,6):
    fstka = Turtle(shape="turtle")
    fstka.color(color_list[t])
    fstka.penup()
    fstka.goto(-230, y_cordinate)
    y_cordinate += 40
    all_turtle.append(fstka)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor()>230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning color is {winning_color}")
            else:
                print(f"You lose! The winning color is {winning_color}")
        random_move = random.randint(0, 10)
        t.forward(random_move)
    

screen.exitonclick()