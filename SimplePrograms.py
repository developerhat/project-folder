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
