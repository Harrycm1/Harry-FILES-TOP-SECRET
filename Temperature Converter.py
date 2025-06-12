from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(0, 0)

style = "Arial 15"

#Function to raise a frame
def show_frame(frame):
    frame.tkraise()

def quit_program():
    print("Goodbye world")
    root.destroy()

def calccenttofahr():
    try:
        n = float(user_entryfahr.get())
        centtofahr = n * 9 / 5 + 32
    #   Pray that it works
        fahrcalc.config(text = centtofahr)
    except ValueError:
        fahrcalc.config(text="Invalid input! Enter a number.")
    

#Main container frame
container = Frame(root)
container.pack(fill="both", expand=True)

#Frame 1: Main Menu
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)

title_label = Label(frame_main, text="Temperature Converter", font=("Arial", 21, "bold"))
title_label.pack(pady=10)

#Button row 
button_frame = Frame(frame_main)
button_frame.pack()

btn_cent = Button(button_frame, text="to Centigrade", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(side=LEFT, padx=10)

btn_fahr = Button(button_frame, text="to Fahrenheit", bg="red", font=style, command=lambda: show_frame(frame_fahr))
btn_fahr.pack(side=LEFT, padx=10)

#Frame 2: To Centigrade
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

Label(frame_cent, text="Enter temperature in Fahrenheit", font=("Arial", 18, "bold")).pack(pady=20)
user_entrycent = Entry(frame_cent)
user_entrycent.pack()

Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()

#Frame 3: To Fahrenheit
frame_fahr = Frame(container)
frame_fahr.place(relwidth=1, relheight=1)

Label(frame_fahr, text="Enter temperature in Centigrade", font=("Arial", 18, "bold")).pack(pady=20)
user_entryfahr = Entry(frame_fahr)
user_entryfahr.pack()

fahrcalc = Label(frame_fahr, text = "calculated number goes here")
fahrcalc.pack()
calcbutton2 = Button(frame_fahr, text="Calculate", command=calccenttofahr).pack()
Button(frame_fahr, text="Back", command=lambda: show_frame(frame_main)).pack()

#Show main menu initially
show_frame(frame_main)

root.mainloop()
