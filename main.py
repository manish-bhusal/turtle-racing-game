import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)

is_game_start = False

all_turtles = []

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_start = True

while is_game_start:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            is_game_start = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(
                    f"You've lose! The {winning_color} turtle is the winner.")
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
