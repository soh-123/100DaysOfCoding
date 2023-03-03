from turtle import Turtle, Screen
import random

marco = Turtle()

def shape(lines):
    for _ in range(lines):
        marco.forward(100)
        marco.right(360/lines)

for shape_sides in range(3,11):
    
    marco.color(random.random(), random.random(), random.random())
    shape(shape_sides)

screen = Screen()
screen.exitonclick()
