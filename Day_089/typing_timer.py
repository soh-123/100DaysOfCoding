from tkinter import *
import time

# ---------------------------- INITIALIZATIONS -------------------------------- #
words = 0
counter = 0
high_score = 0
timer_running = True
timer = 10
_after_id = None

# ---------------------------- RESET -------------------------------- #
def reset():
    """reset the whole game"""
    global words, counter, timer_running, timer

    words = 0
    counter = 0
    timer_running = False
    timer = 10

    generated_text.config(state="disabled")
    generated_text.delete(1.0, END)
    press_enter.config(text="<Press enter to start>")
    number_of_words.config(text="0 Word/s")
    count_down.config(text="")
    max_long_time.config(text=f"Longest time: {high_score}")

# ---------------------------- GAME OVER -------------------------------- #
def game_over():
    """Handle the countdown timer"""
    global timer

    stop_timer()
    timer -= 1
    count_down.config(text=f"Count down {timer}")
    if timer <= 0:
        count_down.destroy()
        generated_text.config(state="disabled")
        press_enter.config(text="<Press Enter to Play Again>")
        reset()

    window.after(1000, game_over)

# ---------------------------- NO INPUT -------------------------------- #
def detect_keys(event):
    """if user didn't input for 5 seconds"""
    global _after_id

    if _after_id is not None:
        window.after_cancel(_after_id)

    _after_id = window.after(5000, game_over)

# ---------------------------- STOP TIMER -------------------------------- #
def stop_timer():
    """Stop time_counter"""
    global timer_running
    timer_running = False

# ---------------------------- TIME COUNTER -------------------------------- #
def time_counter():
    global counter, high_score

    if timer_running:
    
        max_long_time.config(text=f"Longest time: {high_score}")
        counter += 1

        try:
            with open("Day_089/high_score.txt", "r") as file:
                high_score = float(file.read())
        except ValueError:
                high_score = 0

        if counter > high_score:
            with open("Day_089/high_score.txt", "w") as file:
                file.write(str(counter))

        window.after(5000, time_counter)

# ---------------------------- KEYBOARD FUNCTIONS -------------------------------- #
def disable_backspace(event):
    """prevent the user from deleting the input"""
    if event.keysym == "BackSpace":
        return "break"

def word_couter(event):
    """count number of words per space press"""
    global words
    if event.keysym == "space":
        words += 1 
        number_of_words.config(text=f"{words} Word/s")

def start_game(event):
    """let the user stary typing"""
    if event.keysym == "Return":
        generated_text.config(state= "normal")
        press_enter.destroy()
        time_counter()

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Keep writing")
window.config(padx=20, pady=20, background="#000000")

#top informations
count_down = Label( background="#000000", font=("Tahoma", 15), fg="red")
count_down.grid(column=0, row=0)

number_of_words = Label(text=f"0 Word/s", background="#000000", font=("Tahoma", 15))
number_of_words.grid(column=2, row=0)

max_long_time = Label(text=f"Longest time: {high_score}", background="#000000", font=("Tahoma", 15))
max_long_time.grid(column=3, row=0)

generated_text = Text(window, fg="#fafafa", bg="#000000", font=("Tahoma", 18),height=8, width=70, wrap="word")
generated_text.grid(column=0, row=1, rowspan=3, columnspan=4, pady=35)
generated_text.focus()
generated_text.config(state= "disabled")
generated_text.bind("<Key>", detect_keys)

generated_text.bind("<BackSpace>", disable_backspace)
generated_text.bind("<space>", word_couter)
generated_text.bind("<Return>", start_game)

press_enter = Label(text="<Press enter to start>", background="#000000", font=("Tahoma", 12, "bold"))
press_enter.grid(column=2, row=8)

window.mainloop()