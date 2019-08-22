#!/usr/bin/env python
#Practicing code head1st Python
from datetime import datetime
import sys
import os

odds = [1, 3, 9, 11, 15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

#For some reason, this only prints date & time for December 24, 2018. Why?
#Tried editting file to today (08/10/19) but still not working. Not scalable
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print ("This minute seems a little odd..")
else:
    print ("Not an odd minute!")


print(sys.version)
print (sys.platform)
#The above code will print the system platform


os.getcwd()
