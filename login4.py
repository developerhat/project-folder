#Login 4.0 program

print("\n")
start_program = str(input("Welcome to the Login 4.0 program! Press enter to continue"))

username_list = []
password_list = []

print("Let's start by creating an account \n")

username = str(input("Please enter username: "))
password = input("Now, let's enter a password: ")
username_list.append(username)
password_list.append(password) #Storing credentials in the list

print("Great! Now, let's login \n")

attempts_counter = 3

while attempts_counter > 0:
    user_login = str(input("Username: "))
    if user_login in username_list:
        print("Username found! Please enter a password")
        pass_login = input("Password: ")
        if pass_login in password_list:
            print("Authenticated! Hooray!")
            break
        elif pass_login not in password_list:
            print("Invalid password. Please try again. ")
            attempts_counter -=1
    elif user_login not in username_list:
        print("Invalid username. Please try again (3 attempts max): ")
        attempts_counter -=1
