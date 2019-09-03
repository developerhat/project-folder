###########################################################
# CIS 117 Python Programming: Lab #2
#
# Arithmetic, Data Types, User Input, Importing Modules
#
###########################################################

#usr/bin/python

#Importing datetime module
from datetime import date

#Collecting last name from user
num_let = str(input('Hello! What is your last name? '))
#Setting num_let to number of digits user entered
#Number of digits in users last name
num_let = len(num_let)

#Requesting input from user
my_id = input('What is your student G number? ')
#Adding all digits given
my_id = sum(int(i) for i in my_id)

#Displaying num_let & my_id values to user
print('Student G Number added:', my_id)
print('Amount of letters in your last name: ', num_let)

#Calculating & printing expressions 1-9
expression1 = my_id/2
print('expression 1: ',expression1)

expression2 = my_id %2
print('expression 2: ',expression2)

expression3 = 2 + 3 + num_let
print('expression 3: ',expression3)

expression4 = my_id + num_let
print('expression 4: ',expression4)

expression5 = abs(num_let - my_id)
print('expression 5: ', expression5)

expression6 = my_id / num_let + 1100
print('expression 6: ',expression6)

expression7 = num_let % num_let, my_id * my_id
print('expression 7: ',expression7)

expression8 = 1
print('expression 8: ',expression8)

expression9 = round(3.15,1)
print('expression 9: ',expression9)

#Printing today's date
today = date.today()
print("Today's date is: ",today)

#Program output:

#Hello! What is your last name? go
#What is your student G number? 01037101
#Student G Number added: 13
#Amount of letters in your last name:  2
#expression 1:  6.5
#expression 2:  1
#expression 3:  7
#expression 4:  15
#expression 5:  11
#expression 6:  1106.5
#expression 7:  (0, 169)
#expression 8:  1
#expression 9:  3.1
#Today's date is:  2019-09-03
