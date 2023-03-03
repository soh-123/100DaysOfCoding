from turtle import Turtle, Screen
import random

marco = Turtle()
marco.hideturtle()
screen = Screen()
screen.bgcolor("black")


marco.setheading(215)
marco.forward(280)
marco.setheading(0)
marco.speed("fastest")
marco.penup()
marco.hideturtle()

for _ in range(10):
    for _ in range(10):
        marco.dot(20, random.random(), random.random(), random.random())
        marco.forward(50)

    marco.setheading(90)
    marco.forward(50)
    marco.setheading(180)
    marco.forward(500)
    marco.setheading(0)
    
screen.exitonclick()
