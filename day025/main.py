import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

state_list = data.state.to_list()

correct_answer = 0
correct_answer_list = []

while correct_answer != 50:
    answer_state = screen.textinput(title=f"{correct_answer}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # for state in state_list:
        #     if state not in correct_answer_list:
        #         missed_states.append(state)
        missed_states = [state for state in state_list if state not in correct_answer_list]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        row = data[data.state == answer_state]
        x = int(row.x)
        y = int(row.y)

        pen.goto(x, y)
        pen.write(answer_state)

        correct_answer += 1
        correct_answer_list.append(answer_state)
