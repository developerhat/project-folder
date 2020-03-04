#Misc simple programs


#Counting vowels program

def count_vowels(word):
    vowels = 'aeiou'
    word = word.lower()
    print(word.count(vowels))


def fizz_buzz(num):
    for i in range(num):
        if i % 2 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 2 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
