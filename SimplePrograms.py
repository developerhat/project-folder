#Misc simple programs


#Counting vowels program (Incomplete)
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    word = word.lower()
    for vowel in vowels:
        count = word.count(vowel)
        print(count)

#Oh shoot it worked! Did this on my own. Had to look up reorganizing & adding FizzBuzz as first check tho
def fizz_buzz(num):
    for i in range(num):
        if i % 2 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print('Buzz')
        elif i % 2 == 0:
            print('Fizz')
        else:
            print(i)

def reverse_string(str):
    return str[::-1]

#Got through this w minimal help
def is_palindrome(n):
    n = str(n)
    if n[::-1] == n[0::]:
        return True
    else:
        return False

#Counts number of words in program, did this on my own!
def count_words(str):
    for i in str:
        return str.count(' ') +1


def add_char_string(str, char, num):
    char = str(char)
    num = int(num)
    return str + (char*num)



def count_to_n(num):
    while x != num:
        return print(num)
        x += 1


def potatoes(string):
    return string.count('potato')

def count_true(list):
    return list.count(True)

def is_safe_bridge(x):
    if ' ' in x:
        return False
    else:
        return True

def halfQUarterEigth(num):
    list_results = [num/2, num/.25, num/.83]
    return list_results

#Doesn't work..
def sum_first_n_nums(lst, n):
    for n in range(lst):
        return sum(n)

def space_me_out(str):
    return " ".join(str)

def backwords(str):
    return str[::-1]


def count_words(str):
    return str.count(' ') +1


#Doesn't work!
#Add x chars to start & end of string Edabit
def string_add(string, char, length):
    result = string.center(length, char)
    return result

#What! Converts string equation to actual equation.
def equation(s):
    return eval(s)


#wow this worked! Cheated tho, used stackoverflow
def count_syllables(str):
    count = 0
    str = str.lower()
    vowels = 'aeiouy'
    for i in range(0, len(str)):
        if str[i] in vowels and str[i -1] not in vowels:
            count +=1
    if count == 0:
        count+=1
    return count #Trying to count syllables... hm..


#Doesn't work!
#Need for a way to say "If all chars in this string"
#OH SHIT! Got it to work!
#Switched all(i) to all(str)
def get_case(str):
    for i in str:
        if all(str) == str.isupper():
            return 'upper'
        elif all(str) == str.islower():
            return 'lower'
        else:
           return 'mixed'

    #My solution above, verbose

    #Generator solution?
    #return any(str.isupper() for i in str)
