import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_025/US_State_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day_025/US_State_Game/50_states.csv")
states_names = data["state"].to_list()

marco = turtle.Turtle()
marco.hideturtle()
marco.penup()

counter = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_names:
            if state is not guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day_025/US_State_Game/states_to_learn.csv")
        break

    if answer_state in states_names:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        marco.goto(int(state_data.x), int(state_data.y))
        marco.write(answer_state)


