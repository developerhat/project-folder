#Random number generator
import random

print("\n")
print("Welcome to the Random Generator Program!")
print("This program will generate a random number. Your objective is to correctly guess this number")
print("\n")

#Generate the integer here
integer = random.randint(1,5)
user_answer = 0 #Store variable

#Wow!! Got this on my own w no help!! holy shit!
while integer != user_answer:
    user_answer = int(input("I'm thinking of a number between 1 and 5.. can you guess? "))
    if user_answer == integer:
        print("You got it! Your input: ", user_answer, "My input: ", integer)
        True
    else:
        print("Nope! Not that time. Your input: ", user_answer, "My input: ", integer)


#NOT COMPLETE
#Added this 2nd portion because trying to add some function to
#Notify user their guess is too high, or too low
#All while handling exception 
while integer != user_answer:
    user_answer = int(input("I'm thinking of a number between 1 and 5.. can you guess? "))
    if user_answer == integer:
        print("You got it! Your input: ", user_answer, "My input: ", integer)
        True
    else:
        print("Nope! Not that time. Your input: ", user_answer, "My input: ", integer)
