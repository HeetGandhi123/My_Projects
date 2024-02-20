import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        states_missed = [states for states in all_states if states not in guessed_states]
        # for states in all_states:
        #     if states not in guessed_states:
        #         states_missed.append(states)

        left_states = pd.DataFrame(states_missed)
        left_states.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = df[df['state'] == answer_state]
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(answer_state)
        guessed_states.append(answer_state)


