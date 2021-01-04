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
