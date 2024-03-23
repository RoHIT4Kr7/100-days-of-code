from turtle import Turtle
X_CORD = 20
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        global X_CORD
        for _ in range(3):
            X_CORD -= 20
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.setposition(x=X_CORD, y=0)
            self.segments.append(tim)

    def add_segment(self):
        last_x_position = ((self.segments[-1]).xcor())
        last_y_position = (self.segments[-1]).ycor()
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.setposition(x=last_x_position, y=last_y_position)
        self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)


