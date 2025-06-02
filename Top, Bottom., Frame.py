from tkinter import *

root = Tk()
top_frame = Frame(root)
top_frame.pack(fill=X)

label1 = Label(top_frame, text = "I am a frame",
               width = "20", height = "4",
               font = ("Arial", "20", "bold"))
label1.pack(fill=X)

bottom_frame = LabelFrame(root, text = "bottom frame")
bottom_frame.pack()
label2 = Label(bottom_frame, text = "I am a label frame",
               width = "15", height = "2",
               font = ("Arial", "20", "bold"))
label2.pack()

root.mainloop()