import turtle as t
from turtle import Screen
import random
timmy=t.Turtle()
colors=["deep sky blue","forest green","cyan","DarkOrchid","CornflowerBlue","IndianRed","wheat","SlateGray"]

timmy.speed(3)
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


screen=Screen()
screen.exitonclick()    