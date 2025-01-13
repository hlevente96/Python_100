from turtle import Turtle, Screen, colormode
import random
import colorgram
colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
timmy.setposition(-250,-250)

rgb = []
colors = colorgram.extract('picture.png',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r,g,b))

for y in range(-250,250,50):
    for x in range(-250,250,50):
        timmy.goto(x,y)
        timmy.dot(20, random.choice(rgb))


#for i in range(3,10):
#    for _ in range(i):
#        angle = 180-((i-2)*180/i)
#        timmy.forward(100)
#        timmy.right(angle)
#for _ in range(300):
#    color = tuple(random.randint(0,255) for _ in range(3))
#    print(color)
#    timmy.setheading(random.choice(degrees))
#    timmy.pencolor(color)
#    timmy.forward(30)
#for _ in range(45):
#    color = tuple(random.randint(0, 255) for _ in range(3))
#    timmy.circle(100)
#    timmy.pencolor(color)
#    timmy.right(8)

screen = Screen()
screen.exitonclick()