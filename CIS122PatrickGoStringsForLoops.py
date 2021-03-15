#PatrickGo Assignment 8.py
#Author: Patrick Go
#Date last modified: 03/14/21
#Purpose: Using strings & for loops

#Program uses: Strings & for loops

#Assignment 8 - Strings & for loops

#Problem 1:

phrase = "Hello world!"
#What is the value returned by each index position?

print(phrase[0])
print(phrase[1])
#print(phrase[15]) index out of range, value is larger than string
print(phrase[-1])
print(phrase[-2])

#Problem 2:
fruit = 'apple'

#fruit[:]
print(fruit[:])

#fruit[ :3]
print(fruit[:3])

#fruit[ 3:]
print(fruit[3:])

#fruit[: -1]
print(fruit[:-1])

#fruit[0 : 11]
print(fruit[0:11])

#Problem 3:
string_1 = 'Hello World!'
print(string_1[6:-2])
print(string_1[2:5])

#Problem 4:

#Problem 5:
password = 'pwd'
attempts = 3
user_pass = str(input("enter password: "))

while user_pass != password:
    if user_pass == password:
        print("correct!")
    elif user_pass != password:
        print("incorrect!")
        attempts -=1
        break

#Problem 6:
str_2 = 'Midterm Exam is almost here'
str_1 = ''
for i in str_2:
    str_1 += i
print(str_1)
