from random import randint

options = ['Rock', 'Paper', 'Scissors']

computer = options[randint(0,2)]

player = False
loop_placeholder = False
print("Welcome to the Rock, Paper, Scissors Game! ")

#Wow did this all on my own! 
while loop_placeholder == False:
    player = str(input("Rock, Paper, or Scissors? "))
    if player == computer:
        print("Tie! Try again")
    elif player == "Rock":
        if computer == "Paper":
            print('You lose! ', computer, 'covers', player)
        elif computer == 'Scissors':
            print("You win! ", player, 'smashes', computer)
        loop_placeholder = True
    elif player == "Scissors":
        if computer == "Paper":
            print('You win! ', player, 'cuts', computer)
        elif computer == 'Rock':
            print("You lose! ", computer, 'destroys', player)
        loop_placeholder = True
    elif player == 'Paper':
        if computer == "Scissors":
            print('You lose! ', computer, 'cuts', player)
        elif computer == 'Rock':
            print("You win! ", player, 'covers', computer)
        loop_placeholder = True
    else:
        print("That's not a valid play. Check spelling and try again!")
        loop_placeholder = False
