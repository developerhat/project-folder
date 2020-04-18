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


#Doesn't work..
def sum_first_n_nums(lst, n):
    for n in range(lst):
        return sum(n)


def has_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

#Works
def wumbo(words):
	for i in words:
		if i == 'M':
			return words.replace('M', 'W')
		elif i == 'W':
			return words.replace('W', 'M')

#Not working as planned
def simplePigLatin(string):
    return string[:0]  #+ 'ay'

#Got it!
def has_same_bread(lst1,lst2):
    if lst1[0] == lst2[0] and lst1[-1] == lst2[-1]:
        return True
    else:
        return False

def yeahNope(b):
    return "yeah" if b == True else "nope"

#Oh shit! Got this through w some help
def additive_inverse(lst):
    for x in range(len(lst)):
        lst[x] = -lst[x]
    return lst



#Got through this w a lil help!
#It works but is rejected by Edabit
#Found out why rejected - added final_list
def even_odd_partition(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    final_list = [even_list, odd_list]
    return final_list

def long_burp(num):
    return 'Bu' + num * 'r' + 'p'

#So close! Eval doesn't work with =?
def is_it_true(relation):
    if eval(relation) == True:
        return True
    elif '=' in relation:
        relation = relation.replace('=', '==')
        if eval(relation) == True:
            return True
    else:
        return False

#THIS ONE WORKS! Check the diff
def is_it_true(relation):
    if '=' in relation:
        relation = relation.replace('=', '==')
        if eval(relation) == True:
            return True
        else:
            return False
    elif eval(relation) == True:
        return True
    else:
        return False

#Counting list within list
#Fuck doesnt work
def measure_the_depth(lst):
    lst = str(lst)
	return lst.count('[]')





#Simple
def count_claps(txt):
    return txt.count('C')

#Does not work
def can_nest(list1, list2):
    if list1.min(list1) > list2.min(list2) and list1.max(list1) < list2.max(list2):
        return True
    else:
        return False

#For every 6 cups, add 1
#not working
#FIGURE THIS OUT?!
def total_cups(n):
    for x in range(n):
        if x / 6 == 0:
            return n + 1

#Doens't work?
def word_lengths(lst):
    for i in lst:
        return lst.count(len(i))

#WTF? Why isn't this one working. Seems so simple
#NEver returns 1
def flipBool(b):
    if b == True or 1:
        return 0
    elif b == False or 0:
        return 1

#Doesn't work yet, want to sum numbers up to integer given
def add_up_to(n):
    for i in range(n):
        i += i
    return i

#Want to count digits
def length(str):
    for i in str:
        return str.count(i) + 1

def divide(a,b):
    try:
        return a/b
    except:
        print("Can't divide by Zero!")

def one_odd_one_even(n):
    number = len(n)


#Got it to work! Was running into spacing tab errors but fixed that
def increment_items(lst):
    new_list = []
	for i in lst:
		i += 1
        new_list.append(i)
	return new_list

#Doesn't work..
def greet_people(names):
    for i in names:
        return 'Hello '.join(names)

#Getting closer on this one.. gotta figure out the formatting
#Gotta use .join() method
def greet_people(names):
    for i in names:
        return 'Hello', names

#Only returning negative, changed to easy <0, med<0, hard<0
#Needed a little help
def score_calculator(easy, med, hard):
    if easy < 0 or med < 0 or hard < 0:
        return 'invalid'
    else:
        return (easy*5) + (med*10) + (hard *20)


#Got this down, but need to account for negative numbers
def score_calculator(easy, med, hard):
    for i in easy,med,hard:
        if i == -i:
            return "Invalid"
        else:
            easy = easy * 5
            med = med * 10
            hard = hard * 20
            return easy + med + hard

#Got some help on this one, went back to previous code added [:]
def unlucky_13(nums):
    for i in nums[:]:
        if i % 13 == 0:
            nums.remove(i)
    return nums

#Returns sum of all elements in list
#Needed bit of help, was tryna use for loop
def get_sum_of_elements(lst):
    return sum(lst)


def first_vowel(txt):
	if 'a' or 'e' or 'i' or 'o' or 'u' in txt:
        return txt.index('aeiou')

def first_vowel(txt):
	for i in txt:
            if 'a' or 'e' or 'i' or 'o' or 'u' in txt:
                vowels = 'aeiou'
                return txt.index(vowels)

#THIS WORKS!! DAMN! Got a lil help but it CLICKED 
def first_vowel(txt):
    vowels = 'aeiouAEIOU'
    for i in txt:
        if i in vowels:
            return txt.index(i)
