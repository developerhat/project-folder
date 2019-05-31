#usr/bin/python

from tkinter import *

root = Tk()
#Renaming title of window
root.title('Food Calculator')
root.geometry('300x300')
root.resizable(width = False, height = False)
root.configure(bg='gray77')

name = StringVar()
world = StringVar()

def print_name():
    name.set('Patrick')

def hello_world():
    world.set('Hello World!')


#label1 = Label(root, text = 'P1')
#label1.place(x=100, y=50)

#label2 = Label(root, text = "P2")
#label2.place(x=50,y=50)

#label3 = Label(root, text = "P3")
#label3.place(x=50, y=100)
#Placed P1-4 in all 4 corners of the program
#label4 = Label(root, text = 'P4')
#label4.place(x=100, y=100)

#label5 = Label(root, textvariable=name)
#label5.place(x = 75, y = 150)

#label6 = Label(root, textvariable=world)
#label6.place(x=150, y = 150)

#btn1 = Button(root, text = "Click me", command = lambda: print_name())
#btn1.place(x = 10, y =0)

#btn2 = Button(root, text = "Display..", command = lambda: hello_world())
#btn2.place(x = 100, y = 0)

v = IntVar()


label = Label(root, text= "Choose an Item", bg="gray77")
label.place(x=100, y=10)

r_btn = Radiobutton(root, text = "Banana", bg="gray77", variable = v, value=0)
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text = "Apple", bg="gray77", variable = v, value=1)
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text = "Mango", bg="gray77", variable = v, value=2)
r_btn3.place(x=5, y=90)

inText = Label(root, text="Result:", bg="gray77")
inText.place(x=0, y=130)

inWindow = Entry(root, width = 20)
inWindow.place(x=70, y=130)

inWindow2 = Entry(root, width = 20)
inWindow2.place(x=70, y=160)


r_btn4 = Button(root, text="Calculate", highlightbackground = 'gray77')
r_btn4.place(x=0, y = 160)








root.mainloop()
