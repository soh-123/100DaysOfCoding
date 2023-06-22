from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfReader

file_name = ""
BACKGROUND_COLOR = "#C9E792"  

# ---------------------------- CONVERT TEXT TO AUDIO ---------------------------- #
def convert_text_to_audio():
    """PDF reader"""
    global file_name
    pdf_file = PdfReader(file_name)
    pdf_text = "".join([pdf_file.pages[i].extract_text() for i in range(len(pdf_file.pages))])

    myobj = gTTS(text=pdf_text, lang='en', slow=False)
    myobj.save(f"Day_090/welcome.mp3")

# ---------------------------- FILE UPLOAD ---------------------------- #
def upload_file():
    global file_name
    file_name = filedialog.askopenfilename(filetypes=[('pdf files', '*.pdf *.docx *.doc *.txt')])
    status_label.config(text=f"File opened: {file_name}")

#------------------------------- UI ----------------------------------------#
window = Tk()
window.title("Read My File")
window.config(padx=50, pady=50, background="#C9E792")

title = Label(text="Read My File", fg="#CC9F00", bg="#C9E792", font=("Tahoma", 48, "bold"))
title.grid(column=0, row=0, columnspan=2)

sub_title = Label(text="Upload a file to read out loud", fg="#D9541A", bg="#C9E792",font=("Tahoma", 18))
sub_title.grid(column=0, row=1, columnspan=2, pady=20)

upload_button = Button(text="Upload file",  width=10, height=2, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=upload_file)
upload_button.grid(column=0, row=2)

convert_button = Button(text="Convert", bg="#D9541A", width=10, height=2, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=convert_text_to_audio)
convert_button.grid(column=1, row=2)

status_label = Label(text="", fg="#476809", bg="#C9E792",font=("Tahoma", 14))
status_label.grid(column=0, row=4, columnspan=2)

window.mainloop()