from tkinter import *
import random

root = Tk()

count = 0
count_var = IntVar()
count_var.set(0)

def quit_program():
    print("Goodbye world")
    root.destroy()

def ransom():
    global count
    count += 1
    count_var.set(count)
    die1_value = random.randint(1, 6)
    die2_value = random.randint(1, 6)  # Make both dice range 1-6

    label_die1.config(text=str(die1_value))
    label_die2.config(text=str(die2_value))

    if die1_value == 6 and die2_value == 6:
        label_die1.config(bg="green")
        label_die2.config(bg="green")
    else:
        label_die1.config(bg="red")
        label_die2.config(bg="red")

a = Button(root, text="Quit", width=10, command=quit_program)
a.grid(row=0, column=0)

b = Button(root, text="Random", width=10, command=ransom)
b.grid(row=0, column=1)

label_die1 = Label(root, font="Arial 10 bold", bg="red")
label_die1.grid(row=1, column=0)

label_die2 = Label(root, font="Arial 10 bold", bg="red")
label_die2.grid(row=1, column=1)

label1 = Label(root, text="roll count = ")
label1.grid(row=3, column=0)

label2 = Label(root, textvariable=count_var)
label2.grid(row=3, column=2)

root.mainloop()
