#usr/bin/python

import tkinter

window = tkinter.Tk()
#Renaming title of window
window.title('GUI')


#top_frame = tkinter.Frame(window).pack()
#bottom_frame = tkinter.Frame(window).pack(side = "bottom")


#btn1 = tkinter.Button(top_frame, text="Button 1", fg = "red").pack()
#FG is foreground, color of button

tkinter.Label(window, text = "Username").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)

tkinter.Label(window, text = "Password").grid(row = 1)
tkinter.Entry(window).grid(row = 1, column = 1)

# creating a function called say_hi()
#def say_hi():
#    tkinter.Label(window, text = "Hi").pack()

#tkinter.Button(window, text = "Click Me!", command = say_hi).pack()
# 'Checkbutton' is used to create the check buttons


tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)
# 'columnspan' tells to take the width of 2 columns
# you can also use 'rowspan' in the similar manner

















window.mainloop()
