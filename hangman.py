#Hangman game in Python
import random

words = ['apples', 'tesla', 'facebook', 'basketball', 'python']

word = random.choice(words)
print("Welcome to the hangman game! Let's begin..")

guesses = ''

turns = 5

user_answer = 0 #Store variable

print('Guess the chars')

while turns > 0:
    failed = 0
    char = str(input('Test: '))
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed +=1
    if failed == 0:
        print("You won! The word is: ", word)
        break
        guess = str(input("Guess a char: "))
        guesses += guess
        if guess not in word:
            turns -= 1
            print("wrong!")
            print('You have,' + turns, 'left')
            if turns == 0:
                print("You lose!")
