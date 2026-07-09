import tkinter as tk 
from math import *

root = tk.Tk()
root.title("codsoft scientific calculator")
root.geometry("430x620")
root.configure(bg="black")
expression = ""

#  ------------------ Functions ----------------

def click(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def delete():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculator():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# ------------------Display ----------------

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial",16),
    justify="right",
    bd=10,
    relief=tk.RIDGE,
    bg="white",
    fg="black"
)

display.grid(row=0, column=0, columnspan=6,
             ipadx=5, ipady=10, sticky="nsew")

# ------------------Button Style ----------------

blue = "#1E3A8A"
red = "#D32F2F" 

buttons = [
    ("sin",1,0),("cos",1,1),("tan",1,2),("log",1,3),("ln",1,4),("√",1,5),

    ("sin⁻¹",2,0),("cos⁻¹",2,1),("tan⁻¹",2,2),("x²",2,3),("x³",2,4),("π",2,5),

    ("(",3,0),(")",3,1),("%",3,2),("!",3,3),("e",3,4),("^",3,5),

    ("7",4,0),("8",4,1),("9",4,2),("/",4,3),("DEL",4,4),("AC",4,5),

    ("4",5,0),("5",5,1),("6",5,2),("*",5,3),("nCr",5,4),("nPr",5,5),

    ("1",6,0),("2",6,1),("3",6,2),("-",6,3),("Ans",6,4),("Deg",6,5),

    ("0",7,0),(".",7,1),("+",7,2),("=",7,3),("M+",7,4),("M-",7,5),
]

for text,row,col in buttons:

    color = blue 
    if text in ["DEL","AC"]:
        color = red
    
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            bg=color,
            fg="White",
            font=("Arial",10,"bold"),
            command=calculator
        )
    elif text == "AC":
        btn = tk.Button(
            root,
            text=text,
            bg=color,
            fg="white",
            font=("Arial",10,"bold"),
            command=clear
        )
    elif text == "DEL":
        btn = tk.Button(
            root,
            text=text,
            bg=color,
            fg="white",
            font=("Arial",10,"bold"),
            command=delete
        )      
    else:
        btn = tk.Button(
            root,
            text=text,
            bg=color,
            fg="white",
            font=("Arial",10,"bold"),
            width=5,
            height=2,
            command=lambda t=text: click(t)
        )
    
    btn.grid(row=row,
             column=col,
             padx=2,
             pady=2,
             ipadx=15,
             ipady=15,
             sticky="nsew")
    
# Make grid responsive
for i in range(8):
    root.grid_rowconfigure(i, weight=1)

for i in range(6):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()




    
      
