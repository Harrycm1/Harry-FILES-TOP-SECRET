from tkinter import *
root = Tk()

def click():
    global count
    count +=1
    label_text.set(count)

def print_text():
    print(box.get())

count = 0
label_text = IntVar()
label_text.set(0)

button1 = Button(root, text = "+", bg = "Black", fg = "Pink", font = ("Arial 35 bold"), command = click)
button1.pack(fill=X)

box = Entry(root, justify = CENTER)
box.pack(fill = X, ipady = 10)

button_print = Button(root, text = "Print", width = 10, command = print_text)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()