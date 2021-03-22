#PatrickGo Encryption.py
#Author: Patrick Go
#Date last modified: 03/21/21
#Purpose: Using encryption to obscure data

#Program uses: Encrypt given data

#Assignment 9 - Encryption

user_input = str(input("Enter a string: "))

rotation_number = int(input("Enter cipher amount: "))
character = str(input('Enter character: '))
ciphered_result = ''

for i in user_input:
    ciphered_result += i

for i in ciphered_result:
    ciphered_result += character

print(ciphered_result)
