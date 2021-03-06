#usr/bin/python

import os.path

#myAge = int(input('How old are you?'))

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


#with open('my_new_file.txt', mode = 'r') as f:
#        print(f.read())

#with open('TESTIIIING.txt', mode ='w') as f:
#    f.write('This file was created by me \n')
#    f.write('This is a 2nd line')


#with open('TESTIIIING.txt', mode ='r') as d:
#    print(d.read())

#Using Else at the end of the conditional to request for users name & store input
#name = "Patrick"

#if name == 'Michael':
#    print ("Hey Michael!")
#elif name == 'Patrick':
#    print("Hey Patrick!")
#else:
#    userName = input("What is your name?")
#    print("Hey there " + userName)

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
inWord = 'abcdefghijklmnopqrs'

for item in enumerate(inWord):
    print(item)
#The above code prints out index locations & releases it on tuple format

#Practice using zip() function

new_list = [1, 2, 3]
new_list2 = ['a', 'b', 'c', 'd']

for item in zip(new_list, new_list2):
    print(item)


list_test = []
#This will take the user input, and store iterable values in a list
for letter in mystring:
    list_test.append(letter)

print(list_test)

#Here, we are running the above code in ONE LINE! Crazy
#new_list3 = [x for x in 'Word!']

#print(new_list3)

#Here we only print even numbers
for num in my_list:
    if num%2==0:
        print(num)

#Coding problem from Github assessment project

#for num in range(1, 101):
#    if num%3 == 0 and num%5 == 0:
#        print('FizzBuzz!')
#    elif num%3 ==0:
#        print('Fizz')
#    elif num%5 ==0:
#        print('Buzz')
#    else:
#        print(num)

st = 'Create a list of the first letters of every word in this string'
#Printing only the letters that start with each letter
for word in st.split():
    print(word[0])

#userInput = str(input("What's your name?"))

#def testing(userInput):
#    return "Hello!", userInput
#Use return when working with functions in order to RETURN the output of program
#testing(userInput)

#result = testing('HI')

def add(n1, n2):
    return n1+n2

numResult = add(20,30)

#print(numResult)

urString = str(input("Pig latin conversion: "))


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
#Here we are using the dog check function to check if user input string has "dog" in it
#print(dog_check(urString))

def pig_latin(word):

    first_letter = word[0]
    #check for vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin(urString))

#Function below will take an argument and return back sum multiplied by .5
def myfunc1(*args):
    return sum(args) * 0.05

#The code below will return only even numbers
def myfunc(*args):
    mylist = []
    for num in args:
        if num%2==0:
            mylist.append(num)
    return mylist

print(myfunc(2,3,4,5,6,10))

def lesser_of_two_evens(a,b):
    #Both numbers even below
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        #One or both numbers odd
        return max(a,b)

def animal_crackers(a):
    wordlist = a.lower().split()
    #Using double index calls to shorten code
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers("doop DI!"))

#Function below used to check if sum of both numbers or one number is 20
def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

#This function below can determine whether or not 2 words have the same first letter. Returns boolean
def animal_crackers(a):
    wordlist = a.lower().split()
    first = wordlist[0]
    second = wordlist[1]
    return first[0] == second[0]

print(animal_crackers('f Foo!'))


def old_macdonald(name):
    fourth_letter = name[3].upper()
    inbetween = name[1:3]
    first_letter = name[0].upper()
    rest = name[4:]

    return first_letter + inbetween + fourth_letter + rest


def master_yoda(a):
    wordlist = a.split()
    reverse_wordlist = wordlist[::-1]

    return ' '.join(reverse_wordlist)

def almost_there(num3):
    return (abs(100 - num3) <=10) or (abs(200-num3) <=10)

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True

    return False

def paper_doll(text):
    textResult = ''
    for char in text:
        textResult += char*3
    return textResult

def blackjack(a,b,c):
    if a+b+c <= 21:
        return sum([a,b,c]) #Need to use a list to call a,b,c because regular (a,b,c)does not work
    elif 11 in ([a,b,c]) and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'
#Checks whether or not a number is 10, or sum is 10
#Logic is broken, when entering 2,5 it returns true
def makes10(a, b):
  if a or b == 10:
    return True
  elif a + b == 10:
    return True
  elif a or b > 10:
    return False
  elif a + b > 10:
    return False
  elif a + b < 10:
    return False
#Why is this shit broken?!?! This returns true only while testing3 returns false only
#Fixed it in testing3.py, check it out!
