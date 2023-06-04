from PIL import ImageTk, ImageDraw
import PIL.Image
from tkinter import *
from tkinter import filedialog

# ---------------------------- VARIABLES ------------------------------- #
FONT_NAME = "Ariel"
SAVE_NAME = 'new_photo.jpg'
file_name = 0
text_id = None

# ---------------------------- PHOTO UPLOAD ---------------------------- #
def upload_file():
    global img
    global image
    global file_name

    file_name = filedialog.askopenfilename(filetypes=[('Jpg files', '*.jpg')])
    image = PIL.Image.open(file_name)
    if image.mode != "RGB":
        image = image.convert("RGB")

    canvas_width = canvas.winfo_width() 
    canvas_height = canvas.winfo_height()
    image = image.resize((canvas_width, canvas_height), PIL.Image.NEAREST)

    image.save(f'Day_084/{SAVE_NAME}')
    img = ImageTk.PhotoImage(PIL.Image.open(f'Day_084/{SAVE_NAME}'))
    canvas.create_image(0, 0, anchor=NW, image=img)

# ------------------------------ ADD WATERMARK ------------------------------ #
def add_watermark():
    global text_id
    txt = watermark_text.get()
    #text color
    color_choice = COLOR_VAR.get()
    if color_choice == 'black':
        color = '#000000'
    else:
        color = '#FFFFFF'

    #text_position
    position_choice = POS_VAR.get()
    pos_x = 20 if position_choice in [1, 3] else canvas.winfo_width() - len(txt) * 10 - 20
    pos_y = 20 if position_choice in [1, 2] else canvas.winfo_height() - 20

    canvas.delete(text_id)
    text_id = canvas.create_text(pos_x, pos_y, anchor=NW, text=txt, fill=color, font=(FONT_NAME, 16, 'bold'))
        


# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Watermark")
window.minsize(height=100, width=500)
window.config(padx=100, pady=50, background='#000000')

blank_photo = PIL.Image.new(mode="RGBA", size=(900, 900))
image1 = ImageTk.PhotoImage(blank_photo)
canvas = Canvas(highlightthickness=0)
canvas.create_image(900, 900, image=image1)
canvas.grid(column=0, row=0, columnspan=15)

upload_button = Button(text="Choose photo", width=10, command=upload_file,background='#000000', highlightthickness=0).grid(column=0, row=1, columnspan=2, pady=10)

watermark_label = Label(text="Add Text: ", background='#000000').grid(column=0, row=2, pady=10)
watermark_text = Entry()
watermark_text.grid(column=1, row=2, pady=10)

color_label = Label(text="Text Color: ", background='#000000').grid(column=0, row=3)

COLOR_VAR = StringVar()
COLOR_VAR.set('black')
r1_color = Radiobutton(text="Black", value='black', variable=COLOR_VAR, background='#000000').grid(column=0, row=4)
r2_color = Radiobutton(text="White", value='white', variable=COLOR_VAR, background='#000000').grid(column=1, row=4)

position_label = Label(text="Change text position: ", background='#000000').grid(column=3, row=3)

POS_VAR = IntVar()
POS_VAR.set(1)
r1_posiotion = Radiobutton(text="Upper Left", value=1, variable=POS_VAR, background='#000000').grid(column=3, row=4)
r2_posiotion = Radiobutton(text="Upper Right", value=2, variable=POS_VAR, background='#000000').grid(column=4, row=4)
r3_posiotion = Radiobutton(text="Bottom Left", value=3, variable=POS_VAR, background='#000000').grid(column=3, row=5)
r4_posiotion = Radiobutton(text="Bottom Right", value=4, variable=POS_VAR, background='#000000').grid(column=4, row=5)

generate_btn = Button(text="Generate", width=30, height=2,command=add_watermark, background='#000000', highlightthickness=0)
generate_btn.grid(column=0, row=6, columnspan=4,pady=40)

window.mainloop()
