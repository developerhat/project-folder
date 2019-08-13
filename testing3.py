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

#Sum3 figured it out can't use nums[2] must use nums[-1] for last
def sum3(nums):
    return nums[0]+nums[1]+nums[-1]

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


#Codingbat list1
#Returns larger or smaller number b/t 1st & last value
def max_end3(nums):
    if nums[0] > nums[-1]:
        return nums[0]
    elif nums[-1] > nums[0]:
        return nums[-1]

#created to print upper case values
def upperInput():
    textIn = str(input('Please enter a value to print: '))
    return textIn.upper()

#From github python programming exercises
def sortingPhrase():
    raw_input = str(input('Enter a list of values: '))
    for x in raw_input:
        x.split(',')

    items = sort()

#Returns remainder of 2 provided numbers
def remainder(num1, num2):
    return num1 % num2

def hello_name(name):
    return 'Hello ' + name + '!'

#Wrote the 2 below functions by myself. Super easy tho
def to_int(num):
    return int(num)

def to_str(str1):
    return str(str1)

#determine whether or not a number is less than or equal to 0
def lessThanZero(num):
    if num <= 0:
        return True
    elif num > 0:
        return False

#Returns the next number in sequence
def nextNumber(num):
    return num+1

#Dang this was easier & simpler than I thought
def findSmallestNum(list1):
    return min(list1)

#Returns lastname, firstname
def concat_name(name1, name2):
    return name2, name1

#Function to check whether or not an element is in a list
def inList(list2, num1):
    if num1 in list2:
        return True
    elif num1 not in list2:
        return False


#returns difference of minimum & max value in a list
def difference_maxmin(list1):
    return max(list1) - min(list1)


#Edabit "easy" problem can't figure out
def indexOfCaps(str):
    if str == str.upper():
        return str.upper()
    else:
        return False

#I know I have to store this into a list & then run logic on it.
def is_validPIN(pinstr):
    pinstr = []
    if pinstr <= 4:
        return True

#Takes a list & returns the 1st odd number in the list. Created on my own
def find_odd(list1):
    for i in list1:
        if i % 2==1:
            return i

#Equality of 3 values from edabit. hard! Seems easy
#def equal(a,b,c):
#    if a==b:


#Challenge problem from edabit can't solve this either but getting warmer
def amplify(num):
    for i in range(num):
        return i

#did this on my own no help
def concat(list1, list2):
    return list1 + list2

#Fixed it & got it to work! Swapped out str==None to str==''
def is_empty(str):
    if str == '':
        return True
    else:
        return False

#Got through this w no help
def getLastItem(list3):
    return list3[-1]

#Returns integer after given integer
def NextNum(num):
    return num+1

#Did this on my own no help
def divisibleby5(num):
    if num % 5==0:
        return True
    else:
        return False

#Can't return the dashes for some reason
def dashConvert(num):
    for i in range(num):
        return '-'

#Already did this w reverse3 function up above, but wanted to re-write it for muscle memory
def reverseList(num):
    for i in num:
        return num[::-1]

#This only returns true, never returns false. Work in progress
def same_case(str):
    if str == str.upper() or str.lower():
        return True
    else:
        return False

#Did this w little help. At first was trying to return list3.sort() but was getting nothing
#Key is to do 2 separate lines, as sort() permanently changes the values
def sortNumsAscending(list3):
    list3.sort()
    return list3

#Did this on my own! Checks for whether or not given string is an integer/str
def int_or_string(val):
    if val == str(val):
        return 'str'
    elif val == int(val):
        return 'int'

#Returns largest number in list. Too easy
def findLargestNum(list1):
    return max(list1)

#Got a little help from Geeks4Geeks
#Dang got it to work! Trick here is sorting the list & then grabbing 2nd smallest value
def sum_two_smallest_nums(list2):
    list2.sort()
    return min(list2) +list2[1]

#Need to get middle chars in a string
#Involves string slicing and getting nth char using x[:n]
#def get_middle(str):
#    if len(str) % 2 ==0:
#        return str[]

#Woah this actually worked! Using STRINGS to return the output.
#It works, but logic fails when entering 1500 & 16 as values
def smaller_num(num1, num2):
    int(num1), int(num2)
    return min(num1, num2)

#checks to see whether or not a string is plural
def is_plural(str2):
    if str2[-1] == 's':
        return True
    else:
        return False

#Checks to see if value is divisible by 100
def divisible100(num):
    if num % 100 == 0:
        return True
    else:
        return False

#Checks to see whether or not a number is even or odd
def EvenOrOdd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'false'

#Edabit challenge for returning string containing 4 letters in list.
#NOT COMPLETE! couldn't figure it out. Edabit very easy Conditional challenge
def isFourLetters(list3):
    for i in list3:
        if i < 5:
            return i


#Did this on my own!! Reverses boolean & exception handling
def reverseBool(bool):
    if bool == True:
        return False
    elif bool == False:
        return True
    else:
        return 'boolean expected'

#Pretty easy got through myself
def calculate_exponent(base, exp):
    return base**exp

#Seems easy, need to print dashes for every char given
#def numToDashes(num):
#    for i in range(num):
#        return str('-')
#The above commented code is what I wrote myself. The solution is below...
#Moral story: SIMPLIFY! dont overthink
def numToDashes(num):
    return num * '-'

#God damn!! Was stuck on this for so long thinking it needed a for loop & all That
#Key was to use the .count() Method
def char_count(char1, string2):
    return string2.count(char1)

#Working on very easy problem for Edabit, can't get through tho
def add_ending(list4, ending):
    for str in list4:
        return str, ending

#Supposed to countdown from number to 0. Not working tho
def countdown(num):
    for i in range(num):
        return i+1

#Getting closer on this one. I'm sure gotta use loops
def greetings(names):
    for i in [names]:
        return 'Hello', names


#Dang got this to work!! I'm sure there's a better way to this though
def slot_machine(list):
    if list[0] == list[1] == list[2] == list[3]:
        return True
    else:
        return False

#Wow got through this alone!! Crazy!! The trick is to return item in a list
def repeat(item,times):
    return [item] * times

#Did this on my own but had to look up how to add , in between strings
def concat_name(first,last):
    return last + ', ' + first

#Got through this myself, pretty easy
def has_spaces(str):
    if " " in str:
        return True
    else:
        return False



#Got through this on my own!! Turns out you an also reverse STRINGS using the same method for lists
def reverseString(str):
    return str[::-1]


#Function is meant to return high & low integers. Can't get it to work tho, recognizes space as an integer
def high_low(nums):
    return max(nums), min(nums)


def addition(num1,num2):
    return num1 +num2

#Did this on my own! Checks if given element is in a list
def check(list, el):
    if el in list:
        return True
    else:
        return False

#Too easy
def divisible_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

#Too easy
def isEvenOrOdd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

#Returns smallest & largest num in list. Needed to return the numbers in a list, so reformatted
def minMax(list):
    return [min(list), max(list)]

#Got through this w minimal help! Referred to original palindrome
def is_palindrome(str):
    if str[::1] == str[::-1]:
        return True
    else:
        return False

#Got this one down on my own! Checks to see whether or not a string has same case
def same_case(str):
    if str == str.upper():
        return True
    elif str == str.lower():
        return True
    else:
        return False

#Checks to see whether or not an element is in a list
def check(list,el):
    if el in list:
        return True
    else:
        return False


#Checks if all leters are identical... got it right w a lil help
def is_identical(str):
    if str.count(str[0]) == len(str):
        return True
    else:
        return False


#Attempting to repeat each char given by n. Ex: Nnniiiccceee
def repeat_char(txt, n):
    for n in txt:
        return n*txt

#Getting closer but not quite! Need to capitalize 1st letter of all values given
def cap_me(list):
    for i in list:
        return i[0].upper()

#Got it right w a lil help. Needed to convert to grab length + convert to string
def find_digit_amount(num):
    return len(str(num))


#function compares 2 different strings. If the strings are same, return True
def compareString(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

#This only works if the values are exactly the same. Needs to be amount of chars in 1st string
#Got it to work now!! Little help
def comp(str1, str2):
    if len(str1) == len(str2):
        return True
    else:
        return False

#Did this on my own no help. Nice!
def match(str1, str2):
    if str1.lower() == str2.lower():
        return True
    else:
        return False

#Trying to make it so that all 4 values are same, return True. If not return false
#Wow got it to work! Needed to use .count() to count values in the list
def test_jackpot(result):
    if result.count(result[0]) == len(result):
        return True
    else:
        return False


#Wow... the method I was trying to use was to iterate through each char, check char isupper or lower, and then change the value
#Easier to jut use built in method, sheesh.
def reverse_case(str):
    return str.swapcase()


#Trying to return first and last elements as a new list. WORK IN Progress
#Got it done!!!! No help on this one. Just re-read question & reformatted
def first_last(list):
    newList =[list[0], list[-1]]
    return newList

#work in progress
def is_valid(zip):
    if zip <= 5:
        return True
    else:
        return False


#Don't really understand this. Getting warmer but not quite. Solve it. List 2 coding bat
def count_evens(nums):
    for i in [nums]:
        if i % 2 ==0:
            return 'hey'


#Creating this function myself. Removes vowels from user input
#Good use of for loop to remove the vowels, but is not very efficient. All good
def remove_vowel(input):
    #print('I will be removing all vowels from this! Please provide a phrase')
    for letter in 'aeiou':
        input = input.replace(letter, '')
    return input

#Dang did this on my own. Simple!
def say_hello_bye(name, num):
    if num == 1:
        return 'Hello ' + name.capitalize()
    elif num == 0:
        return "Bye " + name.capitalize()

#A bit silly. Did it myself. Good practice for control flow + using IN Operator
def prevent_distractions(txt):
    if 'anime' in txt:
        return 'NO!'
    elif 'meme' in txt:
        return 'NO!'
    elif 'vine' in txt:
        return 'NO!'
    elif 'roasts' in txt:
        return 'NO!'
    elif 'long hair' in txt:
        return 'Keep growing!'
    else:
        return 'Safe watching!'

#Super easy.
def month_name(num):
    if num == 1:
        return 'January'
    elif num == 2:
        return 'February'
    elif num == 3:
        return 'March'
    elif num == 4:
        return 'April'
    elif num == 5:
        return 'May'
    elif num == 6:
        return 'June'
    elif num == 7:
        return 'July'
    elif num == 8:
        return 'August'

#Not complete. On Edabit to determine how many times 'A' appears in the string
def count_a(str):
    letter = 'a'
    for letter in str:
        return letter

# Determining online free shipping eligiblity, but having to use a dictionary to loop through
def free_shipping(order):
    order = {}
    for i in order:
        if i > 50:
            return True
        else:
            return False


#Returns number of times character appears in string.
#Works, but tried 'y' and 'wazup' & it returned 1--why?
def char_count(char, str):
    for char in str:
        if char in str:
            return str.count(char)
        else:
            return 'not in string'

#This supposed to work! Takes all list values & checks to see if all are even
#Unfinished
def check_all_even(lst):
    for x in lst:
        if all(lst) % 2 == 0:
            return True
        else:
            return False


#This ones tough
#Getting warmer. It works when removing the other 2, but it's not "scalable"
#What if user enters 4 values?
#Unfinished
def secret_society(friends):
    for i in friends:
        return i[0][0], i[0][1], i[0][2]

#Oh shit!! Got this on my own. Just gotta make it simple, used count
def hash_plus_count(str):
    return [str.count('#'), str.count('+')]

#Easy money
def flip(y):
    if y == 1:
        return 0
    elif y == 0:
        return 1

#Trying to figure these 2 conversions out, not exactly working out
def to_list(num):
    return [num]

def to_number(lst):
    return (lst)


#Why doesnt this work? Supposed to run a check for all values given but 3 returns false
def is_omnipresent(lst,val):
    for i in range(len(lst[:])):
        if val in lst:
            return True
        else:
            return False

#Answer pretty much given on this one
def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False

#Converts a character to ASCII value

def ctoa(char):
    return ord(char)

#Did this on my own! Dang! Getting back into the swing of things
def number_syllables(word):
    return word.count('-')+1


#Did this on my own too. Just counted spacing to count for words
def count_words(txt):
    return txt.count(' ')+1


#Figured this out on my own! Sick! Got a little help to find out how ot reverse an integer
#Convert to string
def largest_swap(num):
    if str(num)[::-1] < str(num):
        return True
    elif str(num)[::-1] == str(num):
        return True
    else:
        return False

#Got this on my own
def get_word(left, right):
    return left.capitalize() + right

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


#Having trouble removing first & last character in a string
#Strings are immutable, so the string must be recreated somehow

def remove_first_last(txt):
    newtxt = txt.replace(, '')
    return newtxt

#wow!! Did this on my own. Took some time & troubleshooting but got it down
#Removes 1st & last char of string. Scalable!
def remove_first_last(txt):
    return txt[1:-1]


def exists_higher(lst, n):
    for i in lst:
        if i >= n:
            return True
        else:
            return False

#Using reverse method to reverse a list
def reverse_list(lst):
    lst.reverse()
    print (lst)
