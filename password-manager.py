import tkinter as tk
from tkinter import messagebox
import random
import string
import os

# --- File Handling Class ---
class PasswordFileHandler:
    def __init__(self, filename="passwords.txt"):
        self.filename = filename

    def write_entry(self, service, username, password, email):
        """Write password entry to the file in the current directory."""
        try:
            with open(self.filename, "a") as f:
                f.write(f"Service: {service}\nUsername: {username}\nPassword: {password}\nEmail: {email}\n\n")
            return True
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to save password: {str(e)}")
            return False

    def read_entries(self):
        """Read all entries from the file in the current directory."""
        try:
            if not os.path.exists(self.filename):
                return ""  # File doesn't exist yet
            with open(self.filename, "r") as f:
                return f.read()
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read passwords: {str(e)}")
            return ""

    def file_exists(self):
        """Check if the password file exists in the current directory."""
        return os.path.exists(self.filename)

# --- Password Generation ---
def generate_password(length=12):
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char in string.punctuation for char in password) and
            len(password) >= 8):
            return password

# --- GUI Functions ---
def generate_and_display_password():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def on_save():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    # Input validation
    if not all([service, username, password, email]):
        messagebox.showwarning("Input Error", "Please enter all fields.")
        return
    
    # Save using file handler
    handler = PasswordFileHandler()
    if handler.write_entry(service, username, password, email):
        messagebox.showinfo("Success", "Password saved successfully!")

def show_password_list():
    handler = PasswordFileHandler()
    passwords = handler.read_entries()
    
    if not passwords.strip():
        messagebox.showinfo("Password List", "No passwords stored.")
        return
    
    password_list_window = tk.Toplevel(root)
    password_list_window.title("Stored Passwords")
    tk.Label(password_list_window, text="Stored Passwords:", font=("Helvetica", 14)).pack(pady=10)
    
    text_area = tk.Text(password_list_window, wrap=tk.WORD, width=50, height=20)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, passwords)
    text_area.config(state=tk.DISABLED)

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Manager")

# Input fields
tk.Label(root, text="Service:").grid(row=0, column=0, padx=10, pady=10)
service_entry = tk.Entry(root, width=30)
service_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

save_button = tk.Button(root, text="Save Password", command=on_save)
save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

password_list_button = tk.Button(root, text="Password List", command=show_password_list)
password_list_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
