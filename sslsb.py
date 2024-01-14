import stegano
from stegano import lsb
from stegano.lsb import generators
from stegano import exifHeader
from cryptography.fernet import Fernet
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog

import os
import stegano

root = tk.Tk()
root.geometry("400x400")
root.config(bg="black")
path_buffer = ""

def encode_image():
    key = Fernet.generate_key()
    f = Fernet(key)
    message = text.get("1.0", "end-1c")
    if message=="":
        text.delete("1.0", "end-1c")
        text.insert("1.0", "No text to Hide")
    else:
        message = str(key.decode()) + str(f.encrypt(message.encode()).decode())
        if path_buffer[-3:] == "jpg":
            img = exifHeader.hide(path_buffer, "./image.jpg", message)
            print(message)
        else:
            img = lsb.hide(path_buffer, message, generators.eratosthenes())
            img.save("./image.png")
        text.delete("1.0", "end-1c")
        text.insert("1.0", "encoding successful\nImage stored as in python working directory.")

def select_image():
    global path_buffer
    if path_buffer != "":
        path_buffer = ""
    path_image = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", ".jpg"), ("png", ".png")))
    path_buffer += path_image

def decode_image():
    if path_buffer[-3:] == "jpg":
        try:
            message = exifHeader.reveal(path_buffer).decode()
            key = message[0:44].encode()
            f = Fernet(key)
            message = f.decrypt(message[44:].encode()).decode()

            if message =="":
                text.delete("1.0", "end-1c")
                text.insert("1.0", "No Hidden Message!!")
            else:
                text.delete("1.0", "end-1c")
                text.insert("1.0", message)

        except IndexError:
            text.delete("1.0", "end-1c")
            text.insert("1.0", "Unable to detect message-jpg")
    else:
        try:
            message = lsb.reveal(path_buffer, generators.eratosthenes())
            key = message[0:44].encode()
            f = Fernet(key)
            message = f.decrypt(message[44:].encode()).decode()
            text.delete("1.0", "end-1c")

            text.insert("1.0", message)
        except IndexError:
            text.delete("1.0", "end-1c")
            text.insert("1.0", "Unable to detect message-png")

tk.Button(root, command=select_image, text="Open").place(x="10", y="10")
tk.Button(root, command=encode_image, text="Encode").place(x="100", y="10")
tk.Button(root, command=decode_image, text="Decode").place(x="190", y="10")
text = tk.Text(root, height=20, width=50)
text.place(x="0", y="50")
root.title("EzStega")
tk.mainloop()