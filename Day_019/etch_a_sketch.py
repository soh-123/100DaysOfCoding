from turtle import *

marco = Turtle()
screen = Screen()

def move_forward():
    marco.forward(10)

def move_backward():
    marco.backward(10)

def turn_left():
    marco.left(10)

def turn_right():
    marco.right(10)


# def move_up():
#     marco.setheading(90)
#     marco.forward(10)

# def move_down():
#     marco.setheading(-90)
#     marco.forward(10)

# def move_left():
#     marco.setheading(180)
#     marco.forward(10)

# def move_right():
#     marco.forward(10)



screen.listen()
screen.onkey(key="c", fun=marco.reset)
screen.onkey(key="w", fun=turn_left)
screen.onkey(key="s", fun=turn_right)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="d", fun=move_forward)


screen.exitonclick()
