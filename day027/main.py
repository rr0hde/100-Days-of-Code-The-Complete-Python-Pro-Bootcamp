from tkinter import *


def button_clicked():
    mi = float(text_input.get())
    mi_to_km = mi * 1.609
    calc_label.config(text=f"{mi_to_km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

text_input = Entry(width=10)
text_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

main_label = Label(text="is equal to")
main_label.grid(column=0, row=1)

calc_label = Label(text="0")
calc_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
