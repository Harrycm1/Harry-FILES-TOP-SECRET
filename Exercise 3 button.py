
from tkinter import *

def click():
    global count
    count +=1
    label_text.set(count)

root = Tk()
root.title("Exercise 3")

count = 0
label_text = IntVar()
label_text.set(0)

label_1 = Label(root, font = "Calibri 40 bold",
                textvariable = label_text)
label_1.pack()

button1 = Button(root, text = "Don't click me", bg = "Black", fg = "Pink", font = ("Arial 35 bold"), command = click)
button1.pack(fill=X)

root.mainloop()