#usr/bin/python

#This loop will print hello 5 times
spam = 0

#Will print hello until spam is equal to or greater than 5
while spam < 5:
    print('Hello ')
    spam = spam + 1

#Code below keeps asking for input until you type your name
#Programmer humor?
name = ' '

while name != 'your name':
    name = str(input('Please type your name: '))
print('Thank you!')

#Edabit Level 2 Easy problem
#Sorta got it but edge cases like special chars doens't work
def is_valid_pin(pin):
    if len(pin) == 4:
        return True
    elif len(pin) == 6:
        return True
    else:
        return False

#checks for string value as symmetrical
#how can we do this for integer? store in list?
def is_symmetrical(num):
    num = str(num)
    if num[::-1] == num[::1]:
        return True
    else:
        return False

#calculator from Edabit but no exception handling for 0
#Need to add for zero
def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Can't divide by 0!"



#This was easy but silly looking. Basic
def is_truthy(val):
    if val == False or None or 0 or [] or {} or "":
        return 0
    else:
        return 1

#From coding bat, returns given string 3 times
def string_times(str, n):
    return str*n

#From CodingBat, returns first 3 chars times 3
def front_times(str, n):
    return str[:3] * n

#Returns number of times 9 appears in a list
#Getting better using the count function!
def array_count9(nums):
    return nums.count(9)

#Returns True if first 4 values contains the integer 9
def array_front9(nums):
    if 9 in nums[0:4]:
        return True
    else:
        return False

#Returns False. We need it to return True.. why?
def array123(nums):
    if [1,2,3] in nums [0:3]:
        return True
    else:
        return False

#Supposed to return evens in a list
#Only returns the first even
#NEED TO SOLVE CODINGBAT LIST 2
def count_evens(nums):
    for i in nums:
        if i % 2 == 0:
            return nums.count(i)

#Returns True if values are 6 or add up to 6, etc.
def love6(a,b):
    if a or b == 6:
        return True
    elif a + b == 6:
        return True
    elif a - b or b - a == 6:
        return True
    else:
        return False


#wow got this on my own!! Seemed so difficult but got it down!
def operation24(num1, num2):
    if num1 + num2 == 24:
        return 'added'
    elif num1 - num2 == 24:
        return 'subtracted'
    elif num1 * num2 == 24:
        return 'multiplied'
    elif num1 / num2 == 24:
        return 'divided'
    else:
        return None

#Working on very easy problem for Edabit, making progress! only does 1st one tho..
def add_ending(list4, ending):
    for str in list4:
        return str + ending

#Returns Edabit but with a the amount of times input is entered
#Pretty easy got it on my own!
def how_many_times(num):
    return 'Ed' + 'a' * num + 'bit'

#Trying to return text n number of times: 'hhii'
def repeat(txt, n):
    return txt*n

#Got this on StackOverflow. Big hack tho.. idk what it does really
def repeat(txt, n):
    return ''.join([char*n for char in txt])

#Returns the index of first vowel encountered
#Doesn't work though, no substring?
#Returns None, why?
def first_vowel(txt):
    for i in txt:
        if 'aeiou' in txt:
            return txt.index('aeiou')

#This removes 13, however it only removes the 1st 13 value it encounters. Why?
def unlucky_13(nums):
    for i in nums:
        if i % 13 == 0:
            nums.remove(i)
    return nums


#Wow did this on my own!! NO resources!!
#Sick! Returns index for value provided
def search(lst, item):
    for i in lst:
        if item in lst:
            return lst.index(item)
        else:
            return -1


#Getting closer on this one.. gotta figure out the formatting
def greet_people(names):
    for i in names:
        return 'Hello', names

#Doens't work, see answer below. This was my attempt
def count_vowels(txt):
    for i in txt:
        return 'aeiou'.count(txt)

#Got this code from online
#Works tho!
def count_vowels(txt):
    vowels = 0
    for i in txt:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels += 1
    return vowels

#Got this all on my own, easy
def tri_area(base, height):
    return base * height / 2


#This is supposed to return a list of numbers counting down from numbers given to 0
#Can't get through it though. Edabit bookmarked problem
def countdown_to_zero(start):
    for i in start:
        while i != 0:
            i = i - 1
    return i


#Couldn't figure this out. Edabit bookmarked problem
def amplify4(num):
    if num % 4 == 0:
        for i in range(num):
            return


#Need to add ending to strings provided
#Returns only once, need ot return for each item in list
def add_ending(lst, ending):
    for x in lst:
        return x + ending

#Wow got this w minimal help! Needed to add list()
def get_sequence(low, high):
    return list(range(low, high+1))


def reverse(lst):
    return lst[::-1]

#Got through this w minimal help, needed to use max()
def exists_higher(lst, n):
    for i in lst:
        if max(lst) >= n:
            return True
        else:
            return False

#converts hours & minutes + adds for seconds
def convert(hours, minutes):
    hours = hours * 3600
    minutes = minutes * 60
    return hours + minutes

#Wow! Returns index of given string in list
#Did this on my own no help
def find_index(lst, txt):
    return lst.index(txt)

#Damn!! Got this on my own too! Used exception handling
#Instead of using if else, used exception handling
def search(lst, item):
    try:
        return lst.index(item)
    except:
	    return -1


#Need to use list comprehension or lamda, filter, map to remove all values in list
#Why does it only remove one value in list?
def remove_none(list):
    for i in list:
        if i == None:
            list.remove(i)
        return list

#Got through this w a lil help!
#It works but is rejected by Edabit
def even_odd_partition(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list



#Got through this w minimal help
#Needed to copy the list using [:]?
def no_odds(lst):
    for i in lst[:]:
        if i % 2 != 0:
            lst.remove(i)
    return lst

#Needed help on this one but got the fundamentals right on my own(using the for loop + range)
def sum_recursively(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    return total


#Heyyyy got this right all on my own!!
#This works, but not entirely
#Entering 104 & 806 don't get removed even if they are divisible by 13. Weird
#Fixed this by copying the list nums[:]
def unlucky_13(nums):
    for i in nums[:]:
        if i % 13 == 0:
            nums.remove(i)
    return nums

#Did this on my own! Simple
def difference(nums):
    for i in nums:
        return max(nums) - min(nums)

#Figuring this out, how can you multiply list values w length of list?
#Got it! needed to create a new list & store the results in that list
#Needed some help but makes sense
def MultiplyByLength(arr):
    result = []
    for i in arr:
        result.append(i * len(arr))
    return result


#Got through this w a little help!
#Reverses a string
def rev(n):
    n = abs(n)
    return str(n)[::-1]


#This challenge is interesting. Not finished, bookmarked in Edabit
#What am I doing wrong here?
def transform(list):
    for i in list:
        if i % 2 == 0:
            i = i-1
            return list
        else:
            i = i+1
            return list

#Works & did this on my own but pretty simple
def same_first_last(nums):
    if nums[0] == nums[-1]:
        return True
    else:
        return False

#This runs & works but doesn't return absolute value?
def get_abs_sum(lst):
    total = 0
    abs_value = [abs(i) for i in lst]
    for i in range(len(lst)):
        total = total + lst[i]
    return total

#Did this on my own! Pretty simple but good nontheless
#Works but doesn't pass Edabit test
def smaller_num(n1, n2):
    result = min(n1, n2)
    n1 = str(n1)
    n2 = str(n2)
    return result

#Trying to return number of arguments passed through
#Wow got through this! had an overcomplicated answer.
#Simplify it, key is simplify
def number_args(*argv):
    return len(argv)

#Can't figure this out yet
#Need to return the difference between highest & lowest number in list
def list_difference(nums):
    for i in nums:
        result = nums.max(nums) - nums.min(nums)
    return result


#Trying to check if all numbers in list are even
def check_all_even(lst):
    if all(lst) % 2 == 0:
        return True
    else:
        return False

#Checking if all items in list are even. Can't quite get it right
def check_all_even(lst):
    for x in lst:
        if x % 2 == 0:
            return True
        else:
            return False

#Wow got this done on my own! Didn't think it worked but gave it a try
def programmers(one, two, three):
    return max(one, two, three) - min(one, two, three)

#I get what it's asking for but havin trouble formatting..
#Hey got this on my own! Pretty simple
def animals(chickens, cows, pigs):
    return (chickens*2) + (cows*4) + (pigs*4)

#Got this on my own pretty simple
def k_to_k(n, k):
    if k**k == n:
        return True
    else:
        return False

#Wow got this all on my own!!
#At first wasn't taking reverse(), so used built-in copy method
def reverse_capitalize(txt):
    return txt.upper()[::-1]

#Wow pretty much did this on my own!
#Needed some pushing to use sum(), was thinking of using for loop
def mean(nums):
    result = sum(nums)
    mean_result = result / len(nums)
    return round(mean_result, 1)


#Just messing round here!
def testing():
    question = str(input('Hi! What is your name? '))
    print('Hi, ' + question + '!')
    age = int(input('How old are you? '))
    print("Nice! You are " + str(age) + ' years old. You oldie!')



    
