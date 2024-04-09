from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2.5)
        car.color(random.choice(COLORS))
        car.setheading(180)  # Set the initial direction of the car
        car.goto(300, random.randint(-250, 250))  # Spawn the car at a random position
        self.cars.append(car)

    def random_spawn(self):
        if random.randint(1, 6) == 1:  # Adjust probability as needed
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.move_speed *= 0.5
