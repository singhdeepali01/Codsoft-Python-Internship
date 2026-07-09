import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Contact Book")
        self.root.geometry("750x500")
        self.root.config(bg="#0b1f3a")

        # Dictionary to store contacts
        self.contacts = {
            "Alice Smith": ("9876543210", "alice@example.com"),
            "Bob Jones": ("1234567890", "bob@example.com")
        }

        self.create_widgets()
        self.update_contact_list()

    def create_widgets(self):

        # ================= TITLE =================
        title = tk.Label(
            self.root,
            text="📒 My Contact Book",
            font=("Arial", 18, "bold"),
            bg="#08203d",
            fg="white",
            pady=10
        )
        title.pack(fill="x")

        # ================= MAIN FRAME =================
        main_frame = tk.Frame(self.root, bg="#0b1f3a")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # ================= LEFT FRAME =================
        left_frame = tk.Frame(main_frame, bg="#0b1f3a")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

        tk.Label(
            left_frame,
            text="👥 Contact List",
            font=("Arial",12,"bold"),
            bg="#0b1f3a",
            fg="white"
        ).pack(anchor="w")

        # Search
        search_frame = tk.Frame(left_frame,bg="#0b1f3a")
        search_frame.pack(fill="x", pady=5)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial",11)
        )
        self.search_entry.pack(side="left", fill="x", expand=True)

        tk.Button(
            search_frame,
            text="🔍",
            bg="#3498db",
            fg="white",
            command=self.search_contact,
            width=4
        ).pack(side="left", padx=5)

        # Listbox
        list_frame = tk.Frame(left_frame)
        list_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.contact_listbox = tk.Listbox(
            list_frame,
            font=("Arial",11),
            bg="#13294b",
            fg="white",
            selectbackground="#1abc9c",
            selectforeground="white",
            yscrollcommand=scrollbar.set
        )
        self.contact_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.contact_listbox.yview)

        self.contact_listbox.bind(
            "<<ListboxSelect>>",
            self.on_contact_select
        )

        # ================= RIGHT FRAME =================
        right_frame = tk.Frame(main_frame, bg="#0b1f3a")
        right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(
            right_frame,
            text="📇 Contact Details",
            font=("Arial",12,"bold"),
            bg="#0b1f3a",
            fg="white"
        ).pack(anchor="w")

        form = tk.Frame(right_frame, bg="#0b1f3a")
        form.pack(fill="x", pady=10)

        # Name
        tk.Label(
            form,
            text="👤 Name",
            bg="#0b1f3a",
            fg="white",
            font=("Arial",10)
        ).grid(row=0,column=0,sticky="w",pady=8)

        self.name_entry = tk.Entry(
            form,
            font=("Arial",11),
            width=25
        )
        self.name_entry.grid(row=0,column=1,padx=5)

        # Phone
        tk.Label(
            form,
            text="📞 Phone",
            bg="#0b1f3a",
            fg="white",
            font=("Arial",10)
        ).grid(row=1,column=0,sticky="w",pady=8)

        self.phone_entry = tk.Entry(
            form,
            font=("Arial",11)
        )
        self.phone_entry.grid(row=1,column=1,padx=5)

        # Email
        tk.Label(
            form,
            text="✉ Email",
            bg="#0b1f3a",
            fg="white",
            font=("Arial",10)
        ).grid(row=2,column=0,sticky="w",pady=8)

        self.email_entry = tk.Entry(
            form,
            font=("Arial",11)
        )
        self.email_entry.grid(row=2,column=1,padx=5)

        # Buttons
        btn = tk.Frame(right_frame, bg="#0b1f3a")
        btn.pack(pady=20)

        tk.Button(
            btn,
            text="➕ Add",
            bg="#2ecc71",
            fg="white",
            width=15,
            command=self.add_contact
        ).grid(row=0,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="✏ Update",
            bg="#3498db",
            fg="white",
            width=15,
            command=self.update_contact
        ).grid(row=0,column=1,padx=5,pady=5)

        tk.Button(
            btn,
            text="🗑 Delete",
            bg="#e74c3c",
            fg="white",
            width=15,
            command=self.delete_contact
        ).grid(row=1,column=0,padx=5,pady=5)

        tk.Button(
            btn,
            text="🧹 Clear",
            bg="#95a5a6",
            fg="white",
            width=15,
            command=self.clear_fields
        ).grid(row=1,column=1,padx=5,pady=5)

      # ================= FUNCTIONS =================

    def update_contact_list(self):
        """Refresh the contact list."""
        self.contact_listbox.delete(0, tk.END)

        for name in sorted(self.contacts.keys()):
            self.contact_listbox.insert(tk.END, name)

    def search_contact(self):
        """Search contacts by name."""
        text = self.search_entry.get().strip().lower()

        self.contact_listbox.delete(0, tk.END)

        for name in sorted(self.contacts.keys()):
            if text in name.lower():
                self.contact_listbox.insert(tk.END, name)

    def on_contact_select(self, event):
        """Display selected contact details."""
        selection = self.contact_listbox.curselection()

        if selection:
            name = self.contact_listbox.get(selection[0])
            phone, email = self.contacts[name]

            self.clear_fields()

            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, phone)
            self.email_entry.insert(0, email)

    def add_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if name == "" or phone == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter Name and Phone Number."
            )
            return

        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits."
            )
            return

        if email != "" and ("@" not in email or "." not in email):
            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )
            return

        if name in self.contacts:
            messagebox.showerror(
                "Duplicate Contact",
                "This contact already exists."
            )
            return

        self.contacts[name] = (phone, email)

        self.update_contact_list()
        self.clear_fields()

        messagebox.showinfo(
            "Success",
            "Contact added successfully."
        )

    def update_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if name not in self.contacts:
            messagebox.showerror(
                "Error",
                "Select a contact from the list first."
            )
            return

        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits."
            )
            return

        if email != "" and ("@" not in email or "." not in email):
            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email."
            )
            return

        self.contacts[name] = (phone, email)

        self.update_contact_list()

        messagebox.showinfo(
            "Updated",
            "Contact updated successfully."
        )

    def delete_contact(self):

        selection = self.contact_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a contact."
            )
            return

        name = self.contact_listbox.get(selection[0])

        confirm = messagebox.askyesno(
            "Delete Contact",
            f"Delete {name}?"
        )

        if confirm:
            del self.contacts[name]

            self.update_contact_list()

            self.clear_fields()

            messagebox.showinfo(
                "Deleted",
                "Contact deleted successfully."
            )

    def clear_fields(self):

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


# ================= MAIN =================

if __name__ == "__main__":

    root = tk.Tk()

    app = ContactBook(root)

    root.mainloop()      
