import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Car_Project")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

cars = []
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i%6 == 0:
        car = CarManager()
        car.create_car()
        cars.append(car)
    for car in cars:
        car.move(STARTING_MOVE_DISTANCE)
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()
    if 280 < player.ycor():
        score.increase()
        player.starting()
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    i += 1

screen.exitonclick()
