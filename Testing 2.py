from tkinter import *

root = Tk()
root.title("Zandre image 2")

x = PhotoImage(file="Tkinter\PutinFunny.png")
x = x.subsample(10)  # Scale down the image

label = Label(root, image=x)
label.pack()

root.mainloop()