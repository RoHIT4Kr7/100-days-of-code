from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.VALUE_1 = 0
        self.VALUE_2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.VALUE_1, align="center", font=("courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.VALUE_2, align="center", font=("courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def l_point(self):
        self.VALUE_1 += 1
        self.update_score()

    def r_point(self):
        self.VALUE_2 += 1
        self.update_score()

