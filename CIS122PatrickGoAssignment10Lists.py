#PatrickGo Assignment 10.py
#Author: Patrick Go
#Date last modified: 03/28/21
#Purpose: Using lists

#Program uses: List comprehension practice

#Assignment 10 - Lists

#Problem 1:
final_list = [] #create empty list

while len(final_list) < 7:
    user_list = int(input("Enter a number (7 total): ")) #Get user input, keep requesting until 7th entry
    final_list.append(user_list)

print("Your list is: ", final_list)

print('1st element: ',final_list[0], '\n3nd element: ', final_list[2], '\n7th element: ', final_list[-1]) #Display element according to list index position
print("5th to end of list: ", final_list[4::])

fruit_1 = str(input("Favorite fruit #1: "))
fruit_2 = str(input("Favorite fruit #2: "))
fruit_3 = str(input("Favorite fruit #3: ")) #Get input from user as string

final_list.append(fruit_1)
final_list.append(fruit_2)
final_list.append(fruit_3) #Add to end of list

print("Full list w/ fruits added: ", final_list)

new_list = [final_list[7::]] #Instead of using remove(), just create new list

print('After removal: ', new_list)

#Problem 2:
def list_sum():
    lst = [] #creating an empty list

#Enter length of list
    list_len = int(input("(Problem 2) Enter length of list: "))

#Iterating to form list
    for i in range(0, list_len):
        ele = int(input())
        lst.append(ele)

    return 'Your list is: ', lst

print(list_sum())



#Problem 3:
lst_7 = [] #Creating an empty list

#Enter length of list
lst_7_len = int(input("(Problem 3) Enter length of list: "))

#Creating list
for i in range(0, lst_7_len):
    elem = int(input())
    lst_7.append(elem)

print("Original list = ", lst_7)
filtered_list = []
for i in lst_7: #Filtering list values for all list values greater than 7
    if i >= 7:
        filtered_list.append(i) #Add to list if greater than 7
print("Filtered list = ", filtered_list)
