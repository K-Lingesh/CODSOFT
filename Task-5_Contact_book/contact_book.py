import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []  
listbox_contacts = None  

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = text_address.get("1.0", tk.END).strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    messagebox.showinfo("Success", f"Contact '{name}' added!")
    clear_fields()

def view_contacts():
    global listbox_contacts

    if listbox_contacts:
        listbox_contacts.destroy()

    listbox_contacts = tk.Listbox(right_frame, width=40, height=20, bg="#f0f0f0", fg="#333", font=("Arial", 12))
    listbox_contacts.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    for i, contact in enumerate(contacts):
        listbox_contacts.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def search_contact():
    def perform_search():
        keyword = entry_keyword.get().strip()
        results_listbox.delete(0, tk.END)

        if keyword:
            found = []
            for i, contact in enumerate(contacts):
                if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
                    found.append(f"{i+1}. {contact['name']} - {contact['phone']}")

            if found:
                for item in found:
                    results_listbox.insert(tk.END, item)
            else:
                results_listbox.insert(tk.END, "No contact matched.")
        else:
            results_listbox.insert(tk.END, "Enter something to search.")

    
    search_win = tk.Toplevel(root)
    search_win.title("Search Contact")
    search_win.geometry("400x300")
    search_win.config(bg="#f0f8ff")

    tk.Label(search_win, text="Search by Name or Phone:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
    entry_keyword = tk.Entry(search_win, width=30, font=("Arial", 12))
    entry_keyword.pack(pady=5)

    btn_search_now = tk.Button(search_win, text="Search", bg="#2196F3", fg="white",
                               font=("Arial", 11), command=perform_search)
    btn_search_now.pack(pady=10)

    results_listbox = tk.Listbox(search_win, width=50, height=10, font=("Arial", 12))
    results_listbox.pack(pady=10)

def update_contact():
    global listbox_contacts

    if not listbox_contacts:
        messagebox.showwarning("Select", "First view contacts and select one to update.")
        return

    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Select", "Select a contact to update.")
        return

    index = selected[0]
    contact = contacts[index]

    
    update_win = tk.Toplevel(root)
    update_win.title("Update Contact")
    update_win.geometry("400x300")
    update_win.config(bg="#f0f8ff")

    tk.Label(update_win, text="Name:", bg="#f0f8ff", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_upd_name = tk.Entry(update_win, width=30, font=("Arial", 12))
    entry_upd_name.insert(0, contact['name'])
    entry_upd_name.grid(row=0, column=1, pady=5)

    tk.Label(update_win, text="Phone:", bg="#f0f8ff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_upd_phone = tk.Entry(update_win, width=30, font=("Arial", 12))
    entry_upd_phone.insert(0, contact['phone'])
    entry_upd_phone.grid(row=1, column=1, pady=5)

    tk.Label(update_win, text="Email:", bg="#f0f8ff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_upd_email = tk.Entry(update_win, width=30, font=("Arial", 12))
    entry_upd_email.insert(0, contact['email'])
    entry_upd_email.grid(row=2, column=1, pady=5)

    tk.Label(update_win, text="Address:", bg="#f0f8ff", font=("Arial", 12)).grid(row=3, column=0, sticky="nw", padx=10, pady=5)
    text_upd_address = tk.Text(update_win, width=23, height=4, font=("Arial", 12))
    text_upd_address.insert("1.0", contact['address'])
    text_upd_address.grid(row=3, column=1, pady=5)

    def save_update():
        new_name = entry_upd_name.get().strip()
        new_phone = entry_upd_phone.get().strip()
        new_email = entry_upd_email.get().strip()
        new_address = text_upd_address.get("1.0", tk.END).strip()

        if new_name and new_phone:
            contacts[index] = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            }
            messagebox.showinfo("Updated", "Contact updated.")
            view_contacts()
            update_win.destroy()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required.")

    btn_save = tk.Button(update_win, text="Save Changes", bg="#4CAF50", fg="white",
                         font=("Arial", 11), command=save_update)
    btn_save.grid(row=4, column=1, pady=15)

def delete_contact():
    global listbox_contacts

    if not listbox_contacts:
        messagebox.showwarning("Select", "First view contacts and select one to delete.")
        return

    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Select", "Select a contact to delete.")
        return

    index = selected[0]
    contact = contacts[index]
    confirm = messagebox.askyesno("Confirm", f"Delete contact '{contact['name']}'?")
    if confirm:
        contacts.pop(index)
        messagebox.showinfo("Deleted", "Contact deleted.")
        view_contacts()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_address.delete("1.0", tk.END)


root = tk.Tk()
root.title("Contact Manager")
root.geometry("700x400")
root.config(bg="#d9f0ff")


left_frame = tk.Frame(root, bg="#d9f0ff")
left_frame.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(left_frame, text="Name:", bg="#d9f0ff", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(left_frame, width=30, font=("Arial", 12))
entry_name.grid(row=0, column=1, pady=2)

tk.Label(left_frame, text="Phone Number:", bg="#d9f0ff", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(left_frame, width=30, font=("Arial", 12))
entry_phone.grid(row=1, column=1, pady=2)

tk.Label(left_frame, text="Email:", bg="#d9f0ff", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(left_frame, width=30, font=("Arial", 12))
entry_email.grid(row=2, column=1, pady=2)

tk.Label(left_frame, text="Address:", bg="#d9f0ff", font=("Arial", 12)).grid(row=3, column=0, sticky="nw")
text_address = tk.Text(left_frame, width=30, height=4, font=("Arial", 12))
text_address.grid(row=3, column=1, pady=2)

btn_add = tk.Button(left_frame, text="Add Contact", width=15, bg="#4CAF50", fg="white", font=("Arial", 11), command=add_contact)
btn_add.grid(row=4, column=0, pady=8)

btn_view = tk.Button(left_frame, text="View Contacts", width=15, bg="#2196F3", fg="white", font=("Arial", 11), command=view_contacts)
btn_view.grid(row=4, column=1, pady=8)

btn_search = tk.Button(left_frame, text="Search Contact", width=15, bg="#FFC107", fg="black", font=("Arial", 11), command=search_contact)
btn_search.grid(row=5, column=0, pady=5)

btn_update = tk.Button(left_frame, text="Update Contact", width=15, bg="#9C27B0", fg="white", font=("Arial", 11), command=update_contact)
btn_update.grid(row=5, column=1, pady=5)

btn_delete = tk.Button(left_frame, text="Delete Contact", width=15, bg="#F44336", fg="white", font=("Arial", 11), command=delete_contact)
btn_delete.grid(row=6, column=0, pady=5)


right_frame = tk.Frame(root, bg="#e7f4f8")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=20)

root.mainloop()
