#Guess the number program 3.0
import random

actual_number = random.randint(0, 10)


print("Hello! Welcome to the guess the number program! :) ")

user_guess = ''
attempts = 5

while user_guess != actual_number or attempts != 0:
    user_guess = int(input("I'm thinking of a number between 1-10. What's your guess?: "))
    if user_guess == actual_number:
        print("Hooray! You got it :) Good shit. Number: ", actual_number)
        break
    else:
        attempts = attempts - 1
        if attempts < 0:
            print("Try again! Number was: ", actual_number)
            break
        print("Uh oh! Try again. Attempts left: ", attempts)
        if user_guess < actual_number:
            print("You're too low! Higher..")
        elif user_guess > actual_number:
            print("Too high! Lower ")
