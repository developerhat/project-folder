#usr/bin/python


myAge = int(input('How old are you?'))

year = str((2019- myAge)+100)

print('you will be 100 years old in ' + year)

userNum = int(input('Give me a number & I can tell you whether or not its even or odd: '))

if userNum % 2 == 0:
    print('the number is even')
else:
    print('this number is odd')

testList = [1, 11, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4, 6]

for num in testList:
    if num <= 5:
        print(num)
