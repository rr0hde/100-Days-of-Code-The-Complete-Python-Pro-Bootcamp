from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=input_.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button_new = Button(text="I'm new!")
button_new.grid(column=2, row=0)

# Entry
input_ = Entry(width=10)
input_.grid(column=3, row=2)

window.mainloop()

