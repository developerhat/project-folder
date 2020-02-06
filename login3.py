#Login program 3.0


print("Login program 3.0! ")

user_list = []
pass_list = []
#Create variables for storing user supplied data

user_input = str(input("Time to create an account! Please enter a username: "))
user_list.append(user_input) #Whatever they enter, store in list

pass_input = input('Awesome! Now, time to create a password: ')
pass_list.append(pass_input)

username = str(input("Great! Now it's time to login. Please enter username: "))


#Need to fix this loop 
while username not in user_list:
    username = str(input("Please enter username: "))
    password = input("Now password: ")
    if username and password in user_list:
        break
        print("Successfully authenticated! Hooray! :) ")
        True
    else:
        print("Please try again! ")
        False
