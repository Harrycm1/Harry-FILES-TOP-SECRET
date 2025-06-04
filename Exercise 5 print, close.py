from tkinter import *

def quit():
    root.destroy()

def print_text():
    print(box.get())

root = Tk()
root.title("Exercise 5")
root.resizable(0,0)

box = Entry(root, justify = CENTER)
box.pack(fill = X, ipady = 10)

button_print = Button(root, text = "Print", width = 10, command = print_text)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()