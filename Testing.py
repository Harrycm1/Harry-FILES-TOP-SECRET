from tkinter import *

root = Tk()

#Sizing inside window
root.title("Excercise 1")
root.geometry("400x400")
root.resizable(0,0)
root.configure(bg="#879e82")

#Adding labal
x = Label(root, text = "Hello Zandre",
          bg = "Black", fg = "White", 
          font = "Arial 30 bold")
x.pack()


root.mainloop()