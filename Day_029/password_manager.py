from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

def password_generate():
    pass_input.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    
    pass_input.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()

    new_data = {
         website:{
         "email":email,
         "password":password
         }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror("Empty input", message="Please don't leave any of the fields empty")
    else:
            with open("Day_029/data_file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                website_input.delete(0, END)
                email_input.delete(0, END)
                pass_input.delete(0, END)

# ---------------------------- UI SETUP ---------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="Day_029/logo.png")
logo = Canvas(width=200, height=200)
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=38)
email_input.grid(row=2, column=1,columnspan=2)
email_input.insert(END, string="sohier.lotfy@hotmail.com")

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", command=password_generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()