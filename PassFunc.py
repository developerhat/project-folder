#Passing parameter to function practice


def func1(num):
    return num / 2

def func2(n2):
    return n2 * 4

#Taking results from func1, storing in a variable to pass to function 2 
result = func1(1)

print(func2(result))
#OH Shoot! Got it!
