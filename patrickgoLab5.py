###########################################################
# CIS 117 Python Programming: Lab #5
#
# Execution Control Structures, File Encoding, Using Containers
#
#
###########################################################

#usr/bin/python

#Start by validating user data with a while loop

while True:
    user_prompt = str(input('Please enter the name of input file: '))
    try:
        if user_prompt == 't5.dat':
            infile = open('t5.dat', 'r', encoding = 'utf-8')
            dict_values = {}
            break
    except:
        continue
