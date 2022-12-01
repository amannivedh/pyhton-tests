from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="MAKE YOUR BET",prompt="Choose Turtle Color: ")
colors=["red","orange","yellow","blue","green","purple"]
y_pos=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:    
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"You Win!! The wining color is {winner}.")
            else:
                print(f"You Lose!! The winning color is {winner}.")    

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()