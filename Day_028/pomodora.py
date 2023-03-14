from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count %60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark_ckecked = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark_ckecked += "✔"
        mark.config(text=mark_ckecked)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, background=YELLOW)
title.grid(column=1, row=0)


tomato_img = PhotoImage(file="Day_028/tomato.png")
canvas = Canvas(width=224, height=220, background=YELLOW, highlightthickness=0)
canvas.create_image(120, 100, image=tomato_img)
timer_text = canvas.create_text(120, 120, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2, sticky="NSEW")

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2, sticky="NSEW")

mark = Label(fg=GREEN, bg=YELLOW)
mark.grid(column=1, row=3)




window.mainloop()