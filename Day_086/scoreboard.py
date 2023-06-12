from turtle import Turtle

FONT = ("Tahoma", 20, "normal")

try:
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = score
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     Highest Score: {self.highScore}     Lives: {self.lives}", align='center',font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore = self.score
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        self.clear()
        self.score = 0
        self.highScore = score
        self.update_scoreboard()
        open('highestScore.txt', 'w').write(str(self.highScore))


 

 

 

