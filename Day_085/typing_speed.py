from tkinter import *

# ---------------------------- VAR & CONST -------------------------------- #
count = 60
points = 0
FONT = ("Tahoma", 12)
letter_index = -1
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z space . ,"
mistakes = 0
word_per_minute = 0

# ---------------------------- RESTART -------------------------------- #
def restart():
    global count
    global mistakes
    global letter_index

    count = 60
    mistakes = 0
    letter_index = -1

    countdown()
    entry_field.delete(0, 'end')
    generated_text.tag_remove("green", "1.0", "end")
    generated_text.tag_remove("red", "1.0", "end")
    wrong_label.config(text=f"Wrong Words: {mistakes}")
    wpm_label.config(text="WPM: 0.0")


def highscore():
    global word_per_minute

    try:
        with open("Day_085/high_score.txt", "r") as file:
            high_score = float(file.read())
    except ValueError:
        high_score = 0.0

    if word_per_minute > high_score:
        with open("Day_085/high_score.txt", "w") as file:
            file.write(str(high_score))

    high_score_label.config(text=f"High Score: {high_score}")

# ---------------------------- WPM -------------------------------- #
def calculate_wpm():
    global count
    global word_per_minute

    minutes = count/60
    char_num = len(entry_field.get())

    word_per_minute = (char_num/5)/minutes
    wpm_label.config(text=f"WPM: {word_per_minute:.1f}")

# ---------------------------- DISABLE BACKSPACE -------------------------------- #
def disable_backspace(event):
    """Prevent the user from deleting any text he already input"""
    if event.keysym == "BackSpace":
        return "break"
    
# ---------------------------- COUNT DOWN -------------------------------- #
def countdown():
    """Counts down the timer per second and show the result on screen directly"""
    global count
    if count <= 0:
        time_label.config(text="Countdown finished!")
        return
    time_label.config(text=f"Time Left: {count}")
    count -= 1
    calculate_wpm()
    window.after(1000, countdown)

# --------------------------- CHECK SPELLING ------------------------------ #
def check_spelling(event):
    global letter_index
    global mistakes
    global generated_text
    global letters
    global user_input

    user_input = entry_field.get()
    test_text = generated_text.get("1.0", "end")
    
    if event.keysym == "Return":
        entry_field.config(state= "normal")
        press_enter.destroy()
        countdown()
        return

    if event.keysym in letters:
        letter_index += 1    

    if test_text[letter_index] == user_input[letter_index]:
        generated_text.tag_add("green", f"1.{letter_index}")
        generated_text.tag_config("green", foreground="green")

    else:
        mistakes += 1
        wrong_label.config(text=f"Wrong Words: {mistakes}")
        generated_text.tag_add("red", f"1.{letter_index}")
        generated_text.tag_config("red", foreground="red")

# ---------------------------- CREATE TEXT -------------------------------- #
def create_text():
    """Creates sample of 27 words"""
    global generated_text
    with open("Day_085/text_sample.txt", "r") as text:
        all_text = text.read()
        generated_text = Text(window, fg="#fafafa", bg="#000000", font=("Arial", 20, "bold"),
                                    height=4, width=70, wrap="word")
        generated_text.grid(column=0, row=1, rowspan=3, columnspan=4, pady=35)
        generated_text.insert(END, all_text.lower())

        generated_text.config(state=DISABLED)

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20, background="#000000")

#top informations
time_label = Label(text=f"Time Left: {count}", background="#000000", font=("Tahoma", 12))
time_label.grid(column=0, row=0)

wrong_label = Label(text=f"Wrong Words: {mistakes}", background="#000000", font=("Tahoma", 12))
wrong_label.grid(column=1, row=0)

wpm_label = Label(background="#000000", font=("Tahoma", 12))
wpm_label.grid(column=2, row=0)

high_score_label = Label(background="#000000", font=("Tahoma", 12))
high_score_label.grid(column=3, row=0)

input_label = Label(text="Write Below:", background="#000000", font=("Tahoma", 12, "bold")).grid(column=0, row=6)

entry = StringVar()
entry_field = Entry(window, width=80, textvariable=entry,font=("Arial", 16))
entry_field.grid(column=0, row=7, columnspan=4, pady=15)
entry_field.focus()
entry_field.config(state= "disabled")
entry_field.bind("<KeyRelease>", check_spelling)
entry_field.bind("<BackSpace>", disable_backspace)

press_enter = Label(text="<Press enter to start>", background="#000000", font=("Tahoma", 12, "bold"))
press_enter.grid(column=1, row=8)

create_text()
calculate_wpm()
highscore()

restart = Button(text="RESTART", font=FONT, bg="#000000",command=restart)
restart.grid(column=3, row=8)

window.mainloop()