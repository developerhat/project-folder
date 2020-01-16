#Random number generator
import random

print("\n")
print("Welcome to the Random Generator Program!")
print("This program will generate a random number. Your objective is to correctly guess this number")
print("\n")

user_answer = int(input("I'm thinking of a number between 1 and 5.. can you guess? "))

integer = random.randint(1,5)

if user_answer == integer:
    print("You got it! Your input: ", user_answer, "My input: ", integer)
else:
    print("Nope! Not that time. Your input: ", user_answer, "My input: ", integer)
