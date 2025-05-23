import turtle
import pandas
from numpy.ma.core import append

screen=turtle.Screen()
screen.title("U.S. States Game")


screen.addshape("blank_states_img.gif")
screen.setup(height=491,width=725)
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses_states=[]
while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct",
                                    prompt="Whats the another state name?").title()

    print(answer_state)
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guesses_states]
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in all_states:
        guesses_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())




