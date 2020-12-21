#Guess the Number game


import random


rand_number = random.randint(1,5)

user_input = int(input("I'm thinking of a number between 1-5. Can you guess what it is? "))

user_attempts = 0

while user_attempts < 5:
    if user_input == rand_number:
        print("You got it right! Nice. ")
        break
    else:
        user_attempts += 1
        print("Oh no! You did not guess correctly. Attempts left: ", user_attempts)
        True
