

def frames(minutes, fps):
    fps = fps * 60
    return minutes * fps



def googlify(n):
    if n <= 1:
        return 'invalid'
    else:
        result = 'G' + n*'o' + 'gle'
        result = str(result)
        return result

def catch_zero_division(expr):
    if '0' in expr:
        return True
    elif eval(expr) == 0:
        return True
    else:
        return False

#Not my code, solution code edabit
#WTF! Looks so simple compared to mine. Wow
def catch_zero_division(expr):
	try: eval(expr)
	except: return True
	return False

#Ohh shit! Got this on my own eventually!
#TOOK SOME ITME! DAMN RUSTY AF!

#WOW! Was tryna actually divide as opposed to using MODULUS
#FUCKEN ROOKIE
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 ==0:
            return False
    else:
        return False

#0 & 1 return T/F
def reverse_boolean(arg):
    if type(arg) == True:
        return False
    elif type(arg) == False:
        return True
    else:
        return 'boolean expected'


def total_cups(n):
    for i in n:
        if i == 6:
            return i = i + 1

#Wow holy shit! got this on my own
def score_calculator(easy, medium, hard):
    if easy < 0 or medium <0 or hard <0:
        return 'invalid'
    else:
        return (easy*5)+(medium*10)+(hard*20)

#On my own too! Nice
def vol_pizza(radius, height):
    return round((radius**2) * (height * 3.14))

#Checks whehter 2 numbers are zero, negative, or positive
def both(n1, n2):
    if n1 or n2 < 0:
        return False
    elif n1 and n2 > 0:
        return True
    elif n1 == n2:
        return True
    else:
        return False

#Oh shit! Got through w some help here
def get_multiplied_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i * 2)
    return new_list #Make sure to return so doesn't return None
