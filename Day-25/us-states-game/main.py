import turtle
import pandas as pd
from pandas.core.frame import DataFrame

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/Users/Guillermo/Documents/curso-100-DoP/\
ejercicios-100-days-of-code/Day-25/us-states-game/map.gif"
screen.register_shape(image)
turtle.shape(image)

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()

states = pd.read_csv("C:/Users/Guillermo/Documents/curso-100-DoP/\
ejercicios-100-days-of-code/Day-25/us-states-game/50_states.csv")
states_list = states["state"].to_list()
x_coord = states["x"].to_list()
y_coord = states["y"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state name?")
    if answer_state != None:
        answer_state = answer_state.title()
    else:
        break

    if answer_state == "Exit": break

    if (answer_state in states_list) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        writer_turtle.setposition(x_coord[states_list.index(answer_state)],
                                  y_coord[states_list.index(answer_state)])
        writer_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
    else:
        print("Incorrecto.")

for guessed_state in guessed_states:
    states_list.remove(guessed_state)

print(states_list)
states_to_learn = DataFrame(
    {"states": states_list}
)
states_to_learn.to_csv("C:/Users/Guillermo/Documents/curso-100-DoP/\
ejercicios-100-days-of-code/Day-25/us-states-game/States-to-Learn.csv", index=False)

# screen.exitonclick()