from tkinter import *

def kg_to_lbs():
    kg = float(kg_input.get())
    lbs = round(kg * 2.2, 2)
    lbs_result.config(text= f"{lbs}")

window = Tk()
window.title("Kg to lbs converter")
# window.minsize(height=200, width=400)
window.config(padx=20, pady=20)

kg_input = Entry(width=7)
kg_input.insert(END, string="0")
print(kg_input.get())
kg_input.grid(column=1, row=0)

kg_label = Label(text="Kg")
kg_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

lbs_result = Label(text="0")
lbs_result.grid(column=1, row=1)

lbs_label = Label(text="Lbs")
lbs_label.grid(column=2, row=1)

button = Button(text="Calculate",command=kg_to_lbs)
button.grid(column=1, row=2)


window.mainloop()