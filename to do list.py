import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

def clear_tasks():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")  # Set the size of the root window
root.configure(bg="#EDEDED")  # Set the background color of the root window

# Create a Frame for the to-do list items
task_frame = tk.Frame(root, bg="#EDEDED")  # Set the background color of the frame
task_frame.pack(padx=10, pady=10)

# Scrollbar for the task list
scrollbar = tk.Scrollbar(task_frame, orient=tk.VERTICAL)
task_list = tk.Listbox(task_frame, width=30, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, bg="#EDEDED", fg="#333333")  # Set the background and foreground colors of the listbox
scrollbar.config(command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.pack(pady=5)

# Entry field to add tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Buttons to add, remove, and clear tasks
button_frame = tk.Frame(root, bg="#EDEDED")  # Set the background color of the frame
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", padx=10, pady=5, font=("Helvetica", 12, "bold"))  # Set the background and foreground colors of the button, and increase the button size
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, bg="#f44336", fg="white", padx=10, pady=5, font=("Helvetica", 12, "bold"))  # Set the background and foreground colors of the button, and increase the button size
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear All Tasks", command=clear_tasks, bg="#2196F3", fg="white", padx=10, pady=5, font=("Helvetica", 12, "bold"))  # Set the background and foreground colors of the button, and increase the button size
clear_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
