#usr/bin/python

from tkinter import *

root = Tk()
#Renaming title of window
root.title('GUI')
root.geometry('300x300')
#root.resizable(width = False, height = False)

name = StringVar()
world = StringVar()

def print_name():
    name.set('Patrick')

def hello_world():
    world.set('Hello World!')

inWindow = Entry(root)
inWindow.place(x=70, y=200)

inText = Label(root, text="Name: ")
inText.place(x=0, y=200)

label1 = Label(root, text = 'P1')
label1.place(x=100, y=50)

label2 = Label(root, text = "P2")
label2.place(x=50,y=50)

label3 = Label(root, text = "P3")
label3.place(x=50, y=100)

label4 = Label(root, text = 'P4')
label4.place(x=100, y=100)

label5 = Label(root, textvariable=name)
label5.place(x = 75, y = 150)

label6 = Label(root, textvariable=world)
label6.place(x=150, y = 150)

btn1 = Button(root, text = "Click me", command = lambda: print_name())
btn1.place(x = 10, y =0)

btn2 = Button(root, text = "Display..", command = lambda: hello_world())
btn2.place(x = 100, y = 0)












root.mainloop()
