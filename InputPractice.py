#!/usr/bin/env python
import webbrowser
import requests

answer=int(input ("How many houses do you have?"))
if answer <= 10:
    print ("Number of houses: {}".format(answer) + " , that's a lot!")
else:
    print ("Number of houses: over 10? That's a lot!")

print ("enter your name!")
y = input()
print("your name is..." + y)


list = input("How much would you like to count?")
for i in range:
    print(list)

#The code below can be used to open Slack download page
#webbrowser.open('http://slack.com/download')

#Testing changes

#function for websearch
#def websearch():
#    google = input('Google search:')
#    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

#websearch()
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
