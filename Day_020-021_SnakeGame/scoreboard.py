from turtle import *

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day_020-021_SnakeGame/data.txt") as data:
            self.high_score = int(data.read())
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day_020-021_SnakeGame/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
