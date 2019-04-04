#usr/bin/python

import os.path

myAge, myName = 20, "Patrick";
print("Hello, I am " + str(myAge) + " and my name is " + myName);

my_list = [50, 48, 92, 21, 23, 45, 43, 41]
#my_list[0] = 55
#Practicing mutability with lists

print(my_list)

my_list.append(6)
my_list.sort()

print("The value after using append AND sort: ", my_list)

#sort() method is in-place, so can't assign the result to another value


my_dict = {'key1':[0, 1, 2], 'key2': 100}
#Can grab list values or any dictionary values directly using 1 line. Below
print (my_dict['key1'][1])

my_dict['key3'] = 400

print(my_dict.items())


my_tuple = (1, 2, 3)

myset = set()
myset =(1, 52, "Hello")

print("The set values are: ", myset)

#The as myfile in this script is a variable. How? Cool!
with open('myfile.txt', mode ='r') as myfile:
    contents = print(myfile.read())

#print(myfile.readlines())
#Close the file to prevent future errors
#myfile.close()
#however, since we used the script above with indent block code no need to close

#Code below adds string to my_new_file
#with open('my_new_file.txt', mode= 'a') as f:
#    f.write('FOUR on FOURTH!!!')


with open('my_new_file.txt', mode = 'r') as f:
        print(f.read())

with open('TESTIIIING.txt', mode ='w') as f:
    f.write('This file was created by me \n')
    f.write('This is a 2nd line')


with open('TESTIIIING.txt', mode ='r') as d:
    print(d.read())

#Using Else at the end of the conditional to request for users name & store input

name = "Patrick"

if name == 'Michael':
    print ("Hey Michael!")
elif name == 'Patrick':
    print("Hey Patrick!")
else:
    userName = input("What is your name?")
    print("Hey there " + userName)

#Playing w loops to print all iterable items in my list
#for i in my_list:
#    print(i)


for num in my_list:
    #Check for even
    if num % 2 ==0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num1 in my_list:
    list_sum = list_sum + num1

print(list_sum)

mystring = str(input("What's your name?"))

for letter in mystring:
    print(letter)

#Using the range function to count & print list
#for x in range(0,50,5):
#    print(x)

#Practicing printing out index location using enumerate()
inWord = 'abcdef'

for item in enumerate(inWord):
    print(item)
    print('\n')

#The above code prints out index locations & releases it on tuple format
