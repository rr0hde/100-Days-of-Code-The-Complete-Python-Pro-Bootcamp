from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) or len(email) or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=E)

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(END, "brent.lacorte@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, sticky=E)

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky=W)

gen_button = Button(text="Generate Password", command=password_gen)
gen_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
