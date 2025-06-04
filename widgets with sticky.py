from tkinter import *

root = Tk()

root.rowconfigure(0, minsize = 50)
root.columnconfigure([0, 1, 2, 3], minsize = 50)

label1 = Label(text = "0", bg = "black", fg = "white")
label2 = Label(text = "1", bg = "black", fg = "white")
label3 = Label(text = "2", bg = "black", fg = "white")
label4 = Label(text = "3", bg = "black", fg = "white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky = "ew")
label3.grid(row=0, column=2, sticky = "ns")
label4.grid(row=0, column=3,  sticky = "nesw")

root.mainloop()