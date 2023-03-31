from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/portuguese_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
    new_word = {}


def give_new_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_dict)
    canvas.itemconfig(shown_image, image=front_card)
    canvas.itemconfig(word_text, text=new_word["english"], fill="black")
    canvas.itemconfig(language_text, text="English", fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(shown_image, image=back_card)
    canvas.itemconfig(language_text, text="Português", fill="white")
    canvas.itemconfig(word_text, text=new_word["portuguese"], fill="white")

def set_to_learn():
    data_dict.remove(new_word)
    print(len(data_dict))
    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    give_new_word()

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
shown_image = canvas.create_image(400, 263, image=front_card)
language_text = canvas.create_text(400,150, text="English", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400,263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=set_to_learn)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=give_new_word)
wrong_button.grid(column=0, row=1)

give_new_word()


window.mainloop()