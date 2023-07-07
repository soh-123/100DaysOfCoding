from turtle import Turtle, Screen

IMAGE = "Day_094/img/alien.gif"

class Aliens():
    def __init__(self):
        self.screen = Screen()
        self.screen.addshape(IMAGE)
        self.y_start = 0
        self.y_end = 240
        
        self.alien_row = []
        self.create_all_lanes()
 
    def create_lane(self, y_cor):
        for i in range(-350, 350, 65):
            alien = Turtle(shape=IMAGE)
            alien.penup()
            alien.goto(i, y_cor)
            self.alien_row.append(alien)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 65):
            self.create_lane(i)