from turtle import Turtle, Screen

screen = Screen()

#set height and width
screen.setup(500, 400)
user_bet = (screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color:"))
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -65, -30, 5, 40, 75]

for turtle_index in range(0,6):
    edgar = Turtle(shape="turtle")
    edgar.color(colours[turtle_index])
    edgar.penup()
    edgar.goto(x=-238, y=y_positions[turtle_index])



screen.exitonclick()