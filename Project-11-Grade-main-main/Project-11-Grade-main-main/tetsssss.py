import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

# Database setup
conn = sqlite3.connect('profiles.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
conn.commit()

# Functions
def create_profile():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    try:
        cursor.execute('INSERT INTO profiles (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Profile created successfully!")
        load_profiles()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")

def login_and_use_profile():
    selected_profile = listbox_profiles.get(tk.ACTIVE)

    if not selected_profile:
        messagebox.showerror("Error", "Please select a profile.")
        return

    password_prompt = tk.Toplevel(root)
    password_prompt.title("Enter Password")

    lbl_prompt = tk.Label(password_prompt, text=f"Enter password for {selected_profile}:")
    lbl_prompt.pack(padx=10, pady=10)

    entry_password_login = tk.Entry(password_prompt, show="*")
    entry_password_login.pack(padx=10, pady=10)

    def check_password():
        password = entry_password_login.get()
        cursor.execute('SELECT * FROM profiles WHERE username = ? AND password = ?', (selected_profile, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Logged in successfully!")
            password_prompt.destroy()
            use_profile(selected_profile)
        else:
            messagebox.showerror("Error", "Invalid password.")
            password_prompt.destroy()

    btn_submit = tk.Button(password_prompt, text="Submit", command=check_password)
    btn_submit.pack(padx=10, pady=10)

def use_profile(username):
    # Run another Python file upon successful login
    subprocess.run(["python", "part 2.py"])  # Replace 'another_script.py' with your actual script

def load_profiles():
    cursor.execute('SELECT username FROM profiles')
    profiles = cursor.fetchall()

    listbox_profiles.delete(0, tk.END)
    for profile in profiles:
        listbox_profiles.insert(tk.END, profile[0])

# GUI setup
root = tk.Tk()
root.title("Profile Management")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

lbl_username = tk.Label(frame, text="Username:")
lbl_username.grid(row=0, column=0, pady=5)

entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, pady=5)

lbl_password = tk.Label(frame, text="Password:")
lbl_password.grid(row=1, column=0, pady=5)

entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, pady=5)

btn_create = tk.Button(frame, text="Create Profile", command=create_profile)
btn_create.grid(row=2, column=0, pady=5)

lbl_select_profile = tk.Label(frame, text="Select a Profile:")
lbl_select_profile.grid(row=3, column=0, pady=5)

listbox_profiles = tk.Listbox(frame)
listbox_profiles.grid(row=3, column=1, pady=5)

btn_use_profile = tk.Button(frame, text="Use Profile", command=login_and_use_profile)
btn_use_profile.grid(row=4, column=1, pady=5)

load_profiles()

root.mainloop()
