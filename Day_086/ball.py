from turtle import Turtle

MOVE_DIST = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_dist *= -1

    def bounce_x(self):
        self.x_move_dist *= -1

    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10