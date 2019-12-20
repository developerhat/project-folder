#Writing a script to open page
#Importing webbrowser module
import webbrowser

address = str(input('What is your address? '))
google_search = str(input("What're we Google searching for today? One word only unfortunately "))
#Request parameters from user


webbrowser.open('https://www.google.com/maps/place/' + address, new =1, autoraise = True)

webbrowser.open('http://www.google.com/?#q=' + google_search, new =1, autoraise = True)
