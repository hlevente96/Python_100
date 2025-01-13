from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)
def clear():
    tim.clear()
    tim.penup()
    tim.setposition(0,0)
    tim.pendown()
def backward():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)

screen.listen()
screen.onkey(forward, "w")
screen.onkey(clear, "c")
screen.onkey(backward, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")

screen.exitonclick()