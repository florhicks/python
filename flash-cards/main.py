from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card ={}



# ---------------------Cards functions------------------------------- #
def change_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French",fill="black")
    canvas.itemconfig(title_word, text=f"{current_card["French"]}",fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(title_word, text=f"{current_card["English"]}",fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)
def right():
    global data_dict
    data_dict.remove(current_card)
    save_words()
    change_card()



def wrong():
    change_card()


def save_words():
    file_words = pandas.DataFrame(data_dict)
    file_words.to_csv("data/words_to_learn.csv", index=False)


# ---------------------UI------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
title_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))

# Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=right)
right_button.grid(column=1, row=1)

change_card()


window.mainloop()
