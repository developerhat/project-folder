#Simple Programs 2 to run scripts on


def numbers_sum(lst):
    nums_only = []
    for i in lst:
        if isinstance(i, bool):
            continue
        elif isinstance(i, int):
            nums_only.append(i)
        else:
            continue
    return sum(nums_only)



def unique_sort(lst):
    no_dupes = []
    for i in lst:
        if i not in no_dupes:
            no_dupes.append(i)
    return sorted(no_dupes)

def count_vowels(txt):
    vowels = 'aeiou'
    vowel_count = 0
    for i in txt:
        if i in vowels:
            vowel_count += 1
    return vowel_count

def sum_two_smallest_nums(lst):
    two_lowest_nums = []
    positives = []
    for i in lst:
        if i < 0:
            continue
        elif i > 0:
            positives.append(i)
    positives = sorted(positives)
    two_lowest_nums.append(positives[0])
    two_lowest_nums.append(positives[1])
    return sum(two_lowest_nums)

def unique_lst(lst):
    unique_positives = []
    for i in lst:
        if i > 0:
            unique_positives.append(i)
    no_dupes = []
    for i in unique_positives:
        if i not in no_dupes:
            no_dupes.append(i)
    return no_dupes


def filter_list(lst):
    ints_only = []
    for i in lst:
        if isinstance(i, bool):
            continue
        elif isinstance(i, int):
            ints_only.append(i)
    return ints_only

def index_of_caps(word):
    index_pos = []
    for i in word:
        if i.isupper():
            index_pos.append(word.index(i))
    return index_pos

def setify(lst):
    no_dupes = []
    for i in lst:
        if i not in no_dupes:
            no_dupes.append(i)
    return no_dupes

def cap_to_front(s):
    cap_letters = ''
    low_letters = ''
    for i in s:
        if i.isupper():
            cap_letters += i
        else:
            low_letters += i
    return cap_letters + low_letters


def sum_two_smallest_nums(lst):
    two_smallest_nums = []
    no_negs = []
    for i in lst:
        if i > 0:
            no_negs.append(i)
    no_negs = sorted(no_negs)
    two_smallest_nums.append(no_negs[0])
    two_smallest_nums.append(no_negs[1])
    return sum(two_smallest_nums)

def replace_vowels(txt, ch):
    vowels = 'aeiou'
    for i in txt:
        if i in vowels:
            txt = txt.replace(i, ch)
    return txt

#Weird & inefficent solution
def is_in_order(txt):
    sorted_txt = []
    nosorttxt = []
    for i in txt:
        sorted_txt.append(i)
        nosorttxt.append(i)
    if sorted(sorted_txt) == nosorttxt:
        return True
    else:
        return False


def unique_sort(lst):
    no_dupes = []
    for i in lst:
        if i not in no_dupes:
            no_dupes.append(i)
    return sorted(no_dupes)

def stutter(word):
    new_word = ''
    for i in word:
        new_word += i
    return new_word[:2] + '... ' + new_word[:2] + '... ' + new_word +'?'


def sum_two_smallest_nums(lst):
    two_nums = []
    no_negs = []
    for i in lst:
        if i > 0:
            no_negs.append(i)
        else:
            continue
    no_negs = sorted(no_negs)
    two_nums.append(no_negs[0])
    two_nums.append(no_negs[1])
    return sum(two_nums)


def unique_sort(lst):
    no_dupes = []
    for i in lst:
        if i not in no_dupes:
            no_dupes.append(i)
    return sorted(no_dupes)

#Come back & do this one!
def remove_enemies(names, enemies):
    if len(enemies) < 1:
        return names
    else:
        return names.remove(enemies)

def is_harshad(num):
    harshad_num = []
    if num == 0:
        return False
    else:
        for i in str(num):
            harshad_num.append(int(i))
            harshad_num = sum(harshad_num)
            if int(num) % harshad_num == 0:
                return True
            else:
                return False


def society_name(friends):
    secret_word = ''
    word = []
    for i in friends:
        word.append(i[0])
    word = sorted(word)
    for i in word:
        secret_word += i
    return secret_word


def sum_two_smallest_nums(lst):
    two_nums = []
    pos_nums = []
    for i in lst:
        if i > 0:
            pos_nums.append(i)
    pos_nums = sorted(pos_nums)
    two_nums.append(pos_nums[0])
    two_nums.append(pos_nums[1])
    return sum(two_nums)

def disemvowel(string):
    vowels = 'aeiou'
    for i in string:
        if i.lower() in vowels:
            string = string.replace(i, '')
    return string


def xo(s):
    x_count = 0
    o_count = 0
    for i in s:
        if i.lower() == 'x':
            x_count += 1
        elif i.lower() == 'o':
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False


def validate_pin(pin):
    digits = []
    if len(pin) == 4 or len(pin) == 6:
        for
    else:
        return 'nope'

def secret_society(friends):
    result = ''
    initials = []
    for i in friends:
        initials.append(i[0])
    initials = sorted(initials)
    for i in initials:
        result += i
    return result

def array_plus_array(arr1, arr2):
    lst_1 = sum(arr1)
    lst_2 = sum(arr2)
    return lst_1 + lst_2

def shortcut(s):
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            s = s.replace(i, '')
    return s


def opposite(number):
    if number < 0:
        return abs(number)
    elif number >= 1:
        return -number
    elif number == 0:
        return 0

def feast(beast, dish):
    if dish[0] == beast[0] and dish[-1] == beast[-1]:
        return True
    else:
        return False


def mean(num):
    sum_digits = []
    for i in str(num):
        sum_digits.append(int(i))
    return sum(sum_digits) / len(str(num))
