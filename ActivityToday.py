#What're we doing today?
import random

choices = ['Play Ball!', 'Code! ','Read! ', 'Hang out!', 'Eat!', 'Play games!']
user_input = 'y'

while user_input == 'y':
    result = random.choice(choices)
    print('What should you do today, you ask? Here you go: ', result)
    user_input = str(input('Would you like to try again again? '))
    user_input = user_input.lower()
    if user_input == 'y':
        True
    elif user_input == 'n':
        False
