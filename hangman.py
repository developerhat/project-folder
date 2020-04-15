#Hangman game in Python
import random

words = ['apples', 'tesla', 'facebook', 'basketball', 'python']

word = random.choice(words)
print("Welcome to the hangman game! Let's begin..")

turns = 5

guess = ''
guess_word = ''


print('Guess the chars\n')
print('The word is: ', word)

while turns > 0:
    char = str(input('Enter a letter for the word: '))
    for char in word:
        if char == word:
            print(char, 'you got it! You won')
            break
        else:
            print('_')
            continue
            turns -=1
