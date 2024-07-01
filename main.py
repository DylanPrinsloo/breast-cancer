import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "Dylan" and password == "PM_24":
        login_window.destroy()
        main_page()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials or access not approved.")

def login_page():
    global login_window, entry_username, entry_password
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("500x500")  # Adjusted to a more reasonable size

    # Load and scale the background image
    image_path = "C:/Data/.PM_01/Predictive-Main_24/images/jump_jump.jpg"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((500, 500), Image.Resampling.LANCZOS)  # Resize the image to fit the window
    background_image = ImageTk.PhotoImage(resized_image)
    
    label_image = tk.Label(login_window, image=background_image)
    label_image.place(x=0, y=0, relwidth=1, relheight=1)

    # Username Entry
    label_username = tk.Label(login_window, text="Username:")
    label_username.pack(pady=(150, 10))
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    # Password Entry
    label_password = tk.Label(login_window, text="Password:")
    label_password.pack(pady=10)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    # Login Button
    btn_login = tk.Button(login_window, text="Confirm", command=login)
    btn_login.pack(pady=20)

    login_window.mainloop()

def main_page():
    global main_window, session_start_time, entry_insert, topic_label
    main_window = tk.Tk()
    main_window.title("Main Page")
    main_window.geometry("800x600")

    session_start_time = time.time()

    # Display username and session start time
    user_info = tk.Label(main_window, text=f"Username: Dylan\nSession Start: {time.ctime(session_start_time)}")
    user_info.pack(anchor='nw')

    # Insert Bar
    entry_insert = tk.Entry(main_window)
    entry_insert.pack(fill='x', padx=50, pady=50)

    # Exit Button
    btn_exit = tk.Button(main_window, text="Exit", command=confirm_exit)
    btn_exit.pack(anchor='ne')

    # Topic Display
    topic_label = tk.Label(main_window, text="", bg="lightgrey")
    topic_label.pack(side="right", fill='y')

    # Clear Conversation Data Button
    btn_clear = tk.Button(main_window, text="Clear Data", command=clear_data)
    btn_clear.pack(side="bottom")

    main_window.mainloop()

def confirm_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        main_window.destroy()

def clear_data():
    topic_label.config(text="")

if __name__ == "__main__":
    login_page()


