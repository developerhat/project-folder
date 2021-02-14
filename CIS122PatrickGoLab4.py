#PatrickGoFunctions.py
#Author: Patrick Go
#Date last modified: 02/13/21
#Purpose: To demonstrate how to use functions

#Program uses: to become familiar with debugging process, recognizing syntax errors, using IDLE

#Assignment 4 - Functions

#2
def greet():
    user_name = str(input("What's your name? ")) #Take name from user, display name
    print("Hello, " + user_name + '!')

greet()


#3
def cube():
    int1 = int(input("Enter integer 1: ")) #Take input from user
    int2 = int(input("Enter integer 2: "))
    print(int1**int2) #Return cubed integers

cube()

#4
def auto1():
    auto_loan = int(input("Monthly car payment: "))
    insurance = int(input("Monthly insurance: "))
    gas = int(input("Monthly fuel costs: "))
    oil = int(input("Monthly oil cost: "))
    tires = int(input("Monthly tire cost "))
    maint = int(input("Monthly maintenance cost: "))
    monthly_cost = auto_loan + insurance + gas + oil + tires + maint
    print("Total monthly cost: ", monthly_cost)
    return monthly_cost


def auto2():
    monthly_cost = auto1()
    print("Total annual cost: ", monthly_cost * 12)

auto2()
