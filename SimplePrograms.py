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
#Fixed this!
def wumbo(words):
	for i in words:
		if i == 'M':
			return words.replace('M', 'W')
		#elif i == 'W':
		#	return words.replace('W', 'M')

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
    for i in names:
        result = 'Hello '.join(i)
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



#Thought for sure this would work for 2D matrix
#Only works w/ 1 array
def sum_of_evens(lst):
    even_list = []
    for i in lst:
        if (i % 2 == 0):
            even_list.append(i)
    return sum(even_list)


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
#Getting closer! tried joining while the string is reversed
#Couldn't use join() method, used my own
def reverse_and_not(i):
    result = str(i)
    i = str(i)
    return int(i[::-1] + result)

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
#Figured it out, must add +1 so that it counts itself
def countdown(start):
    count = []
    for i in range(start + 1):
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

#Got this on my own!
#Figured out how to "APPEND" to strings
def detect_word(txt):
    new_word = ''
    for i in txt:
        if i.islower():
            new_word +=i
    return new_word


#doesn't work, calculation is off by a small margin
#Probably related to the range
def sum_even_nums_in_range(start, stop):
    even_nums = []
    for i in range(start, stop):
        if i % 2 == 0:
            even_nums.append(i)
    return sum(even_nums)

#Works, but trying to only extract unique elements
#WIP
def count_unique(s1, s2):
    unique_chars = ''
    for i in s1, s2:
        if i not in unique_chars:
            unique_chars += i
    return len(unique_chars)

#Work in progress!
def filter_digit_length(lst, num):
    filtered_list = []
    for i in lst:
        if len(str(i)) <= len(str(num)):
            filtered_list.append(i)
    return filtered_list

#Takes a string & adds all ecen-indexed & odd-indexed together
#Getting close, but missing the last character.. how
#Figured it out, using -1 only counts from the right most of the string (in reverse)
#So, key is to not specify this & use 0:: & 1::
def index_shuffle(txt):
    even_words = txt[0::2]
    odd_words = txt[1::2]
    return even_words + odd_words


#The challenges was to do this without converting to INT, but couldn't figure it out, oh well! Works
def smaller_num(n1, n2):
    n1, n2 = int(n1), int(n2)
    lst = [n1, n2]
    sorted_list = sorted(lst)
    return str(min(sorted_list))

#Not complete, WIP, need to yse all()
def check_all_even(lst):
    for i in lst:
        if i % 2 == 0:
            return True
        else:
            return False


#Work on this! To be continued
def add_nums(nums):
    nums = nums.split(', ')
    return sum(nums)


def add_nums(nums):
	return sum(eval(nums))


#Work in progress, bookmarked
def mirror(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
    new_list.append(lst[::-1])
    return new_list


#Gotem
def mirror(lst):
    return lst + lst[-2:]

#Got it on this one! took a lot of trial & error
def mirror(lst):
    return lst + lst[-2::-1]



#Thought this would be more simple, got it down tho!
#Nice
def str_is_in_order(txt):
    lst = []
    for i in txt:
        lst.append(i)
    lst = sorted(lst)
    sorted_word = ''.join(lst)
    if txt == sorted_word:
        return True
    else:
        return False



#Remove 1st last not complete
#Figure out list slicing notation
def remove_first_last(txt):
    new_word = ''
    for i in txt:
        new_word.append(i[0])
        new_word.append(i[-1])
    return txt


#Remove 1st last not complete
#Figure out list slicing notation
def remove_first_last(txt):
    new_word = []
    for i in txt:
        new_word.append(txt[1:-2])
    return new_word


#Got it! Strengthening list comprehension!!!
def remove_first_last(txt):
    if len(txt) <= 2:
        return txt
    else:
        return txt[1:-1]


#Damn got it down! Noice
#Nice, got stuck on reverting negative to positive but got it down!!

def negate(lst):
    negated_list = []
    for i in lst:
        if i < 0:
            i = -i
            negated_list.append(i)
        elif i > 0:
            i = -+i
            negated_list.append(i)
    return negated_list

#Works but returns True instead of False for last test in Edabit
def hurdle_jump(hurdles, jump_height):
    if len(hurdles) <= 0:
        return True
    else:
        for i in hurdles:
            if len(hurdles) <= jump_height: #Hurdler can clear height if jump height is less than or equal to hurdle height
                return True
            else:
                return False


#2nd attempt, doesn't work
def hurdle_jump(hurdles, jump_height):
    if len(hurdles) < 0:
        return True
    else:
        for i in range(hurdles):
            if jump_height >= i:
                return True
            else:
                return False



def exists_higher(lst, n):
    if len(lst) < 0:
        return False
    else:
        for i in lst:
            if i >= n:
                return True
            else:
                return False


def exists_higher(lst, n):
    for i in lst:
        if i >= n:
            return True
        else:
            return False

#Wow, keep it simple!!
#Upper 2 code is complex, no need for the loop. The instructions tricky interpretation
def exists_higher(lst, n):
    if len(lst) < 0:
        return False
    elif max(lst) >= n:
        return True
    else:
        return False

#Simple problem
#not completed, adds instead of removing
def join_path(portion1, portion2):
    if '/' not in portion1 and portion2:
        return portion1 + '/' + portion2
    elif '/' in portion1:
        return portion1.strip('/') + '/' + portion2
    elif '/' in portion2:
        return portion2.strip('/') + '/' + portion2


#Returning only words that are 4 letters, WIP
def is_four_letters(lst):
    four_letters = []
    for i in lst:
        if len(i) == 4:
            four_letters.append(i)
    return four_letters

#WIP, look @ bookmark
def amplify(num):
    final_list = []
    for i in range(num):
        if i % 4 == 0:
            i = i * 10
            final_list.append(i)
        else:
            final_list.append(i)
    return final_list


#Good problem to solve, keep wokrin
def index_of_caps(word):
    cap_indexes = []
    for i in range(word):
        if i.isupper():
            cap_indexes.append(i)
    return cap_indexes


#Resolved out of memory (Sunday)
def reverse_list(num):
    reversed_list = []
    num = str(num)
    for i in num:
        reversed_list.append(int(i))
    return reversed_list[::-1]

#Resolved out of memory (Sunday)
def reverse_title(txt):
    titled_txt = txt.title()
    return titled_txt.swapcase()

#Resolved out of memory (Sunday)
def increment_items(lst):
    new_list = []
    for i in lst:
        i += 1
        new_list.append(i)
    return new_list

#Redid from memory
def has_same_bread(lst1, lst2):
    if lst1[0] == lst2[0] and lst1[-1] == lst2[-1]:
        return True
    else:
        return False

#Needed hints on this one
def sum_first_n_nums(lst, n):
    first_n_num = lst[:n]
    return sum(first_n_num)

#Redid from memory
def detect_word(txt):
    new_word = ''
    for i in txt:
        if i.islower():
            new_word += i
    return new_word

#Memory
def increment_items(lst):
    new_list = []
    for i in lst:
        i+=1
        new_list.append(i)
    return new_list

#Memory
def length(s):
    str_len = 0
    for i in s:
        str_len += 1
    return str_len

#Good string comprehension practice
def modify_last(txt, n):
    last_char = txt[-1] * n
    return txt[0:-1] + last_char


#Memory, nice!
def is_four_letters(lst):
    four_list = []
    for i in lst:
        if len(i) == 4:
            four_list.append(i)
    return four_list

#Complete this
def spelling(txt):
    word = []
    for i in txt:
        word.append(i)
    return word

#Practiced using eval
def greater_than_one(frac):
    if eval(frac) > 1:
        return True
    else:
        return False


#Doesn't work (OLD CODE)
def owofied(sentence):
    for x in sentence:
        if x == 'i' or x == 'e':
            if 'i' in x:
                x.replace('wi')
            elif 'e' in x:
                x.replace('we')
        return x, sentence


#New code, WIP
def owofied(sentence):
    new_sentence = ''
    for x in sentence:
        if x == 'i':
            x.replace(x, 'wi')
            new_sentence += x
        elif x == 'e':
            x.replace(x, 'we')
            new_sentence += x
    return x, new_sentence

#endswith() practice
def check_ending(str1, str2):
    if str1.endswith(str2):
        return True
    else:
        return False

#WIP
#Trying to strip chars from sentence
def strip_sentence(txt, chars):
    new_string = txt.replace(chars, '') #Only works with 1 letter
    return new_string

#WIP
def both(n1, n2):
    if n1 and n2 > 0 or n1 and n2 < 0 or n1 and n2 == 0:
        return True
    else:
        return False

#Doesn't include number itself
def find_even_nums(num):
    new_list = []
    for i in range(num):
        if i % 2 == 0:
            new_list.append(i)
    return new_list


#Redid from memory
def reverse_and_not(i):
    str_integer = str(i)
    return int(str_integer[::-1] + str_integer)

#Memory
def reverse_title(txt):
    title_case = txt.title()
    return title_case.swapcase()


def get_case(txt):
    for i in txt:
        if i.isupper():
            return 'upper'
        elif i.islower():
            return 'lower'
        elif i != i.lower() and i != i.upper():
            return 'mixed'



def get_case(txt):
    for i in txt:
        if not i.isupper() and not i.islower():
            return 'mixed'
        elif i.islower():
            return 'lower'
        elif i.isupper():
            return 'upper'


#3 attempts from memory, nice!
def get_case(txt):
    mixed_case = not txt.isupper() and not txt.islower()
    for i in txt:
        if mixed_case == True:
            return 'mixed'
        elif i.islower():
            return 'lower'
        elif i.isupper():
            return 'upper'

#Memory
def word_lengths(lst):
    wordlen_list = []
    for i in lst:
        wordlen_list.append(len(i))
    return wordlen_list

#Counting cap words, memory
def count_caps(word):
    cap_letters = 0
    for i in word:
        if i.isupper():
            cap_letters += 1
    return cap_letters
#Memory
def modify_last(txt, n):
    last_letter = txt[-1]
    return txt[0:-1] + (last_letter * n)

#memory
def long_burp(num):
    num = num - 1
    word = "Burp"
    return word[0:2] + (word[2] * num) + word[2::]

#Memory :)
def is_it_true(relation):
    if eval(relation) == True:
        return True
    else:
        return False

#Memory
def minus_one(lst):
    new_list = lst[0:-1]
    return new_list

#Memory
def reverse_title(txt):
    first_cap = txt.title()
    return first_cap.swapcase()

3
