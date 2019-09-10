###########################################################
# CIS 117 Python Programming: Lab #3
#
# Programming with Numbers and Strings, Execution Control,---
#--Iterator Structures and User Defined Functions

#
###########################################################

#usr/bin/python


#def main():
#grocery_bill = input('What is the total amount of your grocery bill? ')
#while True:
#    if grocery_bill.isdigit():
#        grocery_bill = int(grocery_bill)
#        print('you entered: ', grocery_bill)
#        break

def main():
    while True:
        grocery_bill = input('What is the total amount of your grocery bill? ')
        try:
            float(grocery_bill)
            return True
        except ValueError:
            return False
        if grocery_bill.isdigit():
            grocery_bill = float(grocery_bill)
            print('you entered: ',grocery_bill)
            break
        elif type(grocery_bill) == float():
            grocery_bill = float(grocery_bill)
            print('you entered: ',grocery_bill)
            break
    if grocery_bill <= 10:
        print('Sorry, you get no coupon!')
    elif grocery_bill > 10 and grocery_bill < 60:
        dollar_amnt = grocery_bill * 8 / 100.0
        print('You receive an 8% off coupon. Dollar amount: $',dollar_amnt)
    elif grocery_bill >= 60 and grocery_bill <= 150:
        dollar_amnt1 = grocery_bill * 10 / 100.0
        print('You receive a 10% off coupon. Dollar amount: $',dollar_amnt1)
    elif grocery_bill >= 150 and grocery_bill <= 210:
        dollar_amnt2 = grocery_bill * 12 / 100.0
        print('You receive a 12% off coupon. Dollar amount: $',dollar_amnt2)
    elif grocery_bill >= 210:
        dollar_amnt3 = grocery_bill * 14 / 100.0
        print('You receive a 14% off coupon. Dollar amount: $', dollar_amnt3)


for x in range(5):
    main()



#TRY USING ERICS CODE TO DO THIS!
# Will need to import over all other stuff
#def main1():
    """
    Asks user for grocery bill amount, then print coupon amount eligible.
    """
#    grocery_bill = -1
#    while grocery_bill < 0:
#        user_input = input('What is the total amount of your grocery bill? ' )
#        try:
#            grocery_bill = float(user_input)
#            break
#        except ValueError as e:
#            continue
#    print('you entered: ', grocery_bill)

#main1()

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
