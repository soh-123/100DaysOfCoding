from tkinter import *
import requests

def get_quote():
    answer = requests.get("https://api.kanye.rest")
    answer.raise_for_status() #check for errors 
    kaney_quote = answer.json()["quote"] 
    canvas.itemconfig(quote_text, text=kaney_quote)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="Day_033/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day_033/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, highlightbackground="white", background="white")
kanye_button.grid(row=1, column=0)



window.mainloop()