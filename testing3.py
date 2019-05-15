#usr/bin/python


#practicing from practicepython.org practice problems

userNum = int(input("Give me a number:  "))

if userNum % 4==0:
    print('this number is divisible by 4')
elif userNum % 2==0:
    print('this number is even')
else:
    print('this number is odd')

#This is for practice problem list list_ends
#Can return the last value, but not the first one
def list_ends():
    a = [5, 10, 15, 20, 25]

    new_list = a[0],a.pop()
    return new_list

def list_overlap():
     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
     #Exercise number 5 for practicepython.org
     #need to use in operator to check

def max_three():
    Num1 = int(input('Number 1: '))
    Num2 = int(input('Number 2: '))
    Num3 = int(input('Number 3: '))

    if Num3 > Num2 and Num1:
        return Num3
    elif Num2 > Num1 and Num3:
        return Num2
    elif Num1 > Num3 and Num2:
        return Num1
    #Easy way to do it below. Do it yourself above. Try using 6, logic is flawed need to modify
    #return max(Num1, Num2, Num3)

#real_password = "unsafepassword"
#user_password = str(input("Enter the password: "))
#Password checker
#while user_password != real_password:
#    user_password = input("Enter the password: ")
#print("You may enter!")

def pig_latin(word):

    first_letter = word[0]
    #check for vowel
    if first_letter in 'abcdefghijklmnopqrstuvwxyz':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('hi there'))

#Checks for whether or not 2 numbers are 10, make 10, or exceed 10
#This works! Only numbers sum 10, or are 10
def makes10(a, b):
    if a + b > 10:
        return False
    elif a + b < 10:
        return False
    elif a or b == 10:
        return True
    elif a + b == 10:
        return True

#From codingbat warmup problem
#Returning absolute difference for given number
def diff21(n):
    if n <= 21:
        return 21 - n
        return abs(n)
    elif n > 21:
        return (n - 21) * 2

#this is the complex way, and it's broken. Verbose
def sleep_in(weekday, vacation):
    if weekday == True:
        return False
    elif vacation == True:
        return True
    elif vacation == False:
        return False
    elif weekday == False:
        return True

#this is the advanced way of doing it, although not as verbose
def sleep_in2(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def make_out_word(out, word):
    string_end = out.split()
    word_end = word
#can't get through this problem. Coding bat string-1 make_out_word problem

#Coding bat logic-1 problem
def caught_speeding(speed):
    if speed < 60:
        return 0
    elif speed > 81:
        return 2
    elif speed >= 61:
        return 1
    elif speed < 80:
        return 1

#Coding bat problem logic-1
def love6(a,b):
    if a or b == 6:
        return True
    elif a + b == 6:
        return True
    elif a - b == 6:
        return True

#Codingbat logic-1 sorta_sum
def sorta_sum(a,b):
    if a + b >= 19:
        return 20
    elif a + b < 11:
        return a + b

#My solution below
#def array_count9(nums):
#    for i in nums:
#        if i == 9:
#            return nums


def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count +1

    return count


#From python 3 bootcamp function pracice problems

def count_primes(num):

    if num < 2:
        return 0
        #checking to  see if number is 0 or 1, cos they're excluded
    primes = [2]
    x = 3
    #X is going through every number up to input number
    while x <= num:
        #check if X is prime
        for y in range (3, x, 2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

#Homework assignment python3 bootcamp course---I GOT IT ON MY OWN!!!!
def ran_bool(num, low, high):
    if num in range(low,high):
        return True
    else:
        return False
#Same here, did this on my own. Gettin it
def ran_check(num, low, high):
    if num in range(low,high):
        print(num, 'is in range of', low, 'and' ,high)
    else:
        print('That number not in range')

#Wow! Got this one on my own too!
def palindrome(s):
    if s[::-1] == s[::1]:
        return True
    else:
        return False

#This is my attempt at this
def multiply(numbers):
    for i in numbers:
        i *=numbers
    return numbers

#This is the answer copied, getting there!
def multiply(numbers):
    total = numbers[0]
    for i in numbers:
        total *= i
    return total

#Codingbat string 2, incomplete
def count_hi(str):
    hi = 'hi'
    for hi in str:
        return num

#Got through this w minimal help! .reverse() method does not work here
def reverse3(nums):
    for i in nums:
        return nums[::-1]

#Oh shit did this all on my own! CodingBat marking as wrong why? Tested works good
def middle_way(a,b):
    for i in a,b:
        return a[1], b[1]

#This worked too, got it down but doesn't work in codingbat
def same_first_last(nums):
    if nums[0] == nums[-1]:
        return True
    else:
        return False

#Sum3 can't figure out but seems simple
def sum3(nums):
    return nums[0]+nums[1]+nums[3]

#This works, but it never returns false. Why?
def has23(nums):
    if 2 or 3 in nums:
        return True
    else:
        return False

#Heyyy this worked! On my own too
def make_ends(nums):
    return [nums[0], nums[-1]]

#This works, however the prompt wanted it to be less than 2 add both numbers. Just adding both for this right here.
def sum2(sums):
    for i in sums:
        return sums[0] + sums[1]

#This was ridiculously easy
def make_pi():
    return [3,1,4]
