#Python 3.4.3, MAC OSX (Latest)
#Hangman Game

import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")

WORDS = ("APPLE", "ORACLE", "MIMO", "TESLA")
word = random.choice(WORDS)
POSITIVE_SAYINGS = ("Well done!", "Awesome!", "You Legend!")
MAX_WRONG = len(word) - 1
so_far = ("-") * len(word)
used = []
wrong = 0

print("\t \t Welcome to Hangman!")
print()
input("Press Enter to START: ")

while wrong < MAX_WRONG and so_far != word:
    print()
    print(HANGMAN[wrong])
    print("Word so far: ", so_far)
    print("Letters used: ", used)

    guess = input("Guess a letter: ").upper()
    sleep(1) # Time delay - allows userfriendly reading
    print()

    while guess in used:
        print("Try again... You've already used this letter")
        guess = input("Guess a letter: ").upper()
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS),"...Updating word so far...")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new

    else:
        print("INCORRECT! Try again!")
        wrong += 1

print("Calculating result...")
sleep(1)
if wrong == MAX_WRONG:
    print("UNLUCKY! Better luck next time!")

else:
    print("WINNER! Congratulations!")

print()
print()
input("Press Enter to Leave: ")
