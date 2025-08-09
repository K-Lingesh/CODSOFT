import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f4f7")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(root, bg="#f0f4f7")
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=5, ipady=5)

        self.add_button = tk.Button(self.frame, text="Add Task", width=12, bg="#4CAF50", fg="white",
                                    font=("Helvetica", 10, "bold"), command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE, font=("Helvetica", 12), bd=0,
                                  highlightthickness=1, relief="solid")
        self.listbox.pack(pady=10)

        self.button_frame = tk.Frame(root, bg="#f0f4f7")
        self.button_frame.pack(pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", width=12, bg="#2196F3", fg="white",
                                       font=("Helvetica", 10, "bold"), command=self.update_task)
        self.update_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", width=12, bg="#f44336", fg="white",
                                       font=("Helvetica", 10, "bold"), command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.done_button = tk.Button(self.button_frame, text="Mark as Done", width=12, bg="#9C27B0", fg="white",
                                     font=("Helvetica", 10, "bold"), command=self.mark_done)
        self.done_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task!")
        else:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to update!")
            return

        current_task = self.tasks[selected_index[0]]

        # Open a custom update dialog
        self.open_update_dialog(selected_index[0], current_task)

    def open_update_dialog(self, index, current_task):
        update_window = Toplevel(self.root)
        update_window.title("Update Task")
        update_window.geometry("400x150")
        update_window.configure(bg="#f0f4f7")

        Label(update_window, text="Edit Task:", font=("Helvetica", 12), bg="#f0f4f7").pack(pady=10)
        entry = Entry(update_window, width=40, font=("Helvetica", 12))
        entry.pack(pady=5, ipady=5)
        entry.insert(0, current_task)

        def save_updated_task():
            new_task = entry.get().strip()
            if new_task:
                self.tasks[index] = new_task
                self.update_listbox()
                update_window.destroy()

        Button(update_window, text="Save", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
               command=save_updated_task).pack(pady=10)

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return

        del self.tasks[selected_index[0]]
        self.update_listbox()

    def mark_done(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")
            return

        task = self.tasks[selected_index[0]]
        if not task.startswith("[Done] "):
            self.tasks[selected_index[0]] = "[Done] " + task
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
