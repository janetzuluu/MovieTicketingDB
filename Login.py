import tkinter
from tkinter import messagebox
import os


root = tkinter.Tk()
root.title("Login form")
root.geometry('1000x1200')
root.configure(bg='#333333')

def login():
    username = "admin1"
    password = "12345"
    username2="user1"
    password1="12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        root.destroy()
        os.system(f" python management.py")

    if username_entry.get()==username2 and password_entry.get()==password1:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        root.destroy()
        os.system(f" python user_info_table.py")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Admin Login", bg='#333333', fg="#b2d3f0", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#b2d3f0", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screens on a grid
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

root.mainloop()