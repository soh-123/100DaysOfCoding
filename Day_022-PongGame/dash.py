from turtle import Turtle

class DashedDot(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.left(90)
        self.penup()
        self.goto(0, -300)
        self.pensize(5)

        for _ in range(20):
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()