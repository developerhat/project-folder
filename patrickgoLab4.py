###########################################################
# CIS 117 Python Programming: Lab #4
#
# Programming with Text Data, Files and Exceptions
#
#
###########################################################

#usr/bin/python

#while True:
#    user_prompt = input('Please enter filename: ')
#    try:
#        read_file = open('lab4demo.txt', 'r')
#        read_file.read([n])
#    except:
#        continue

#This reads input file
while True:
    read_user_prompt = str(input('Please enter filename for input: '))
    try:
        if read_user_prompt == 'lab4demo.txt':
            read_me = open(read_user_prompt, 'r')
            break
    except:
        continue

read_me = open(read_user_prompt, 'r')


print(read_me.read())

#Goal is to write to output file, with prices to left & names to right
#Also add all together


#Not sure what I was doing here. Trying to write to new file though
while True:
    write_user_prompt = str(input('Please enter filename for output: '))
    try:
        if write_user_prompt == 'lab4demo_out.txt':
            write_me = open(write_user_prompt, 'w')
            break
    except:
        continue

write_me = open(write_user_prompt, 'w')
print(write_me.write())
#Advanced method of doing
#with open(user_prompt, 'r') as read_file:
#    for line in read_file:
#        if user_prompt in line:
#            print(line)
#            break
