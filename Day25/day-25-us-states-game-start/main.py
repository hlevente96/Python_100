import turtle
from turtle import Turtle

import pandas as pd
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
FONT = ("Courier", 24, "normal")

guessed_states = set()
while len(guessed_states) < 50:
    state = screen.textinput(
        title=f"{len(guessed_states)}/50 States",
        prompt="What's another state's name?").title()
    if state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if state in all_states:
        turtle = Turtle()
        turtle.penup()
        turtle.color("black")
        turtle.hideturtle()
        found_state_info = df[df.state == state]
        turtle.goto(found_state_info.x.item(), found_state_info.y.item())
        turtle.write(state)
        guessed_states.add(state)



screen.exitonclick()