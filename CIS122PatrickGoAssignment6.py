#PatrickGo Assignment 6.py
#Author: Patrick Go
#Date last modified: 02/21/21
#Purpose: Functions with Return

#Program uses: Using selection & conditionals

#Assignment 6 - Selection


#Problem 1:
def average():
    grade_1 = int(input("Enter grade 1: "))
    grade_2 = int(input("Enter grade 2: "))
    grade_3 = int(input("Enter grade 3: ")) #Store user input in variables
    average_grade = []
    average_grade.append(grade_1)
    average_grade.append(grade_2)
    average_grade.append(grade_3) #Append values to list
    true_avg = sum(average_grade) / len(average_grade) #Calculate average
    print ('Your average is: ',float(round(true_avg)))

average()

#Problem 2:
def grade_conversion():
    user_grade = int(input("Enter your grade: ")) #Collect input
    if user_grade <= 59: #Return a value depending on user input
        print("You have a C")
    elif user_grade >= 90:
        print("You have an A")
    elif user_grade >= 80:
        print("You have a B")

grade_conversion()

#Problem 3:
def temp_conversion():
    user_choice = int(input("Enter 1 to convert to Celsius, enter 2 to convert to Fahrenheit: "))
    if user_choice == 1: #Prompt user for conversion
        fahrenheit = int(input("Enter Fahrenheit value: "))
        c_conversion = (fahrenheit - 32) * 5/9 #Calculate conversion rate from fahrenheit to Celsius
        print("Celsius conversion: ", round(c_conversion))
    elif user_choice == 2: #Prompt user for conversion
        cels = int(input("Enter Celsius value: "))
        f_conversion = ((9/5)*cels)+32 #Calculate value
        print("Fahrenheit conversion: ", f_conversion)
    else:
        print("Not an option!") #Edge case error handling


temp_conversion()


#Problem 4:
def magic_date():
    month_input = int(input("Enter month: "))
    day_input = int(input("Enter day: "))
    year_input = int(input("Enter year: ")) #Gather user input
    if month_input * day_input == year_input: #Logic for whether or not month * day == year
        print("This date is magic!")
    else:
        print("Sorry! This date is not magic")

magic_date()

#Problem 5:
def bmi_calculator():
    height = int(input("Enter your height in inches: "))
    weight = int(input("Enter your weight in pounds: ")) #Gather user input
    bmi = weight*703 / (height**2) #Calculate bmi
    if bmi <= 18.5:
        print("You are underweight")
    elif bmi >= 25:
        print("You are overweight")
    elif bmi >= 18.5 and bmi <= 25:
        print("Your weight is optimal")

bmi_calculator()
