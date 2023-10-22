import turtle
import pandas as pd

# Initialize the Turtle screen and set the background image
screen = turtle.Screen()
screen.title("U.S States Game")
screen.bgpic("blank_states_img.gif")

# Create a Turtle object
t = turtle.Turtle()
t.penup()

# Load state data from CSV file
data = pd.read_csv("50_states.csv")
all_states = data["state"].str.title().tolist()

# Initialize variables
states_correct = 0
answers = []
missed_states = []

while states_correct < 50:
    answer_state = screen.textinput(title=f"{states_correct}/50 states correct", prompt="What's another state's name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        # Get the coordinates of the state
        state_data = data[data["state"].str.title() == answer_state]
        x, y = float(state_data["x"]), float(state_data["y"])

        # Go to the state's location and display the state name
        t.goto(x, y)
        t.write(answer_state, align="center", font=("Arial", 7, "normal"))

        states_correct += 1
        answers.append(answer_state)
    else:
        print("Incorrect state")

# Find missed states
missed_states = [state for state in all_states if state not in answers]

# Save missed states to a CSV file
missed_states_df = pd.DataFrame({"Missed States": missed_states})
missed_states_df.to_csv("Missed_States.csv", index=False)

# Close the Turtle graphics window
turtle.done()
