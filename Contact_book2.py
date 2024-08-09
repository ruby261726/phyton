import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the main window
main_window = tk.Tk()
main_window.title("Contact Book")
main_window.configure(bg="#e0f7fa")  # Light cyan background

# Initialize the contacts dictionary
contact_list = {}

# Function to add a new contact
def add_new_contact():
    contact_name = simpledialog.askstring("Input", "Enter contact name:")
    if contact_name:
        contact_phone = simpledialog.askstring("Input", "Enter phone number:")
        contact_email = simpledialog.askstring("Input", "Enter email:")
        contact_address = simpledialog.askstring("Input", "Enter address:")
        contact_list[contact_name] = {"phone": contact_phone, "email": contact_email, "address": contact_address}
        refresh_contact_display()

# Function to update the contact list display
def refresh_contact_display():
    contact_listbox.delete(0, tk.END)
    for contact_name, contact_info in contact_list.items():
        contact_listbox.insert(tk.END, f"{contact_name}: {contact_info['phone']}")

# Function to view contact details
def view_contact_details():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_name = selected_contact.split(":")[0]
        contact_info = contact_list.get(contact_name)
        if contact_info:
            messagebox.showinfo("Contact Details", f"Name: {contact_name}\nPhone: {contact_info['phone']}\nEmail: {contact_info['email']}\nAddress: {contact_info['address']}")

# Function to update a contact
def modify_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_name = selected_contact.split(":")[0]
        if contact_name in contact_list:
            new_phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact_list[contact_name]["phone"])
            new_email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact_list[contact_name]["email"])
            new_address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact_list[contact_name]["address"])
            contact_list[contact_name] = {"phone": new_phone, "email": new_email, "address": new_address}
            refresh_contact_display()

# Function to delete a contact
def remove_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_name = selected_contact.split(":")[0]
        if contact_name in contact_list:
            del contact_list[contact_name]
            refresh_contact_display()

# Function to search for a contact
def find_contact():
    search_query = simpledialog.askstring("Search", "Enter name or phone number:")
    if search_query:
        found_contact = False
        for contact_name, contact_info in contact_list.items():
            if search_query.lower() in contact_name.lower() or search_query in contact_info['phone']:
                messagebox.showinfo("Search Result", f"Name: {contact_name}\nPhone: {contact_info['phone']}\nEmail: {contact_info['email']}\nAddress: {contact_info['address']}")
                found_contact = True
                break
        if not found_contact:
            messagebox.showinfo("Search Result", "No contact found")

# Create GUI elements
contact_frame = tk.Frame(main_window, bg="#e0f7fa")
contact_frame.pack(pady=10)

add_contact_button = tk.Button(contact_frame, text="Add Contact", command=add_new_contact, bg="#4CAF50", fg="white")
add_contact_button.pack(side=tk.LEFT, padx=5)

view_contact_button = tk.Button(contact_frame, text="View Contact", command=view_contact_details, bg="#2196F3", fg="white")
view_contact_button.pack(side=tk.LEFT, padx=5)

update_contact_button = tk.Button(contact_frame, text="Update Contact", command=modify_contact, bg="#FFC107", fg="white")
update_contact_button.pack(side=tk.LEFT, padx=5)

delete_contact_button = tk.Button(contact_frame, text="Delete Contact", command=remove_contact, bg="#F44336", fg="white")
delete_contact_button.pack(side=tk.LEFT, padx=5)

search_contact_button = tk.Button(contact_frame, text="Search Contact", command=find_contact, bg="#673AB7", fg="white")
search_contact_button.pack(side=tk.LEFT, padx=5)

contact_listbox = tk.Listbox(main_window, width=50, bg="#FFFFFF", fg="#000000")
contact_listbox.pack(pady=10)

refresh_contact_display()

# Run the application
main_window.mainloop()
