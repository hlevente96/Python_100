from turtle import Screen
from slider import Slider
from ball import Ball
from scoreboard import Score
import time

screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

slider = Slider(350,0)
slider_2 = Slider(-350,0)
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(slider.up,"Up")
screen.onkey(slider.down, "Down")
screen.onkey(slider_2.up, "w")
screen.onkey(slider_2.down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() < -280 or 280 < ball.ycor():
        ball.bounce_y()
    if ball.distance(slider) < 50 and 320 < ball.xcor() or ball.distance(slider_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if 380 < ball.xcor():
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
screen.exitonclick()