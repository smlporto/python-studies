import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil States Game")

screen.bgpic("blank_states_img.gif")

guessed = []
game_is_on = True
while game_is_on:
    states_list = pandas.read_csv("brazil_states.csv")

    states = states_list.state.to_list()

    answer = screen.textinput(f"Guess the state {len(guessed)}/{len(states)}", "What's another state's name? (exit to quit)").title()

    if answer == "Exit":
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)
        missing_data = pandas.DataFrame(missing)
        missing_data.to_csv("to_learn.csv")
        break
    if answer in states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = states_list[states_list.state == answer]
        t.setposition(int(state_info.x), int(state_info.y))
        t.write(answer)

