import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif" #create own turtle shape(image)
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50", prompt="What's another state's name?").title()

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #row where state == answer_state
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) #/ (state_data.state.item())
    elif answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break








# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor) #get coordinates on screen click
# turtle.mainloop()


