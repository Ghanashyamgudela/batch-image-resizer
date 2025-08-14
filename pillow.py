import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar
from PIL import Image

def choose_input():
    folder = filedialog.askdirectory()
    input_var.set(folder)

def choose_output():
    folder = filedialog.askdirectory()
    output_var.set(folder)

def resize_images():
    input_dir = input_var.get()
    output_dir = output_var.get()
    width = int(width_var.get())
    height = int(height_var.get())
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            in_path = os.path.join(input_dir, file)
            with Image.open(in_path) as img:
                img = img.resize((width, height), Image.LANCZOS)
                base = os.path.splitext(file)[0]
                out_path = os.path.join(output_dir, base + ".jpg")
                img.save(out_path, "JPEG")
    print("✅ Done!")

root = Tk()
root.title("Image Resizer Tool")

input_var = StringVar()
output_var = StringVar()
width_var = StringVar(value="800")
height_var = StringVar(value="800")

Label(root, text="Input Folder").grid(row=0, column=0)
Entry(root, textvariable=input_var, width=40).grid(row=0, column=1)
Button(root, text="Browse", command=choose_input).grid(row=0, column=2)

Label(root, text="Output Folder").grid(row=1, column=0)
Entry(root, textvariable=output_var, width=40).grid(row=1, column=1)
Button(root, text="Browse", command=choose_output).grid(row=1, column=2)

Label(root, text="Width").grid(row=2, column=0)
Entry(root, textvariable=width_var).grid(row=2, column=1)

Label(root, text="Height").grid(row=3, column=0)
Entry(root, textvariable=height_var).grid(row=3, column=1)

Button(root, text="Resize Images", command=resize_images).grid(row=4, column=1)

root.mainloop()
