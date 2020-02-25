#Hangman 3.0

import random

word = random.choice(['tesla','apple', 'basketball'])

guessed = []
wrong = []

tries = 7

while tries > 0:

    out =''
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        print('You guessed:', word)
        break

    print('Guess a letter in the word:', out)

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print('yup')
        guessed.append(guess)
        tries = tries - 1
    else:
        print("NAH")
        tries = tries - 1
        wrong.append(guess)

if tries:
    print('You guessed: ', word)
else:
    print("Almost! The word was: ", word)
