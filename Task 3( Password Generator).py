import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# ------------------Window Setup ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x700")
root.config(bg="#FFD1DC") #Light Pink
root.resizable(False, False)

# ------------------Functions----------------

def generate_password():
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += "!@#$%^&*()+-=[]{}|;:,.<>?"

    if characters == "":
        messagebox.showwarning(
            "Warning",
            "Please select at least one option!"
        )
        return
    
    length = length_slider.get()

    # Avoid repeated characters
    if repeat_var.get():
        if length > len(characters):
            messagebox.showwarning(
                "Warning",
                "Length is too large for unique characters!"
            )
            return
        password = "".join(
            random.sample(characters, length)
        )
    else:
        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

    password_entry.delete(0, tk.END)
    password_entry.insert(0,password)


def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first!"
        )
        return

    pyperclip.copy(password)
    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )

#  ------------------- Heading ---------------------

title_lable = tk.Label(
    root,
    text="🔐Generate Strong Password",
    font=("Arial",20,"bold"),
    bg="#FFD1DC",
    fg="#C2185B"
)
title_lable.pack(pady=20)

# --------------- Password Box ---------------------

password_entry = tk.Entry(
    root,
    font=("Arial",16),
    width=28,
    justify="center",
    bd=3,
    relief="solid"
)
password_entry.pack(pady=15, ipady=8)

# ------------------- Copy Button ---------------

copy_btn = tk.Button(
    root,
    text="📋 Copy to Clipboard",
    font=("Arial",12,"bold"),
    bg="#EC407A",
    fg="white",
    width=18,
    command=copy_password
)
copy_btn.pack(pady=15)

# ----------------- Slider Section ---------------

length_frame = tk.Frame(
    root,
    bg="#F8BBD0",
    bd=2,
    relief="ridge"
)
length_frame.pack(pady=20)

length_label = tk.Label(
    length_frame,
    text="Password Length",
    font=("Arial",14,"bold"),
    bg="#F8BBD0",
    fg="#880E4F"
)
length_label.pack(pady=5)

slider_value = tk.Label(
    length_frame,
    text="12",
    font=("Arial",14,"bold"),
    bg="#F8BBD0",
    fg="#880E4F"
)
slider_value.pack()

def update_value(value):
    slider_value.config(text=str(int(float(value))))

length_slider = tk.Scale(
    length_frame,
    from_=4,
    to=30,
    orient="horizontal",
    length=220,
    command=update_value,
    bg="#F8BBD0",
    highlightthickness=0
)
length_slider.set(12)
length_slider.pack(pady=5)

# -------------------- Checkboxes -----------------

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
repeat_var = tk.BooleanVar(value=False)

checkbox_font = ("Arial", 12)

tk.Checkbutton(
    root,
    text="Include Uppercase Letters (A-Z)",
    variable=upper_var,
    bg="#FFD1DC",
    fg="#880E4F",
    font=checkbox_font
).pack(anchor="w", padx=70, pady=8)

tk.Checkbutton(
    root,
    text="Include Lowercase Letters (a-z)",
    variable=lower_var,
    bg="#FFD1DC",
    fg="#880E4F",
    font=checkbox_font
).pack(anchor="w", padx=70, pady=8)

tk.Checkbutton(
    root,
    text="Include Numbers (0-9)",
    variable=number_var,
    bg="#FFD1DC",
    fg="#880E4F",
    font=checkbox_font
).pack(anchor="w", padx=70, pady=8)

tk.Checkbutton(
    root,
    text="Include Symbols (!@#$%^&*)",
    variable=symbol_var,
    bg="#FFD1DC",
    fg="#880E4F",
    font=checkbox_font
).pack(anchor="w", padx=70, pady=8)

tk.Checkbutton(
    root,
    text="Avoid Repeating Characters",
    variable=repeat_var,
    bg="#FFD1DC",
    fg="#880E4F",
    font=checkbox_font
).pack(anchor="w", padx=70, pady=8)

# ---------------- Generate Button ----------------

generate_btn = tk.Button(
    root,
    text="🔑 Generate Password",
    font=("Arial", 15, "bold"),
    bg="#AD1457",
    fg="white",
    width=22,
    height=2,
    command=generate_password
)
generate_btn.pack(pady=40)

root.mainloop()