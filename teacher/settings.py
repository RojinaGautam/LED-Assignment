import customtkinter as ctk
import sqlite3
from tkinter import simpledialog, messagebox
from database.handler import read_records,update_record,delete_record

def create_settings_content(master, user_id, conn):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")

    # Create a shadowed border effect
    border_frame = ctk.CTkFrame(content_frame, fg_color="#ddd", width=400, height=400)
    border_frame.pack(padx=10, pady=10, expand=True, fill='both')

    inner_frame = ctk.CTkFrame(border_frame, fg_color="#fff")
    inner_frame.pack(padx=10, pady=10, expand=True, fill='both')

    settings_label = ctk.CTkLabel(inner_frame, text="Settings and Profile", font=("Arial", 20))
    settings_label.pack(pady=20)

    # Search Bar
    search_frame = ctk.CTkFrame(inner_frame, fg_color="#f0f0f0")
    search_frame.pack(pady=10, fill='x')
    
    search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search...")
    search_entry.pack(pady=5, padx=10, fill='x')

    # Link-like buttons
    buttons_frame = ctk.CTkFrame(inner_frame, fg_color="#fff")
    buttons_frame.pack(pady=10, fill='x')

    button_names = ["Account Information", "Update Password", "Notification", "Delete Account", "About"]
    for name in button_names:
        button = ctk.CTkButton(
            buttons_frame,
            text=name,
            fg_color="#fff",
            text_color="#000",  # Set text color to black
            hover_color="#e0e0e0",
            width=300,
            height=40,
            command=lambda n=name: button_action(n, user_id, conn)
        )
        button.pack(pady=5)

def button_action(button_name, user_id, conn):
    if button_name == "Account Information":
        show_account_information(user_id, conn)
    elif button_name == "Update Password":
        update_password(user_id, conn)
    elif button_name == "Notification":
        show_notifications(conn)
    elif button_name == "Delete Account":
        delete_account(user_id, conn)
    elif button_name == "About":
        messagebox.showinfo("About", "This is a settings page.")

def show_account_information(user_id, conn):
    user_details = read_records(conn, 'students', columns=['name', 'class', 'gender', 'phone', 'email'],
                                where_clause=f"id = {user_id}")

    if user_details:
        user = user_details[0]
        details = (
            f"Name: {user[0]}\n"
            f"Class: {user[1]}\n"
            f"Gender: {user[2]}\n"
            f"Phone: {user[3]}\n"
            f"Email: {user[4]}"
        )
        messagebox.showinfo("Account Information", details)
    else:
        messagebox.showerror("Error", "No account information found.")

def update_password(user_id, conn):
    new_password = simpledialog.askstring("Update Password", "Enter new password:")
    if new_password:
        try:
            update_record(conn, 'students', {'password': new_password}, f"id = {user_id}")
            messagebox.showinfo("Success", "Password updated successfully.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error updating password: {e}")

def show_notifications(conn):
    announcements = read_records(conn, 'announcements', columns=['description'])
    if announcements:
        notification_text = "\n".join([a[0] for a in announcements])
        messagebox.showinfo("Notifications", notification_text)
    else:
        messagebox.showinfo("Notifications", "No notifications available.")

def delete_account(user_id, conn):
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete your account? This action cannot be undone."):
        try:
            delete_record(conn, 'students', f"id = {user_id}")
            messagebox.showinfo("Success", "Account deleted successfully.")
            # Optionally, you may want to log out the user or close the application after deletion
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error deleting account: {e}")

