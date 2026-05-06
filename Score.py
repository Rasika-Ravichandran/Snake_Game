from turtle import Turtle

class Score:
    def __init__(self):
        self.score = 0
        self.cutie = Turtle()
        self.cutie.goto(0,270)
        self.cutie.hideturtle()
        self.cutie.color("white")
        self.cutie.write(f"Score:{self.score}", align="center", font=("Courier", 24, "bold"))
    def increase_score(self):
        self.cutie.clear()
        self.score += 1
        self.cutie.write(f"Score:{self.score}", align="center", font=("Courier", 24, "bold"))
    def game_over(self):
        self.cutie.goto(0,0)
        self.cutie.write("GAMEOVER!!!", align="center", font=("Courier", 24, "bold"))

