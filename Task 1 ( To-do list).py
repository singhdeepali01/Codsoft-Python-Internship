from tkinter import *

# Creating the main window
window = Tk()
window.title("Deepali's To-Do List")
window.geometry("500x500")
window.config(bg="#222831") 

# List to store tasks
tasks = []

#  Function to add a task
def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END,task)
        task_entry.delete(0,END)

# Function to delete selected task
def delete_task():
    selected = task_listbox.curselection()

    if selected:
        task_listbox.delete(selected)

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0,END)

# Heading
title_label = Label(
    window,
    text="Deepali's To-Do List",
    font=("Arial",20,"bold")
)
title_label.pack(pady=20)

# Entry box

task_entry = Entry(
    window,
    width=35,
    font=("Arial",14)
)
task_entry.pack(pady=10)

# Add button
add_button = Button(
    window,
    text="Add Task",
    font=("Arial",12),
    command=add_task
)
add_button.pack(pady=10)

# Listbox to display tasks
task_listbox = Listbox(
    window,
    width=40,
    height=10,
    font=("Arial",14)
)
task_listbox.pack(pady=20)

# Delete button
delete_button = Button(
    window,
    text="Delete Task",
    font=("Arial",12),
    command=delete_task
)
delete_button.pack(pady=10)

# CLear button
clear_button = Button(
    window,
    text="Clear All ",
    font=("Arial",12),
    command=clear_tasks
)
clear_button.pack(pady=10)

# Run application
window.mainloop()
