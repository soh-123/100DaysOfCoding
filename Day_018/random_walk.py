from turtle import Turtle, Screen
import random

marco = Turtle()
marco.pensize(10)
marco.speed("normal")
directions = [90, 180, 270, 0]


for _ in range(200):
    marco.color(random.random(), random.random(), random.random())
    marco.forward(30)
    marco.right(random.choice(directions))



screen = Screen()
screen.exitonclick()
