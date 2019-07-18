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


#btn1 = Button(root, text = "Click me", command = lambda: print_name())
#btn1.place(x = 10, y =0)

#btn2 = Button(root, text = "Display..", command = lambda: hello_world())
#btn2.place(x = 100, y = 0)

v = IntVar()

res = IntVar()

def cal_price():
    value = int(v.get())
    if value == 0:
        res.set(int(inWindow2.get()) * 4)
    elif value == 1:
        res.set(int(inWindow2.get()) * 6)
    elif value == 2:
        res.set(int(inWindow2.get()) * 10)


label = Label(root, text= "Choose an Item", bg="gray77")
label.place(x=100, y=10)

r_btn = Radiobutton(root, text = "Banana", bg="gray77", variable = v, value=0)
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text = "Apple", bg="gray77", variable = v, value=1)
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text = "Mango", bg="gray77", variable = v, value=2)
r_btn3.place(x=5, y=90)

inText = Label(root, text="Price: ", bg="gray77")
inText.place(x=0, y=130)

inWindow = Entry(root, width = 20)
inWindow.place(x=70, y=130)

inWindow2 = Entry(root, width = 20)
inWindow2.place(x=70, y=160)


r_btn4 = Button(root, text="Cal: ", highlightbackground = 'gray77', command = lambda: cal_price())
r_btn4.place(x=0, y = 160)







root.mainloop()
