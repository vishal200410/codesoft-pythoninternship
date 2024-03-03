import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_index = listbox.curselection()[0]
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for adding and updating tasks
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

# Button to update tasks
update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.grid(row=0, column=2, padx=5, pady=10)

# Button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=3, padx=5, pady=10)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
