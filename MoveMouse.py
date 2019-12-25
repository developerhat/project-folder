#usr/bin/python

#Using web browser to scrape sites

import webbrowser
import sys
import pyperclip

user_input = str(input(sys.argv)) # Parameters will be ['mapit.py', '870', 'Valencia', 'St']

#Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #Doing formatting here
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
