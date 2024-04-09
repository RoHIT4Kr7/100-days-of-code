from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.make_turtle()

    def make_turtle(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.penup()
        new_y = self.ycor() + 20
        self.goto(x=0, y=new_y)

    def down(self):
        self.penup()
        new_y = self.ycor() - 20
        self.goto(x=0, y=new_y)
