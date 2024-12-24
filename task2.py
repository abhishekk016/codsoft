import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Setting up the layout
        self.setup_ui()

    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Contact Book", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Name label and entry
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=1, column=0, sticky="w", padx=10)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=1, column=1)

        # Phone label and entry
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=2, column=0, sticky="w", padx=10)
        self.phone_entry = tk.Entry(self.root, width=30)
        self.phone_entry.grid(row=2, column=1)

        # Email label and entry
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=3, column=0, sticky="w", padx=10)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.grid(row=3, column=1)

        # Address label and entry
        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(row=4, column=0, sticky="w", padx=10)
        self.address_entry = tk.Entry(self.root, width=30)
        self.address_entry.grid(row=4, column=1)

        # Buttons to add, update, search, remove and view contacts
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, pady=10)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=1, pady=10)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.remove_button.grid(row=6, column=1, pady=10)

        self.view_button = tk.Button(self.root, text="View All Contacts", command=self.view_contacts)
        self.view_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact for {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact for {name} updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found for {name}")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
        else:
            messagebox.showerror("Error", f"No contact found for {name}")

    def remove_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact for {name} removed successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found for {name}")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts available.")
        else:
            contacts_info = ""
            for name, info in self.contacts.items():
                contacts_info += f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n"
            messagebox.showinfo("All Contacts", contacts_info)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


# Main Code to Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
