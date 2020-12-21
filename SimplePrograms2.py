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
