from tkinter import *

root = Tk()
root.title("Grid layout")

style = "Arial 20"
background = "yellow"

a = Label(root, text = "top left", bg = background, font = style)
a.grid(row = 0, column = 0, sticky = "WE")

b = Label(root, text = "top right", font = style)
b.grid(row = 0, column = 1)

c = Label(root, text = "bottom left", font = style)
c.grid(row = 1, column = 0)

d = Label(root, text = "bottom right", bg = background, font = style)
d.grid(row = 1, column = 1)

e = Label(root, text = "merge", bg = "pink", font = style)
e.grid(row = 2, column = 0, columnspan = 2, sticky = "WE")

root.mainloop()