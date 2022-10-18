from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

button_right_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

next_card()

window.mainloop()
