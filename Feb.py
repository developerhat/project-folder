

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
