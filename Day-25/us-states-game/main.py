import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
# Funciona solamente con ruta absoluta
image = "C:/Users/Guillermo/Documents/curso-100-DoP/\
ejercicios-100-days-of-code/Day-25/us-states-game/map.gif"
screen.register_shape(image)
turtle.shape(image)

states = pd.read_csv("C:/Users/Guillermo/Documents/curso-100-DoP/\
ejercicios-100-days-of-code/Day-25/us-states-game/50_states.csv")
states_list = states["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state name?")
    if answer_state != None:
        answer_state = answer_state.title()
    else:
        break

    if (answer_state in states_list) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        turtle.setposition(100,100)
        turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
    else:
        print("Incorrecto.")

print(guessed_states)
# state_info = states[states["state"] == answer_state]
# state_name = state_info["state"]
# state_x_coord = state_info["x"]
# state_y_coord = state_info["y"]
# print(f"{state_name}\n {state_x_coord}\n{state_y_coord}")

screen.exitonclick()