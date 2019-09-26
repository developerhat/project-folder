#usr/bin/python

#filename = 'my_new_file.txt'
#Trying to figure out why this won't open the file
#Why won't this print? works in Testing.py
#try:
#    with open('my_new_file.txt', mode = 'r') as filename:
#        contents = print(filename.read())
#except:
#    print('file not found')



#Just random problem solving on Edabit below

#Function below can convert minutes to seconds
def convert(minutes):
    return minutes * 60

#Convertion hours to seconds
def how_many_seconds(hours):
    return hours * 3600

#Converts hours & minutes to seconds
def minutes_and_hours(hours, minutes):
    return hours * 3600, minutes * 60


MAGIC_NUM = 5

def magic(num):
    return num + 2 * 10

result = magic(MAGIC_NUM)

print(result)
