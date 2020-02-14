#Dice rolling program
import random

user_input = 'y'

#Wow!! Got through this on my own pretty much
while user_input == 'y':
    dice = random.randint(1, 6)
    print('You rolled: ', dice)
    user_input = str(input('Would you like to roll again? '))
    user_input = user_input.lower()
    if user_input == 'y':
        True
    elif user_input == 'n':
        False
