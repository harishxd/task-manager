import tkinter as tk
from tkinter import messagebox
import task_backend   #importing the logic file

root = tk.Tk()
root.title("🔥 Task Manager Pro")
root.geometry("500x600")   
root.config(bg="#1e1e2f")

#Functions
def add_task():
    task = entry.get()
    if task_backend.add_task(task):
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if task_backend.delete_task(task):
            listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        old_task = listbox.get(selected)
        new_task = entry.get()

        if task_backend.update_task(old_task, new_task):
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def load_selected(event):
    try:
        selected = listbox.curselection()[0]
        entry.delete(0, tk.END)
        entry.insert(0, listbox.get(selected))
    except:
        pass

#UI
title = tk.Label(root, text="Task Manager 🚀",
                 font=("Arial", 22, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, ipady=6)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack()

tk.Button(btn_frame, text="Add", bg="green", fg="white",
          command=add_task).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", bg="blue", fg="white",
          command=update_task).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", bg="red", fg="white",
          command=delete_task).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, font=("Arial", 14))
listbox.pack(pady=20, fill=tk.BOTH, expand=True)

listbox.bind("<<ListboxSelect>>", load_selected)

root.mainloop()