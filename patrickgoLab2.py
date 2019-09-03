###########################################################
# CIS 117 Python Programming: Lab #2
#
# Arithmetic, Data Types, User Input, Importing Modules
#
###########################################################

#usr/bin/python
from datetime import date

num_let = str(input('Hello! What is your last name? '))

#my_id = int(input('What is your student G number? '))

num_let = len(num_let)

def sumID():
    my_id = input('What is your student G number? ')
    for i in my_id:
        if i.isdigit():
            return sum(i)

sumID()

today = date.today()
print(today)
