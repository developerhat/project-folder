#PatrickGo Assignment 11.py
#Author: Patrick Go
#Date last modified: 04/11/21
#Purpose: Using nested lists

#Program uses: List comprehension practice

#Assignment 10 - Nested Lists


#Problem 1:
nested_list = [[2,3,4,5],[2,4,8,8],[3,5,7,7]]
#Declare nested list

print('Current nested list is: ', nested_list) #Display list

def nested_sum(nested_list):
    total = 0  #declare placeholder variable for result
    for i in nested_list: #iterate through the list
        if isinstance(i, list):  # checks if iterables are list type
            total += nested_sum(i) #if yes, add to placeholder variable
        else:
            total += i
    return total

print("Sum of nested list:", nested_sum(nested_list))


#Problem 2:
three_list = []
