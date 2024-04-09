import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.bgcolor("white")
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    car_manager.move_cars()
    car_manager.random_spawn()
    screen.update()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:  
        scoreboard.level_up()
        player.goto(STARTING_POSITION)
        car_manager.level_up()

screen.exitonclick()
