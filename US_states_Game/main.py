import turtle
from extractcsv import StateData

screen = turtle.Screen()
state_data = StateData()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_turtles = {}


def display_text(x, y, text):
    if text not in state_turtles:
        state_turtles[text] = turtle.Turtle(visible=False)
    turtle_obj = state_turtles[text]
    turtle_obj.penup()
    turtle_obj.hideturtle()
    turtle_obj.goto(x, y)
    turtle_obj.write(text, align="center", font=("Arial", 12, "normal"))
    # turtle_obj.showturtle()


text_x = 0
text_y = 0
counter = 0
Game_on = True
while Game_on:
    answer_state = screen.textinput(title=f"{counter}/{len(state_data.list_of_states)} Guess the State",
                                    prompt="What's another state's name")
    if answer_state is None:
        break
    if answer_state.capitalize() in state_data.list_of_states:
        print(f"Correct! {answer_state} is one of the states.")
        counter += 1
        index = state_data.list_of_states.index(answer_state.capitalize())
        text_x = state_data.list_of_xc[index]
        text_y = state_data.list_of_yc[index]
        display_text(text_x, text_y, answer_state.capitalize())

    if counter == 50:
        Game_on = False
        print("God Player, a True Champ")
    else:
        print("Incorrect. Game over!")

turtle.mainloop()
