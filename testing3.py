#usr/bin/python


#practicing from practicepython.org practice problems

userNum = int(input("Give me a number:  "))

if userNum % 4==0:
    print('this number is divisible by 4')
elif userNum % 2==0:
    print('this number is even')
else:
    print('this number is odd')

#This is for practice problem list list_ends
#Can return the last value, but not the first one
def list_ends():
    a = [5, 10, 15, 20, 25]

    new_list = a[0],a.pop()
    return new_list

def list_overlap():
     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
     #Exercise number 5 for practicepython.org
     #need to use in operator to check

def max_three():
    Num1 = int(input('Number 1: '))
    Num2 = int(input('Number 2: '))
    Num3 = int(input('Number 3: '))

    if Num3 > Num2 and Num1:
        return Num3
    elif Num2 > Num1 and Num3:
        return Num2
    elif Num1 > Num3 and Num2:
        return Num1
    #Easy way to do it below. Do it yourself above. Try using 6, logic is flawed need to modify
    #return max(Num1, Num2, Num3)

#real_password = "unsafepassword"
#user_password = str(input("Enter the password: "))
#Password checker
#while user_password != real_password:
#    user_password = input("Enter the password: ")
#print("You may enter!")

def pig_latin(word):

    first_letter = word[0]
    #check for vowel
    if first_letter in 'abcdefghijklmnopqrstuvwxyz':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('hi there'))

#Checks for whether or not 2 numbers are 10, make 10, or exceed 10
#This works! Only numbers sum 10, or are 10
def makes10(a, b):
    if a + b > 10:
        return False
    elif a + b < 10:
        return False
    elif a or b == 10:
        return True
    elif a + b == 10:
        return True

#From codingbat warmup problem
#Returning absolute difference for given number
def diff21(n):
    if n <= 21:
        return 21 - n
        return abs(n)
    elif n > 21:
        return (n - 21) * 2

#this is the complex way, and it's broken. Verbose
def sleep_in(weekday, vacation):
    if weekday == True:
        return False
    elif vacation == True:
        return True
    elif vacation == False:
        return False
    elif weekday == False:
        return True

#this is the advanced way of doing it, although not as verbose
def sleep_in2(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
