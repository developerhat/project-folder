#Password generator program
#Wow pretty basic! Got it to work w minimal help
import random

print("Hello! Welcome to Patrick's password generator!")
print("\n")
word_list = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlength = 0
print('For security purposes, your password must exceed 8 characters.')

while passlength <= 7:
    passlength = int(input('How long would you like this password to be? '))
    if passlength <=7:
        print('We need more than 8 chars fam!')
else:
    generated_password = ''.join(random.sample(word_list,passlength))
    print("Thanks for using me! Here's your super secure password: ", generated_password)
