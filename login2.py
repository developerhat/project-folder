#Creating login program for Python

#TO ADD: Once authenticated, take user through webopen program to open pages w google maps
import webbrowser

user_list = []
pass_list = []

print('\n')
print("Welcome to Patrick's Login Program 2.0! \n")

#Not using this function b/c just typed it in manually
#This function should authenticate user
#def authenticate(username, password):
#    if username in user_list and password in pass_list:
#        return "You've been authenticated!"

login_flow = str(input('Do you have an account with us? Y/N: '))
if login_flow.lower() == 'n':
    print("Perfect! Let's create an account for you \n")
    username = str(input('Please enter your username: '))
    user_list.append(username)
    password = input('Please enter a password: ')
    pass_list.append(password)
    print(user_list,pass_list)
    print("You've now created your accounts. Please log in: \n")
    user1 = input("Username: ")
    pass1 = input("Password: ")
    if user1 in user_list and pass1 in pass_list:
        print ('Authenticated!')
        google_search = str(input("What're we Google searching for today? One word only unfortunately "))
        webbrowser.open('http://www.google.com/?#q=' + google_search, new =1, autoraise = True)
    else:
        print ('Login failed')
    #authenticate(username,password)
elif login_flow.lower() == 'y':
    print('No, you dont! No one has an account. Nice try :) \n')
    username = str(input("Let's create one! Please enter your username: "))
    password = input('Please enter a password: ')
    user_list.append(username)
    pass_list.append(password)
    user1 = input("Username: ")
    pass1 = input("Password: ")
    print('validating your credentials....')
    if user1 in user_list and pass1 in pass_list:
        print ('Authenticated!')
        google_search = str(input("What're we Google searching for today? One word only unfortunately "))
        webbrowser.open('http://www.google.com/?#q=' + google_search, new =1, autoraise = True)
    else:
        print ('Login failed')
