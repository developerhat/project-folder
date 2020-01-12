#Creating a login program


print('Welcome to our very own login program! ')
print(\n)


def create_account():
    pass

def authenticate_account():
    pass

user_list = []
pass_list = []

prompt = str(input("First, we'll need a username and password. Do you have an account with us? Y/N: "))

#The skeleton here
#if prompt.lower() == 'n':
#    print("Let's create an account! Follow the steps below.")
#    create_account() #If they don't have acc, create account function
#elif prompt.lower() == 'y':
#    authenticate_account() #Authenticate account here
#else:
    #Add exception handling, maybe put in a loop



if prompt.lower() == 'n':
    print("Let's create an account! Follow the steps below.")
    username = str(input("First, let's create a username: "))
    user_list.append(username)
    password = input("Now, create a password (8 chars only): ")
    pass_list.append(password)
elif prompt.lower() == 'y':
    authenticate_account() #Authenticate account here
else:
    #Add exception handling, maybe put in a loop?
    
    #Next steps: Need to add a way to validate password, work w text file, etc
    #Good progress tho!
