from turtle import Turtle, Screen

DISTANCE = 70

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.goto(position)

    def right(self):
        new_x_position = self.xcor() + DISTANCE
        if new_x_position < 380:
            self.goto(new_x_position, self.ycor())


    def left(self):
        new_x_position = self.xcor() - DISTANCE
        if new_x_position > -380:
            self.goto(new_x_position, self.ycor())