import turtle
import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("Guess the US States")
screen.setup(width=728, height=490)

image = '/Users/ayman/Desktop/Udemy_python/Day 25/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
score = 0
total_states = data['state'].to_list()
guessed_states = []

while True:
    guess = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state's name?").title()
    for state in data['state']:
        if guess == state:
            score += 1
            result = Turtle()
            result.hideturtle()
            result.penup()
            new_data = data[data['state'] == guess]
            x = int(new_data['x'].iloc[0])
            y = int(new_data['y'].iloc[0])
            result.goto(x=x, y=y)
            result.write(arg=f'{guess}', align='center', font=("Cambria", 12, "normal"))
            guessed_states.append(guess)

    
    if score == 50:
        message = Turtle()
        message.hideturtle()
        message.penup()
        message.write(arg='Congratulations!\nThank you for playing :)', align='center', font=("Cambria", 22, "bold"))
        break

    if guess == 'Exit':
        states_to_learn = []
        for state in total_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        with open('states_to_learn.csv', mode='w') as file:
            states_to_learn_str = ', '.join(states_to_learn)
            file.write(states_to_learn_str)
        break


