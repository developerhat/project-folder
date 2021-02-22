#PatrickGo Assignment 5.py
#Author: Patrick Go
#Date last modified: 02/21/21
#Purpose: Functions with Return

#Program uses: Using functions to calculate given data & return a result

#Assignment 5 - Functions with Return


#Problem 1
def get_avg():
    lst_nums = [] #Declare empty list
    number_1 = int(input("Enter number: ")) #Get number from user
    lst_nums.append(number_1) #Add user input to list
    number_2 = int(input("Enter number: "))
    lst_nums.append(number_2)
    number_3 = int(input("Enter number: "))
    lst_nums.append(number_3)
    number_4 = int(input("Enter number: "))
    lst_nums.append(number_4)
    return 'first avg = ', sum(lst_nums) / len(lst_nums) #Calculate average
    #print('first avg = ', sum(lst_nums) / len(lst_nums)) #Calculate average

get_avg()


#Problem 2
def access():
    username = str(input("Enter username: ")) #Get user name
    password = input("Enter password: ") #Get password
    return username, password #Return back to caller
    #print(username, password)
access()

#Problem 3
def feet_to_inches():
    feet = int(input("Feet: "))
    return feet * 12 #Return feet x 12 to convert to inches
    #print(feet * 12)
feet_to_inches()

#Problem 4
def insurance():
    cost = int(input("Enter the value of your home or building: "))
    return 'You will need to purchase $',cost * 0.8,'of insurance' #Calculate 80% cost of given value (0.8)

insurance()

#Problem 5
def diet_calculations():
    cal_from_fat = int(input("Enter grams of fat consumed: "))
    cal_from_carbs = int(input("Enter grams of carbs consumed: ")) #Get input from user
    print('Number of cals from fat = ', cal_from_fat * 9) #Return value using nutritionist calculation
    return 'Number of cals from carbs = ', cal_from_carbs * 4

diet_calculations()
