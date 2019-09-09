###########################################################
# CIS 117 Python Programming: Lab #3
#
# Programming with Numbers and Strings, Execution Control,---
#--Iterator Structures and User Defined Functions

#
###########################################################

#usr/bin/python


#def main():
grocery_bill = input('What is the total amount of your grocery bill? ')
while True:
    if grocery_bill.isdigit():
        grocery_bill = int(grocery_bill)
        print('you entered: ', grocery_bill)
        break




#def main():
#grocery_bill = 0
#while True:
#	   user_input = input('What is the total amount of your grocery bill? ')
#	   try:
#	       grocery_bill = float(user_input)
#	   except ValueError as e:
#	       continue
#	       break

#print('you entered: ', grocery_bill)

#main()
