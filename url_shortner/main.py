import pyshorteners
from tkinter import *

# firstly we will make a window here. we can take that window from tkinter using tk class and named it as win

win = Tk()
win.geometry('400x270')
win.configure(bg="navy blue")
# button fuction
def short():
    url = input1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    input2.insert(END, s )
# Label for entering user url
Label(win,text="Enter Your Url link", font='impack 17 bold', bg= 'black', fg='white').pack(fill='x')
# input box 
input1 = Entry(win,font='10', bd= 3, width= 40)
input1.pack(pady= 30 )

Button(win, text="Short it ", font="impack 12 bold", bg="blue", fg= "white", width= 14, command=short).pack()

# entry
input2 = Entry(win , font="impack 16 bold", bg="navy blue", width=24, bd= 0)
input2.pack(pady=30)

# now we are using mainloop fuction to finally make the window
mainloop()
