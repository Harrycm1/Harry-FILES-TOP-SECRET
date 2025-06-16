from tkinter import *
from tkinter import ttk

root = Tk()
radio_var = StringVar()

#Label
answer = Label(root, text="", font=("Arial", 12, "bold"))
answer.grid(row=10, column=0, columnspan=2, pady=10)

#Combine function
def radio_call():
    value = radio_var.get()
    s2 = textbox.get()
    s3 = my_combobox.get()

    if value == "1":
        s1 = "Happy"
    elif value == "2":
        s1 = "Awesome"
    elif value == "3":
        s1 = "Outgoing"
    elif value == "4":
        s1 = "Funky"
    else:
        s1 = "Undefined"

    combined = f"{s1} {s2} {s3}"
    answer.config(text=f"You are a {combined}")

#Ajective selection
label = Label(root, text="Choose an adjective...", font=("Arial", 10, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)

option1 = ttk.Radiobutton(root, text="Happy", value="1", variable=radio_var)
option1.grid(row=1, column=0, sticky=W, padx=10)

option2 = ttk.Radiobutton(root, text="Awesome", value="2", variable=radio_var)
option2.grid(row=2, column=0, sticky=W, padx=10)

option3 = ttk.Radiobutton(root, text="Outgoing", value="3", variable=radio_var)
option3.grid(row=3, column=0, sticky=W, padx=10)

option4 = ttk.Radiobutton(root, text="Funky", value="4", variable=radio_var)
option4.grid(row=4, column=0, sticky=W, padx=10)

#Color Entry
label2 = Label(root, text="Enter a color", font=("Arial", 10, "bold"))
label2.grid(row=5, column=0, columnspan=2, pady=10)

textbox = Entry(root)
textbox.grid(row=6, column=0, sticky=W, padx=10)

#Animal Dropdown
label3 = Label(root, text="Pick an animal", font=("Arial", 10, "bold"))
label3.grid(row=7, column=0, columnspan=2, pady=10)

animals = ["Baboon", "Bee", "Cat", "Chicken", "Cougar", "Deer", "Dog", "Eagle", "Fish", "Goat",
           "Leopard", "Lion", "Megalodon", "Octapus", "Pig", "Raccoon", "Seal", "Tuna", "MONKEY"]
chosen_animals = StringVar()
chosen_animals.set("")

my_combobox = ttk.Combobox(root, textvariable=chosen_animals, state="readonly")
my_combobox['values'] = animals
my_combobox.grid(row=8, column=0, sticky=W, padx=10)

#Go Button
go = Button(root, text="GO!", font="Arial 20", command=radio_call)
go.grid(row=9, column=0, padx=10, pady=10)

root.mainloop()
