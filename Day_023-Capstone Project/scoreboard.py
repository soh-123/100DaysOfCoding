from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        
    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

