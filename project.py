import tkinter as tk
from tkinter import * 
from tkinter import filedialog
import pyautogui
import PIL
from PIL import Image,ImageTk
import pytesseract

root = tk.Tk()
root.title("Image to Text Converter")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


logo = Image.open('logo.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


def open_file():
    browse_text.set("loading...")
    file_path = filedialog.askopenfilename()
    try:
        imgObj = Image.open(file_path)
        txt = pytesseract.image_to_string(imgObj)        
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, txt)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Select Image")

    except IOError:
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        txt = "Please select an Image File."
        text_box.insert(1.0, txt)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        browse_text.set("Select Image")

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
browse_text.set("Select Image")
browse_btn.grid(column=1, row=1)

instructions = tk.Label(root, text="Text : ", font="Raleway")
instructions.grid(columnspan=2, column=0, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()