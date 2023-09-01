import tkinter as tk
from tkinter import messagebox
def login():
    if username_entry.get() == "admin" and password_entry.get() == "password":
        messagebox.showinfo("Login", "Login sukses")
    else:
        messagebox.showerror("Login", "Username atau password salah")
window = tk.Tk()
window.title("Form Login")
window.geometry("300x200")
username_label = tk.Label(text="Username:")
username_entry = tk.Entry()
password_label = tk.Label(text="Password:")
password_entry = tk.Entry(show="*")
login_button = tk.Button(text="Login", command=login)
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)
window.mainloop()
