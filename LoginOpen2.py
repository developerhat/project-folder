#Login program + Opening pages program

import webbrowser
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
logout = 1

while attempts_counter or logout > 0 :
    user_login = str(input("Username: "))
    if user_login in username_list:
        print("Username found! Please enter a password")
        pass_login = input("Password: ")
        if pass_login in password_list:
            print("Authenticated! Hooray!")
            #break
            print('Which website are we visiting today?\n')

            print('1 - LinkedIn')
            print('2 - Glassdoor')
            print('3 - Reddit')
            print('4 - YouTube')
            print('5 - Enter a URL')

            user_answer = '' #Placeholder here

            while user_answer.lower() != 'n': #Wow, this works, but it's a bit clunky. Y/N do th opposite of what it's supposed to do..
                user_choice = int(input(''))
                if user_choice == 1:
                    webbrowser.open('https://linkedin.com', new =1, autoraise = True)
                    user_answer = str(input('Great! Would you like to open another page? Y/N: '))
                    if user_answer.lower() == 'y':
                        True
                        print("What're we opening this time?: ")
                    else:
                        attempts_counter = attempts_counter - 4 #Trying to break the nested while loop above us, seems like this portion works but after hitting N for this loop, loop continues to ask for username
                        logout = logout - 2 #Supposed to stop it here.. keep workin!
                        print('Thank you for using the Page Opener program! :) ')
                        print(logout) #So prints value as -1, but doesn't end loop.. maybe b/c loop is scoped outside of program?
                        False
                elif user_choice == 2:
                    webbrowser.open('https://glassdoor.com', new =1, autoraise = True)
                    user_answer = str(input('Great! Would you like to open another page? Y/N: '))
                    if user_answer.lower() == 'y':
                        True
                        print("What're we opening this time?: ")
                    else:
                        False
                        print('Thank you for using the Page Opener program! :) ')

                elif user_choice == 3:
                    webbrowser.open('https://reddit.com', new =1, autoraise = True)
                    user_answer = str(input('Great! Would you like to open another page? Y/N: '))
                    if user_answer.lower() == 'y':
                        True
                        print("What're we opening this time?: ")
                    else:
                        False
                elif user_choice == 4:
                    webbrowser.open('https://youtube.com', new =1, autoraise = True)
                    user_answer = str(input('Great! Would you like to open another page? Y/N: '))
                    if user_answer.lower() == 'y':
                        True #How do we make it so that it just loops back to regular, without having to cancel the program?
                        print("What're we opening this time?: ")
                    else:
                        False
                        print('Thank you for using the Page Opener program! :) ')
                elif user_choice == 5:
                    webpage_name = str(input('Name of website?: '))
                    webbrowser.open('https://' + webpage_name + '.com', new =1, autoraise = True)
                    user_answer = str(input('Great! Would you like to open another page? Y/N: '))
                    if user_answer.lower() == 'y':
                        True
                        print("What're we opening this time?: ")
                    else:
                        False
                        print('Thank you for using the Page Opener program! :) ')
            else:
                #WOW THIS WORKED! Lined up while statement for page opener with this else
                #DUH!
                print('Thank you for using the Page Opener program! :) ')
                break
        elif pass_login not in password_list:
            print("Invalid password. Please try again. ")
            attempts_counter -=1
            print('Attempts left: ', attempts_counter)
    elif user_login not in username_list:
        print("Invalid username. Please try again (3 attempts max): ")
        attempts_counter -=1
        print('Attempts left: ', attempts_counter)
