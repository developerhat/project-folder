#usr/bin/python


#Practicing using ATBSWP

#This program says hello, asks for age, and displays length + age in a year
user_input = str(input('Hello! What is your name? '))
user_age = int(input('What is your age? '))

print('Hello, ' + user_input + '!')
print('The length of your name is: ', len(user_input))

if len(user_input) > 10:
    print('wow! That is a long name')
else:
    print('great to meet you!')

print('You will be ' + str((user_age +1)) + ' in one year. Congrats!')


#Messing round w Try/exception
#Trying to figure out what's going on here
def exception():
    user_input = str(input("What's your name? "))
    try:
        print(user_input)
        print(x)
    except:
        print('No value for X')
    finally:
        print("Hi!")
