from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet_color = screen.textinput(title="Make your Bet", prompt="Who will win the race? Enter a color:")
user_bet = screen.numinput(title="Make your Bet", prompt="How much money would you Bet?")
print(f"Yoy have bet on {user_bet_color} color turtle.")
print(f"You have bet {user_bet}.")
colors = ["red", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100]
all_turtles = []
winning_color = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])

    all_turtles.append(new_turtle)

if user_bet_color:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color.append(turtle.pencolor())
            if winning_color[0] == user_bet_color:
                print(f"{winning_color[0]} color turtle has won. You won {user_bet * 5}!")
            else:
                print(f"{winning_color[0]} color turtle has won.You Lost")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
