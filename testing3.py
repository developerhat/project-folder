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
    for hi in range(len(str)):
            return hi

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

#Got through this all on my own no help
def first_two(str):
    if len(str) <= 2:
        return str
    else:
        return str[0] + str[1]

#Damn! Got through this by myself too! keep workin
def extra_end(str):
    return (str[-2] + str[-1])*3

#Got through this too damn!
def non_start(a, b):
    return a[1:] + b[1:]

#Almost got this one, but needed some help on it.
def first_half(str):
    return str[:len(str) // 2]


#String-2 double char CodingBat
#This is a bit tougher. Getting closer tho esp w for loop
#Why isn't this working? why return 0?
#Keep trying, it's a tough one
def double_char(str):
    for i in range(len(str)):
        return str*2

#Coding bat warmup got through no help
def not_string(str):
    if 'not' not in str:
        return 'not ' + str
    else:
        return str

#Needed a little help on this one. I was able to extract first and last value from the string tho
def front_back(str):
    return str[-1:] + str[1:-1] + str[:1]

#Did this all on my own
def sum_double(a,b):
    if a == b:
        return (a+b)*2
    else:
        return a+b


#Got through w minimal help
def without_end(str):
    return str[1:-1]

def make_out_word(out, word):
    string_end = out.split()
    return string_end, out
#can't get through this problem. Coding bat string-1 make_out_word problem

#Got through this alone
def make_abba(a,b):
    return a+b+b+a


#Got this right by myself but needed to use verbose method cos OR was not working. Returnig true all the time
def first_last6(nums):
    if nums[0] == 6:
        return True
    elif nums[-1] == 6:
        return True
    else:
        return False

#Did this on my own too, learned from the double_char function
def front3(str):
    return str[0:3]*3
        return i*2

#Holy crap I got this one on my own! Simplified it. Warmup 2
def front_times(str, n):
    return str[0:3]*n

#Dang same here got it on my own too easy
def string_times(str, n):
    return str*n

#Got through it but no exception handling or "edge" cases. Gotta be a better way to do this
def lucky_sum(a,b,c):
    if a == 13:
        return a+b
    elif b == 13:
        return b+c
    elif c == 13:
        return a+b
    else:
        return a+b+c

#Don't really understand this. Getting warmer but not quite. Solve it. List 2 coding bat
def count_evens(nums):
    for i in nums:
        if i % 2 ==0:
            return i

#Dang did this all on my own! Seemed complex but simple. Codingbat list 2
def big_diff(nums):
    return max(nums) - min(nums)

#Did this on my own from hackerrank but no edge case or exception handling
def if_else(n):
    if n % 2 == 1:
        return 'Weird'
    elif n % 2== 0 and n<5 and n>2:
        return 'Not Weird'
    elif n % 2 == 0 and n>6 and n<20:
        return 'Weird'

#Got through this alone too. Boss!
def split1(str):
    oldstr = str.split(' ')
    newstr = '-'.join(str)
    return oldstr, newstr

#This was too easy. Python doing all the legwork
def swap_case(s):
    return s.swapcase()

#Not complete but getting there. The goal is to print up to 123
def printfunc(n):
    if n < 123:
        for i in range(n):
            print(i)