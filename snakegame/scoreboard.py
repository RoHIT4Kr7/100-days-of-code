from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.VALUE = 0
        self.hideturtle()
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.VALUE}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.VALUE += 1
        self.clear()
        self.update_score()
