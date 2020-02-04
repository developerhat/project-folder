#Guess the number

import random


integer = random.randint(1,5)
user_answer = 0 #Store variable

print("Welcome to the Guess the Number Program 2.0! ")
print("\n")

#Wow got this all on my own!! Keep working
while user_answer != integer:
    user_answer = int(input("I'm thinking of a number between 1 and 5, can you guess what it is? "))
    if user_answer < integer:
        print("Too low! Keep trying..")
    elif user_answer > integer:
        print("That's too high! Keep trying..")
    elif user_answer == integer:
        print("You got it mothafucka!! Yeee")
        print("The number was: ", integer)
