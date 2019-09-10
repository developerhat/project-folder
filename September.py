#usr/bin/python

#filename = 'my_new_file.txt'
#Trying to figure out why this won't open the file
#Why won't this print? works in Testing.py
try:
    with open('my_new_file.txt', mode = 'r') as filename:
        contents = print(filename.read())
except:
    print('file not found')
