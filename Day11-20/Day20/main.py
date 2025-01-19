from turtle import Screen
import time

from scoreboard import Score
from snake import Snake
from food import Food

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    time.sleep(0.06)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    cond1 = snake.head.xcor() < -290
    cond2 = 290 < snake.head.xcor()
    cond3 = snake.head.ycor() < -290
    cond4 = 290 < snake.head.ycor()
    cond = [cond1, cond2, cond3, cond4]
    if any(cond):
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()