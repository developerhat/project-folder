#Hangman game

import random

word = random.choice(['Subaru','Tesla','Honda','BMW'])

guessed_letters = []
attempt_number = 7
print(word)


while attempt_number <= 7:
    user_input = str(input('Input a letter: '))
    if user_input in word:
        print("You got it!")
    else:
        attempt_number -= 1
        print("Nope! Attempts left: ", attempt_number)
