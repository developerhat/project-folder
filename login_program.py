#Login Program Function

def authenticate():
    attempts = 5 #5 attempts max

    print("Welcome to the Login Program! \n")
    user_list = []
    pass_list = []
    print("Let's start by creating an account \n")


    username = str(input("Enter a username: "))
    password = input("Enter a password: ")

    #Storing user provided input in the lists
    user_list.append(username)
    pass_list.append(password)

    print("Let's login Now!\n" )

    while attempts > 0:
        user_login = str(input("Username: "))
        if user_login not in user_list:
            attempts -=1
            print("Try again! Attempts left: ", attempts)
            continue
        elif user_login in user_list:
            print("Valid username! Now, enter password below")
            pass_login = input("Password: ")
            if pass_login not in pass_list:
                attempts -=1
                print("Damn! Start over. Attempts left: ", attempts) #Make it so that don't have to start over again? Maybe just from password?
            elif pass_login in pass_list:
                print("AWESOME!! Authenticated! ")
                break
    else:
        print("Darn! Execute again")
