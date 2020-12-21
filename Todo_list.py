#To do list


todo_list = []

user_input = str(input("What do you need to accomplish today? "))

todo_list.append(user_input)

print(todo_list)

user_choice = str(input("Would you like to add more to the list? Y/N: "))

if user_choice.lower() == 'y':
    user_input = str(input("What're we adding this time? "))
    todo_list.append(user_input)
    print("The current list is: ", todo_list)
elif user_choice.lower() == 'n':
    print("No problem! Enjoy your day :) Exiting program.. ")
