#usr/bin/python


#Practicing using ATBSWP

import pyperclip

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


#The below code uses range(len(list)) to print out all items in the list
cars = ['VW GTI', 'Subaru BRZ', 'Honda Civic Si']
for i in range(len(cars)):
    print('Index ' + str(i) + ' of this list is: ' + cars[i])


copy_clipboard = str(input('What would you like to copy on the clipboard? '))

pyperclip.copy(copy_clipboard)
paste_clipboard = pyperclip.paste()

print(paste_clipboard)
