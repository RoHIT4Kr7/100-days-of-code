from turtle import Turtle
FONT = ("Courier", 24, "normal")
counter = 1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = counter
        self.penup()
        self.goto(-200, 250)  # Adjust the position based on your preference
        self.hideturtle()
        self.goto(0, 250)  # Adjust the position based on your preference
        self.write("LEVEL 1", align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def level_up(self):
        self.counter += 1
        self.clear()  # Clear any previous text
        self.goto(0, 250)  # Adjust the position based on your preference
        self.write(f"LEVEL {self.counter}", align="center", font=("Courier", 12, "normal"))