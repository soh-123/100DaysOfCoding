from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
new_dect = {}

try:
    data = pandas.read_csv("Day_031/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day_031/data/french_words.csv")
    new_dect = original_data.to_dict(orient="records")
else:
    new_dect = data.to_dict(orient="records")

# ---------------------------- NEXT CARD ---------------------------

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list(new_dect))
    the_card.itemconfig(white_img, image=front_card)
    the_card.itemconfig(french_word, text=current_card["French"], fill= "black")
    the_card.itemconfig(language, text="French", fill= "black")
    flip_timer = window.after(3000, flip_card)

# ---------------------------- FLIP CARD ---------------------------
def flip_card():
    the_card.itemconfig(white_img, image=back_card)
    the_card.itemconfig(language, text="English", fill="white")
    the_card.itemconfig(french_word, text=current_card["English"], fill="white")

def is_known():
    new_dect.remove(current_card)
    data_csv = pandas.DataFrame(new_dect)
    data_csv.to_csv("Day_031/data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ---------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#Card
front_card = PhotoImage(file="Day_031/images/card_front.png")
back_card = PhotoImage(file="Day_031/images/card_back.png")
the_card = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
white_img = the_card.create_image(400, 265, image=front_card)
language = the_card.create_text(400, 150, font=LANGUAGE_FONT)
french_word = the_card.create_text(400, 263, font=WORD_FONT)
the_card.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file="Day_031/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="Day_031/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()