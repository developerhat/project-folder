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

def is_it_true(relation):
    return eval(relation)

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
#WTF? Why isn't this one working. Seems so simple
#NEver returns 1
def flipBool(b):
    if b == True or 1:
        return 0
    elif b == False or 0:
        return 1


def divide(a,b):
    try:
        return a/b
    except:
        print("Can't divide by Zero!")

def one_odd_one_even(n):
    number = len(n)

#Need ot finish, book marked
def reverse_title(txt):
    return txt.swapcase()


#Doesn't wokr
def owofied(sentence):
    for x in sentence:
        if x == 'i' or x== 'e':
            if 'i' in x:
                x.replace('wi')
            elif 'e' in x:
                x.replace('we')
        return x, sentence


def googlify(n):
    if n <= 1:
        return 'invalid'
    else:
        return 'g' + ('o'*n) + 'gle'


#Having trouble incrementing
#NVM got this right! Solved it by creating new list, and appending new values to that list
#Instead of modifying list in place

def increment_items(lst):
	new_list = []
	for i in lst:
		i +=1
		new_list.append(i)
	return new_list

def has_same_bread2(lst1,lst2):
    if lst1[0] == lst2[0] and lst1[-1] and lst2[-1]:
        return True
    else:
        return False

#Wow needevd help looked in October.py code
#My solution was to use count, but didn't work
#Instead iterate through
def capital_letters(txt):
    cap_letters_counter = 0
    for i in txt:
        if i.isupper():
            cap_letters_counter += 1
    return cap_letters_counter


def reverse_capitalize(txt):
    txt = txt[::-1]
    return txt.upper()


def less_than_100(num1, num2):
    if num1 + num2 < 100:
        return True
    else:
        return False

def divides_evenly(a,b):
    if a % b == 0:
        return True
    else:
        return False

#Finish this!
def search(lst, item):
    for item in lst:
        return lst.index(item)


def prevent_distractions(txt):
    for i in txt:
        if 'anime' or 'meme' or 'vine' or 'roasts' or 'Danny DeVito' in txt:
            return 'NO!'
        else:
            return "Safe watching!"

#Got it on my own! Wow! memorized, no help
def is_identical(s):
    if s[::-1] == s[::]:
        return True
    else:
        return False

def and(a,b):
    if a and b == True:
        return True
    else:
        return False

#Damn figured this out!

def rev(n):
    n = str(abs(n))
    return n[::-1]

#Wow, was using or True & or False here but no need!
def flip_bool(b):
    if b == 1:
        return 0
    elif b == 0:
        return 1

def F_to_C(f):
    return (f - 32) * (5/9)

def C_to_F(c):
    return (c * 9/5) + 32


def get_first_value(number_list):
    return number_list[0]

#this one's a bit more complicated, solve it later hehe
#Requires 0 count first
def count_syllables(txt):
    return txt.count()

#Damn gotta figure this out!
#Got it! Switched logic from is 13, to if not 13
def unlucky_13(nums):
    new_list = []
    for i in nums:
        if i % 13 != 0:
            new_list.append(i)
    return new_list

#Couldn't figure this out!!
def hello_world(num):
    if num % 5 and num % 3 == 0:
        return 'Hello World'
    elif num % 3 == 0:
        return 'Hello'
    elif num % 5 == 0:
        return 'World'


def hello_world(num):
    if num % 15 == 0:
        return 'Hello World'
    elif num % 3 == 0:
        return 'Hello'
    elif num % 5 == 0:
        return  'World'

def get_multiplied_list(lst):
    new_list = []
    for i in lst:
        i = i * 2
        new_list.append(i)
    return new_list


def remove_none(lst):
    new_list = []
    for i in lst:
        if i != None:
            new_list.append(i)
    return new_list

def has_spaces(txt):
    if ' ' in txt:
        return True
    else:
        return False

#Doesn't work gotta return number of capital letters
def capital_letters(txt):
    for i in txt:
        if i.isupper():
            return i.count(txt)

def k_to_k(n, k):
    if k**k == n:
        return True
    else:
        return False


#Got from hacker rank
def conditional(n):
    if n % 2 == 1:
        return 'Weird'
    elif n % 2 == 0 and n in range(2,5):
        return 'Not Weird'
    elif n % 2 == 0 and n in range(6,20):
        return 'Weird'
    elif n % 2 == 0 and n > 20:
        return 'Not Weird'

#Got it w minimal help!
#Was fucken up w/ max(lst), wrote it as lst.max()
def difference_max_min(lst):
    for i in lst:
        return max(lst) - min(lst)


def concat_list(lst1,lst2):
    return lst1 + lst2


#DAMN! Pretty much solved this on my own
#Had trouble w/ format for count(), was using count(hashes) instead of hashes.count()
def hash_plus_count(txt):
    hashes = []
    pluses = []
    for i in txt:
        if i == '#':
            hashes.append(i)
        elif i == '+':
            pluses.append(i)
    return [hashes.count('#'), pluses.count('+')]

#Ouh this was a fun one!
#Solved on my own!! OH SHIT!
def remove_none(lst):
    new_list = []
    for i in lst:
        if i != None:
            new_list.append(i)
    return new_list


def get_word(left, right):
    return left.title() + right


#DOESNT WORK! FIGURE THIS ONE OUT
#GOT IT!
def is_palindrome(txt):
    #rev_text = reverse(txt)
    #Dont need rev_text, since the code below is already reversed
    if txt[::-1] == txt:
        return True
    else:
        return False

def first_last(lst):
    new_list = []
    new_list.append(lst[0])
    new_list.append(lst[-1])
    return new_list

#Returns the mean of number
def mean(nums):
    result = sum(nums) / len(nums)
    return round(result, 1)

#Swaps the cases
def reverse_case(txt):
    return txt.swapcase()


def find_digit_amount(num):
    num = str(num)
    return len(num)

#Checks if all elementsi n list are same
#Not sure how count does this?
def jackpot(result):
    if result.count(result[0]) == len(result):
        return True
    else:
        return False

#DAMN! DID THIS ON MY OWN!
def count_vowels(txt):
    vowels = 'aeiou'
    vowel_count = 0
    for i in txt:
        if i in vowels:
            vowel_count += 1
    return vowel_count

#Got it down yee yee
#One of the first few problems I solved on Edabit
def no_odds(lst):
    no_odds = []
    for i in lst:
        if i % 2 == 0:
            no_odds.append(i)
    return no_odds

#Not working?
def greet_people(names):
    hello = 'Hello'
    for i in names:
        result = hello.join(names)
    return result

#Doesn't work yet, want to sum numbers up to integer given
def add_up_to(n):
    for i in range(0, n):
        i += i
    return i




#OH SHOOT! Got this right no help
def findLargestNums(lst):
    new_list = []
    for i in names:
        new_list.append(i)
    return new_list.join('Hello, ', new_list[0])



def get_fillings(sandwich):
    new_list = []
    for i in sandwich:
        if i != 'bread':
            new_list.append(i)
    return new_list


def get_only_evens(nums):
    new_list = []
    for i in range(0, nums):
        if i % 2 == 0:
            new_list.append(i)
    return new_list


#I GOT IT! BUT DOESNT do it in right format, why?
#Oh got it! Just add as an integer
def reverse_list(num):
    new_list = []
    for i in str(num):
        new_list.append(int(i))
    return new_list[::-1]


#?? Doesn't work
def measure_the_depth(lst):
    return str(lst).count('[]')


def is_avg_whole(arr):
    result = sum(arr) / len(arr)
    if result.is_integer():
        return True
    else:
        return False

#Got it!

def divisible(lst):
    result = 1
    for i in lst: #This for loop returns the product of all ele in list
        result = result * i
    if result % sum(lst) == 0:
        return True
    else:
        return False

#EZ
#Tried doing it in 1 line initially: return(abs(sum(lst))), but didn't work
def get_abs_sum(lst):
    new_list = []
    for i in lst:
        new_list.append(abs(i))
    return sum(new_list)


#Work in progress, bookmarked
def mirror(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
    new_list.append(lst[::-1])
    return new_list

#Thought for sure this would work for 2D matrix
#Only works w/ 1 array
def sum_of_evens(lst):
    even_list = []
    for i in lst:
        if (i % 2 == 0):
            even_list.append(i)
    return sum(even_list)


#doesn't work
def sum_even_nums_in_range(start, stop):
    even_nums = []
    for i in range(start, stop):
        if i % 2 == 0:
            even_nums.append(i)
    return sum(even_nums)

#got this!
#Could also use count = 0, count=+1
def count_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return len(even_nums)

#CodingBat
def big_diff(nums):
    return max(nums) - min(nums)
#CodingBat
def make_ends(nums):
    new_list = []
    new_list.append(nums[0])
    new_list.append(nums[-1])
    return new_list


#CodingBat
def sum2(sums):
    new_list = []
    new_list.append(sums[0])
    new_list.append(sums[1])
    return sum(new_list)

#1st list nests inside 2nd
def can_nest(list1,list2):
    if min(list1) > min(list2) and max(list1) < max(list2):
        return True
    else:
        return False



#Want to count digits without using len()
#Got it! Was trying to use a list, but use count in this case
#Count() doesn't work here
def length(str):
    count = 0
    for i in str:
        count += 1
    return count

#Can't figure out the formatting here
def reverse_and_not(i):
    result = str(i)
    i = str(i)
    i = reversed(i)
    return i.join(result)

#Increment +1 for odd, -1 for even
#Got 'em! Getting better!!
def transform(lst):
    final_list = []
    for i in lst:
        if i % 2 == 0:
            i -= 1
            final_list.append(i)
        elif i % 2 != 0:
            i += 1
            final_list.append(i)
    return final_list

#Remove 1st last not complete
#Figure out list slicing notation
def remove_first_last(txt):
    new_word = ''
    for i in txt:
        new_word.append(i[0])
        new_word.append(i[-1])
    return txt


#Couldn't get this, return later
def add_odd_to_n(n):
    num_list = range(n)
    for i in num_list:
        if i % 2 != 0:
            sum_result = sum(num_list)
    return sum_result


#def add_odd_to_n(n):
    #sum = int()
    #for i in range(n):
        #if i % 2 != 0:

#Incomplete return later
def max_total(nums):
    sorted = sort(nums)
    result = sum(sorted)
    return result

#How do you inlcude integer? 1 should return 1,0
def countdown(start):
    count = []
    for i in range(start):
        count.append(i)
    return count[::-1]


def calculate_scores(txt):
    return [txt.count('A'), txt.count('B'), txt.count('C')]


#Logic practice
def should_serve_drinks(age, on_break):
    if age >= 21 and on_break == False:
        return True
    elif age >= 21 and on_break == True:
        return False
    elif age <= 20 and on_break == False:
        return False
    elif age <= 20 and on_break == True:
        return False

#Doesn't work..
def sum_first_n_nums(lst, n):
    for n in range(lst):
        return sum(n)

#Revised code, nice!!!
def sum_first_n_nums(lst, n):
    first_n_num = lst[:n]
    return sum(first_n_num)


#Doens't work?
def word_lengths(lst):
    for i in lst:
        return lst.count(len(i))


#My new solution! Look @ the progress
def word_lengths(lst):
    word_lengths = []
    for i in lst:
        word_lengths.append(len(i))
    return word_lengths

#Redid this for memory
def divisible(lst):
    product = 1
    for i in lst:
        product = i * product
    if product % sum(lst) == 0:
        return True
    else:
        return False

def transform(lst):
    new_list = []
    for i in lst:
        if i % 2 == 0:
            i = i -1
            new_list.append(i)
        elif i % 2 != 0:
            i = i + 1
            new_list.append(i)
    return new_list

#Redid this for memory
#Had to go back & check former answer
def sum_first_n_nums(lst, n):
    first_n_num = lst[::n]
    return sum(first_n_num)

#Logic here, redid for practice
def can_nest(list1, list2):
    if min(list1) > min(list2) and max(list1) < max(list2):
        return True
    else:
        return False

#Redid this for memory
def word_lengths(lst):
    word_lengths = []
    for i in lst:
        word_lengths.append(len(i))
    return word_lengths

#redid this one from memory too, nice!! 
def reverse_list(num):
    final_list = []
    num = str(num)
    for i in num:
        final_list.append(int(i))
    return final_list[::-1]
