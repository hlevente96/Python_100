from random import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        y = random.randint(-230,230)
        self.goto(300, y)

    def move(self, speed):
        self.setheading(180)
        self.forward(speed)
