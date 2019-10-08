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
