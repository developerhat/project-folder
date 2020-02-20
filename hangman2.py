import random

words = ['b','a','s','s','k','e','t','b','a','l','l',]

word = random.choice(words)
print("Welcome to the hangman game! Let's begin..")

guess = ''

guess_word = []

turns = 5

print(word)

#We need a way for it to only do select LETTERS
while turns > 0:
    user_answer = str(input("Guess the chars: "))
    if user_answer not in word:
        print("Wrong! Attempts: ", turns)
        turns -= 1
    elif user_answer in word:
        print("That's right! Here's the word: ", word)
        break


def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word You need to guess has", len(word), "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)


def guessing():
    guess_taken = 1

    while guess_taken < 10:
        guess = input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was",         secretWord)
change()
guessing()
