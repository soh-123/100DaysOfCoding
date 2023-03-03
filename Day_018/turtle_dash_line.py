from turtle import Turtle, Screen

marco = Turtle()

for _ in range(5):
    marco.forward(10)
    marco.penup()
    marco.forward(10)
    marco.pendown()

screen = Screen()
screen.exitonclick()
