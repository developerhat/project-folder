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

#Need to add ending to strings provided
#Returns holy
def add_ending(lst, ending):
    ending = str(ending)
    for x in lst:
        return x + ending

#Heyyyy got this right all on my own!!
#This works, but not entirely
#Entering 104 & 806 don't get removed even if they are divisible by 13. Weird
def unlucky_13(nums):
    for i in nums:
        if i % 13 == 0:
            nums.remove(i)
    return nums


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
