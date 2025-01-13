from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet", "Which turtle?")

colors = ["red","orange","yellow","green","blue","purple","black"]
turtles=[]
y = -150

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-230,y)
    y += 50
    turtles.append(turtle)

if user_bet:
    race = True

while race:
    for turtle in turtles:
        if 230 < turtle.xcor():
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"WON {winning_color}")
            else:
                print(f"LOST, your bet was: {user_bet}, the winner was: {winning_color}")
        turtle.forward(random.randint(0,10))

screen.exitonclick()