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
contents = read_me.read()
grocery_list = contents.splitlines()

def containsColon(input):
    # return True if input contains a colon,
    # return False otherwise
    if (':' in input):
        return True
    return False

grocery_list = filter(lambda x: ':' in x, grocery_list)
# grocery_list = filter(containsColon, grocery_list)

#40 & 41 are exactly the same thing

grocery_list = list(map(lambda x: x.split(': '), grocery_list))
total = 0

#Iterate through groceryList & pick out ':'
#Only format after you get total. 54 calculates total

#groceryList = list(map(lambda x: x.split(': '), groceryList))
#total = 0
for item in grocery_list:
    total += round(float(item[1]), 2)

print(total)
#Format grocery_list for left hand & right hand side



#Goal is to write to output file, with prices to left & names to right
#After calculating total,


#Look for python function that adds spaces. Function takes a string & pads accordingly to align
#Will need to add just the right amount of spacing depending on character provided, to achieve right length
#if on right side, needs to be left justified
#If on left side, needs to be right justified
#Format grocery list corresponds to each line in the output file. Make sure ---
#---input line 0 is same as output line line 0


# Item X:                       $2.45
# Item asdfadsfdasfad:       $4456.24
# Item Z:                     $334.45
# Total:                     $6799.44

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
