from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(0, 0)

style = "Arial 15"

# Function to raise a frame
def show_frame(frame):
    frame.tkraise()

def quit_program():
    print("Goodbye world")
    root.destroy()

# -------- Main container frame ----------
container = Frame(root)
container.pack(fill="both", expand=True)

# --------- Frame 1: Main Menu ----------
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)

title_label = Label(frame_main, text="Temperature Converter", font=("Arial", 21, "bold"))
title_label.pack(pady=10)

# Button row (L and R side-by-side)
button_frame = Frame(frame_main)
button_frame.pack()

btn_cent = Button(button_frame, text="to Centigrade", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(side=LEFT, padx=10)

btn_fahr = Button(button_frame, text="to Fahrenheit", bg="red", font=style, command=lambda: show_frame(frame_fahr))
btn_fahr.pack(side=LEFT, padx=10)

# --------- Frame 2: To Centigrade ----------
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

Label(frame_cent, text="Enter temperature in Fahrenheit", font=("Arial", 18)).pack(pady=20)
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()

# --------- Frame 3: To Fahrenheit ----------
frame_fahr = Frame(container)
frame_fahr.place(relwidth=1, relheight=1)

Label(frame_fahr, text="Enter temperature in Centigrade", font=("Arial", 18)).pack(pady=20)
Button(frame_fahr, text="Back", command=lambda: show_frame(frame_main)).pack()

# Show main menu initially
show_frame(frame_main)

root.mainloop()
