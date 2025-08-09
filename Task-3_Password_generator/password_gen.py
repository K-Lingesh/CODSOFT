import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="#f0f0f0")


title = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)


length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Enter Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
length_label.pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=5, font=("Helvetica", 12))
length_entry.pack(side=tk.LEFT, padx=10)


generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white")
generate_button.pack(pady=10)


password_display = tk.Entry(root, font=("Helvetica", 14), justify='center', state='readonly', width=30)
password_display.pack(pady=5)


root.mainloop()
