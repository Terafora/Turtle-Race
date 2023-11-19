from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(500, 400)
user_bet = (screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color:"))
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -65, -30, 5, 40, 75]
all_turtles = []


for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colours[turtle_index])
    t.penup()
    t.goto(x=-238, y=y_positions[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You lose! The {winning_colour} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

screen.exitonclick()