from random import randint

options = ['Rock', 'Paper', 'Scissors']

computer = options[randint(0,2)]

retry = ''
player = ''
loop_placeholder = True
print("Welcome to the Rock, Paper, Scissors Game! ")

#Wow did this all on my own!
while loop_placeholder == True:
    player = str(input("Rock, Paper, or Scissors? "))
    if player == computer:
        print("Tie! Try again")
    elif player == "Rock":
        if computer == "Paper":
            print('You lose! ', computer, 'covers', player)
            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]
                loop_placeholder = True
            else:
                loop_placeholder = False

        elif computer == 'Scissors':
            print("You win! ", player, 'smashes', computer)

            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]
                loop_placeholder = True
            else:
                loop_placeholder = False
                print("Thank you for using the RPS 2.0 Program! :) ")
        #loop_placeholder = True
    elif player == "Scissors":
        if computer == "Paper":
            print('You win! ', player, 'cuts', computer)
            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]
                loop_placeholder = True
            else:
                loop_placeholder = False
                print("Thank you for using the RPS 2.0 Program! :) ")
        elif computer == 'Rock':
            print("You lose! ", computer, 'destroys', player)
            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]
                loop_placeholder = True
            else:
                loop_placeholder = False
                print("Thank you for using the RPS 2.0 Program! :) ")
        #loop_placeholder = True
    elif player == 'Paper':
        if computer == "Scissors":
            print('You lose! ', computer, 'cuts', player)
            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]

                loop_placeholder = True
            else:
                loop_placeholder = False
                print("Thank you for using the RPS 2.0 Program! :) ")

        elif computer == 'Rock':
            print("You win! ", player, 'covers', computer)
            retry = str(input('would you like to try again? Y/N: '))
            if retry.lower() == 'y':
                computer = options[randint(0,2)]
                loop_placeholder = True
            else:
                print("Thank you for using the RPS 2.0 Program! :) ")
                loop_placeholder = False
        #loop_placeholder = True
    else:
        print("That's not a valid play. Check spelling and try again!")
        loop_placeholder = False
