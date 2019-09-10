###########################################################
# CIS 117 Python Programming: Lab #3
#
# Programming with Numbers and Strings, Execution Control,---
#--Iterator Structures and User Defined Functions

#
###########################################################

#usr/bin/python

#Defining main function
def main():
    """
    Ask user for grocery bill amount, then calculate & print coupon amount.
    """
    #While loop to begin program
    while True:
        user_input = input('What is the total amount of your grocery bill? ' )
        try:
            #Store user input as a float
            grocery_bill = float(user_input)
            #If input is negative, prompt user again
            if grocery_bill < 0:
                continue
            break
        except ValueError as e:
            continue
    print('you entered: ', round(grocery_bill, 2))
    #Processing user input below, depending on amount given
    if grocery_bill <= 10:
        print('Sorry, you get no coupon!')
    elif grocery_bill > 10 and grocery_bill < 60:
        #The calculation below converts percentage to decimal
        dollar_amnt = grocery_bill * 8 / 100.0
        #Round() is used to round value to 2 decimal places
        print('You receive an 8% off coupon. Amount: $',round(dollar_amnt, 2))
    elif grocery_bill >= 60 and grocery_bill <= 150:
        dollar_amnt1 = grocery_bill * 10 / 100.0
        print('You receive a 10% off coupon. Amount: $',round(dollar_amnt1, 2))
    elif grocery_bill >= 150 and grocery_bill <= 210:
        dollar_amnt2 = grocery_bill * 12 / 100.0
        print('You receive a 12% off coupon. Amount: $',round(dollar_amnt2, 2))
    elif grocery_bill >= 210:
        dollar_amnt3 = grocery_bill * 14 / 100.0
        print('You receive a 14% off coupon. Amount: $',round(dollar_amnt3, 2))


#For loop to execute function 5 times
for x in range(5):
    main()

#Program output:

#What is the total amount of your grocery bill? -2
#What is the total amount of your grocery bill? 30.35
#you entered:  30.35
#You receive an 8% off coupon. Amount: $ 2.43
#What is the total amount of your grocery bill? 80.88
#you entered:  80.88
#You receive a 10% off coupon. Amount: $ 8.09
#What is the total amount of your grocery bill? 171.33
#you entered:  171.33
#You receive a 12% off coupon. Amount: $ 20.56
#What is the total amount of your grocery bill? 222.33
#you entered:  222.33
#You receive a 14% off coupon. Amount: $ 31.13
#What is the total amount of your grocery bill? 8
#you entered:  8.0
#Sorry, you get no coupon!
