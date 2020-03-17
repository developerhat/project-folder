#Writing a script to open page
#Importing webbrowser module
import webbrowser

#webbrowser.open('https://www.google.com/maps/place/' + address, new =1, autoraise = True)
#webbrowser.open('http://www.google.com/?#q=' + google_search, new =1, autoraise = True)

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
            False
            print('Thank you for using the Page Opener program! :) ')
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

    #if user_answer.lower() == 'y':
    #    continue
#Have a feeling this is how we solve this
