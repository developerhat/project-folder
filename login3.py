#Login program 3.0


print("Login program 3.0! ")

user_list = []
pass_list = []
#Create variables for storing user supplied data

user_input = str(input("Time to create an account! Please enter a username: "))
user_list.append(user_input) #Whatever they enter, store in list

pass_input = input('Awesome! Now, time to create a password: ')
pass_list.append(pass_input)

#username = str(input("Great! Now it's time to login. Please enter username: "))
attempts_counter = 0

while attempts_counter < 3:
    username = str(input("Time to login! Please enter username: "))
    password = input("Now password: ")
    if username in user_list and password in pass_list:
        print("Successfully authenticated! Hooray! :) ")
        False
        break
    else:
        print("Invalid credentials. Please try again! 3 attempts max. ")
        attempts_counter +=1 #Adding for each attempt
        True
        if attempts_counter == 3:
            print("Maximum attempts reached! Please try again later. ")
