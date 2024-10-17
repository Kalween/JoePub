import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S: States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.speed("fastest")
screen.setup(width=800, height=600, startx=2700, starty=200)

 
data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []




while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")          
        break
    if answer_state in state_list and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)





screen.exitonclick()
