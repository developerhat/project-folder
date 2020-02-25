#Python hangman game

import random
words = ['subaru', 'culture', 'calabasas', 'honda', 'patek']
livesRemaining = 14
#livesRemaining = (int)livesRemaining
guessedLetters = ''

def pickaword():
	wordPosition = random.randint(0, len(words) - 1)
	return words[wordPosition]

def play():
	livesRemaining = 14
	word=pickaword()
	while True:
		guess= getGuess(word)
		if processGuess(guess, word):
			print('Congratulations! You won! ')
			break
		if processGuess <= int(livesRemaining): #Double check this line
			print('Oh no! You just got hung!')
			print('The word was: ' + word)
			break

def getGuess(word):
	printWord(word)
	print('Lives Remaining: ' + str(livesRemaining))
	guess = input('Give me a letter: ')
	return guess

def printWord(word):
	displayWord = ''
	for letter in word:
		if guessedLetters.find(letter) > -1:
			# Will do if letter found
			displayWord = displayWord + letter
		else:
			#Will do if letter not found
			displayWord = displayWord + '-'
			print(displayWord)

def processGuess(guess, word):
	if len(guess) > 1 and len(guess) == len(word):
		return wholewordguess(guess, word)
	else:
		return single_letter_guess(guess, word)

def wholewordguess(guess, word):
	global livesRemaining
	if guess.lower() == word.lower():
		return
		#the word guessed is right, what should be returned? Check this^^
	else:
		livesRemaining = livesRemaining-1
		#^^Check this
	return False

def single_letter_guess(guess, word):
	global guessedLetters
	#global livesRemaining
	if word.find(guess) == -1:
		#	 letter guess was incorrect
		livesRemaining =- 1
		#the above line of code is wrong, can you see where?
		guessedLetters = guessedLetters + guess.lower()
	if all_letters_guessed(word):
		return True
	return False


def all_letters_guessed(word):
	for letter in word:
		if guessedLetters.find(letter.lower()) == -1:
			return False
	return True

play()
