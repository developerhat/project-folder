import webbrowser
import os

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
#Find some way to track logout from user, so can log out. Another while loop? fuck..
user_prompt =''
re_prompt = ''
while attempts_counter > 0:
    user_login = str(input("Username: "))
    if user_prompt.lower() or re_prompt.lower() == 'n':
        False
        print("Thank you for using THE.LOGIN.PROGRAMM!!! ")

    if user_login in username_list:
        print("Username found! Please enter a password")
        pass_login = input("Password: ")
        if pass_login in password_list:
            print("Authenticated!")
            user_prompt = 'y'
            while user_prompt.lower() != 'n':
                user_prompt = str(input('Would you like to open a new page? Y/N: '))
                if user_prompt.lower() == 'y':
                    site = str(input("Which website? Type without www & .com: "))
                    webbrowser.open('https://' + site +'.com', new =1, autoraise = True)
                    #re_prompt = str((input("Another one? Y/N: ")))
                    #if re_prompt.lower() == 'y':
                    #    True
                    #elif re_prompt.lower() == 'n':
                    #    False
                    #    break
                    #Couldn't figure this out... just removed it 
                elif user_prompt.lower() == 'n':
                    print("Thanks for using the loginopen program! :)")
                    print("Logging out...")
                    attempts_counter = -3
                    False
                    break
                    #Somewhere here?..
            else:
                break
                print("Thanks for using the loginopen programmmmm! :)")
        elif pass_login not in password_list:
            print("Invalid password. Please try again. ")
            attempts_counter -=1
            print('Attempts left: ', attempts_counter)
    elif user_login not in username_list:
        print("Invalid username. Please try again (3 attempts max): ")
        attempts_counter -=1
        print('Attempts left: ', attempts_counter)
else:
    print("Hi")
