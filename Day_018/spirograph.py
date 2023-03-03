from turtle import Turtle, Screen
import random

marco = Turtle()
marco.speed("fastest")
marco.pensize(3)

screen = Screen()

screen.bgcolor("black")

for _ in range(36):
    marco.color(random.random(), random.random(), random.random())
    marco.circle(100)
    # marco.right(10)
    marco.setheading(marco.heading() + 10)


screen.exitonclick()
