import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
from datetime import datetime, timedelta

# Global variable to hold tasks
tasks = []

# File to save and load tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from the JSON file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to the JSON file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Function to add a task
def add_task():
    task_name = entry_task.get()
    task_priority = priority_var.get()
    due_date = entry_due_date.get()
    
    if task_name == "":
        messagebox.showwarning("Input Error", "Please enter a task!")
        return
    
    # Validate the date format (DD-MM-YYYY)
    try:
        datetime.strptime(due_date,"%d-%m-%Y")
    except ValueError:
        messagebox.showwarning("Date Error", "Please enter a valid date (DD-MM-YYYY)!")
        return
    
    task = {
        "name": task_name,
        "priority": task_priority,
        "due_date": due_date,
        "done": False
    }
    
    tasks.append(task)
    update_listbox()
    save_tasks()

    entry_task.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)

# Function to remove selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks[selected_task_index]["done"] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Function to edit selected task
def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = tasks[selected_task_index]

        # Open dialog to edit task name, priority, and due date
        new_task_name = simpledialog.askstring("Edit Task", "Edit Task Name:", initialvalue=task["name"])
        if new_task_name:
            task["name"] = new_task_name
        
        new_priority = simpledialog.askstring("Edit Priority", "Edit Task Priority (Low, Medium, High):", initialvalue=task["priority"])
        if new_priority:
            task["priority"] = new_priority
        
        new_due_date = simpledialog.askstring("Edit Due Date", "Edit Due Date (DD-MM-YYYY):", initialvalue=task["due_date"])
        if new_due_date:
            try:
                datetime.strptime(new_due_date, "%d-%m-%Y")  # Validate the date
                task["due_date"] = new_due_date
            except ValueError:
                messagebox.showwarning("Date Error", "Please enter a valid date (DD-MM-YYYY)!")
                return

        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Function to sort tasks by priority or due date
def sort_tasks():
    sort_by = simpledialog.askstring("Sort By", "Sort by (priority/due_date):")
    if sort_by == "priority":
        tasks.sort(key=lambda task: task["priority"])  # Sorting based on priority
    elif sort_by == "due_date":
        tasks.sort(key=lambda task: datetime.strptime(task["due_date"], "%d-%m-%Y"))  # Sorting based on due date
    else:
        messagebox.showwarning("Invalid Input", "Please choose 'priority' or 'due_date'.")
        return
    update_listbox()
    save_tasks()

# Function to filter tasks by search query
def search_tasks():
    search_query = entry_search.get().lower()
    filtered_tasks = [task for task in tasks if search_query in task['name'].lower()]
    listbox.delete(0, tk.END)
    for task in filtered_tasks:
        display_text = f"{task['name']} - {task['priority']} - Due: {task['due_date']}"
        if task['done']:
            display_text = f"{display_text} (Done)"
        listbox.insert(tk.END, display_text)

# Function to update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"{task['name']} - {task['priority']} - Due: {task['due_date']}"
        if task['done']:
            display_text = f"{display_text} (Done)"
        listbox.insert(tk.END, display_text)

# Function to switch between light and dark mode
def toggle_theme():
    current_bg = root.cget("bg")
    if current_bg == "#ffffff":  # Light mode
        root.config(bg="#2e2e2e")
        entry_task.config(bg="#4f4f4f", fg="white")
        entry_due_date.config(bg="#4f4f4f", fg="white")
        entry_search.config(bg="#4f4f4f", fg="white")
        listbox.config(bg="#4f4f4f", fg="white")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.config(bg="#2e2e2e", fg="blue")
    else:  # Dark mode
        root.config(bg="#ffffff")
        entry_task.config(bg="#ffffff", fg="black")
        entry_due_date.config(bg="#ffffff", fg="black")
        entry_search.config(bg="#ffffff", fg="black")
        listbox.config(bg="#ffffff", fg="black")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.config(bg="#ffffff", fg="black")

# Function to show reminders for upcoming tasks
def show_reminders():
    now = datetime.now()
    for task in tasks:
        task_due_date = datetime.strptime(task["due_date"], "%d-%m-%Y")
        if task_due_date <= now + timedelta(days=1) and not task["done"]:
            messagebox.showinfo("Reminder", f"Task '{task['name']}' is due soon: {task['due_date']}")

# Function to create the GUI window
def create_gui():
    global entry_task, entry_due_date, entry_search, listbox, priority_var, root

    # Create root window
    root = tk.Tk()
    root.title("Advanced To-Do List Application")
    root.geometry("600x600")  # Set the window size

    # Task name input field
    tk.Label(root, text="Task:").pack(pady=5)
    entry_task = tk.Entry(root, width=40)
    entry_task.pack(pady=5)

    # Priority dropdown
    tk.Label(root, text="Priority:").pack(pady=5)
    priority_var = tk.StringVar(value="Medium")
    priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
    priority_menu.pack(pady=5)

    # Due date input field (DD-MM-YYYY format)
    tk.Label(root, text="Due Date (DD-MM-YYYY):").pack(pady=5)
    entry_due_date = tk.Entry(root, width=40)
    entry_due_date.pack(pady=5)

    # Search bar for filtering tasks
    tk.Label(root, text="Search Task:").pack(pady=5)
    entry_search = tk.Entry(root, width=40)
    entry_search.pack(pady=5)
    entry_search.bind("<KeyRelease>", lambda event: search_tasks())

    # Buttons for adding, removing, editing, marking as done, sorting, etc.
    add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
    add_button.pack(pady=5)

    remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
    remove_button.pack(pady=5)

    done_button = tk.Button(root, text="Mark as Done", width=20, command=mark_done)
    done_button.pack(pady=5)

    edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
    edit_button.pack(pady=5)

    sort_button = tk.Button(root, text="Sort Tasks", width=20, command=sort_tasks)
    sort_button.pack(pady=5)

    theme_button = tk.Button(root, text="Change Theme", width=20, command=toggle_theme)
    theme_button.pack(pady=5)

    reminder_button = tk.Button(root, text="Show Reminders", width=20, command=show_reminders)
    reminder_button.pack(pady=5)

    # Listbox to display tasks
    listbox = tk.Listbox(root, width=50, height=12, selectmode=tk.SINGLE)
    listbox.pack(pady=10)

    # Scrollbar for the listbox
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Load tasks from the file
    global tasks
    tasks = load_tasks()
    update_listbox()

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
