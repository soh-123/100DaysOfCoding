from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(f"{self.p1_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(f"{self.p2_score}", align="center", font=("Courier", 80, "normal"))

    def p1score(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2score(self):
        self.p2_score += 1
        self.update_scoreboard()