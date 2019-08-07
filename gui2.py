from tkinter import *
from tkinter import ttk

root = Tk()
root.title('GUI Application')
#Renaming title of window

def callback():
    label.config(text = 'You clicked me', fg = 'red', bg= 'grey')



root.geometry('500x450')

button1 = Button(root, text = "Click Me", command = callback)

button1.pack()

label = Label(root,text = 'Hello World!', fg= 'grey', bg = 'yellow', wraplength = '150')
label.config(font = 'Helvetica 20')

label.pack()




root.mainloop()
