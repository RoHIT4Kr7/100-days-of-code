from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.make_paddle()

    def make_paddle(self):
        self.penup()
        self.goto(x=self.x_coordinate, y=self.y_coordinate)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.x_coordinate, y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.x_coordinate, y=new_y)




