from tkinter import *
from tkinter import ttk

root = Tk()
root.title('GUI Application')
#Renaming title of window

def callback():
    label.config(text = 'You clicked me', fg = 'red', bg= 'grey')

def EntryButton():
    val1 = entry.get()
    val2 = entry2.get()
    print('Your name is: ' + val1)
    print('Your password is: ' + val2)

root.geometry('500x450')

button1 = Button(root, text = "Click Me", command = callback)

button1.pack()

label = Label(root,text = 'Hello World!', fg= 'grey', bg = 'yellow', wraplength = '150')
label.config(font = 'Helvetica 20')

label.pack()

entry = ttk.Entry(root, width = 30)
entry.insert(0, 'Please enter your username')
entry.pack()

entry2 = ttk.Entry(root, width = 30)
entry2.insert(0, 'Please enter your password')
entry2.config(show = '*')

entrybutton = ttk.Button(root, text = 'Enter', command = EntryButton)
entrybutton.pack()

entry2.pack()

#Commenting this stuff because .grid() and .pack() can not be used in same program
#lbltitle = ttk.Label(text = 'Im a Title', font = (('Arial'), 22))

lblname = ttk.Label(text = 'Username: ')
lblpass = ttk.Label(text = 'Password: ')
#lbltitle.grid(row = 0,column = 0)
#lblname.grid(row = 1,column = 0)

#Did a test below. Our goal is to place username & password next to the entry fields
#If using pack, the entry field automatically places below. Almost like a "list" structure
#Practicing using .grid() on gui3.py

#Can actually use grid and place(), but not under the same FRAME
#Look up what this means^^?


lblname.pack()
lblpass.pack()

root.mainloop()
