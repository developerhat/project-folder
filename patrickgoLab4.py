###########################################################
# CIS 117 Python Programming: Lab #4
#
# Programming with Text Data, Files and Exceptions
#
#
###########################################################

#usr/bin/python

#Code below validates user input & reads input file
#Storing txt file contents in read_me
while True:
    read_user_prompt = str(input('Please enter filename for input: '))
    try:
        #If user input is valid, open file & store contents in read_me
        if read_user_prompt == 'lab4demo.txt':
            read_me = open(read_user_prompt, 'r')
            break
    except:
        continue

#Storing txt file in a different variable for reading
#splitlines() separates each line as list item & stores in a list
contents = read_me.read()
grocery_list = contents.splitlines()

#This will return True if a colon is present
grocery_list = filter(lambda x: ':' in x, grocery_list)

#Map() is being used to separate ': ' in txt file (grocery_list)
#After splitting, store values in list
grocery_list = list(map(lambda x: x.split(': '), grocery_list))
print(grocery_list)


#Code below calculates total for items in input txt file.
total = 0
for item in grocery_list:
    total += round(float(item[1]), 2)
#Round figure to 2 decimal places

#Requesting & validating user input for output txt file
while True:
    write_user_prompt = str(input('Please enter filename for output: '))
    try:
        if write_user_prompt == 'patrickgoLab4out.txt':
            write_me = open(write_user_prompt, 'w')
            break
    except:
        continue

#Writing data to patrickgoLab4out.txt. If file doesn't exist, create it
out_file = open('patrickgoLab4out.txt', 'w+')
#Print items in grocery_list
for item in grocery_list:
    print (out_file, item)
out_file.close()

#Adding all values from original .txt file
print('Total is: ', total)

#Program Output:

#Please enter filename for input: lab4demo.txt
#[['Binder paper', '2.29'], ['Mop', '7.50'], ['Scouring pads', '5']]
#Please enter filename for output: patrickgoLab4out.txt
#<_io.TextIOWrapper name='patrickgoLab4out.txt' mode='w+' encoding='UTF-8'> \
#['Binder paper', '2.29']
#<_io.TextIOWrapper name='patrickgoLab4out.txt' mode='w+' encoding='UTF-8'> \
#['Mop', '7.50']
#<_io.TextIOWrapper name='patrickgoLab4out.txt' mode='w+' encoding='UTF-8'> \
#['Scouring pads', '5']

#Total is:  14.79
