import customtkinter as ctk
from tkinter import messagebox
from database.connection import create_connection
from database.handler import create_record


def create_announcement_content(master):
    global content_frame, announcement_textbox

    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Log out button at the top right
    logout_button = ctk.CTkButton(content_frame, text="Log out", fg_color="#3498db", text_color="#fff")
    logout_button.grid(row=0, column=1, sticky="ne", padx=20, pady=10)

    # Announce something frame
    announce_frame = ctk.CTkFrame(content_frame, fg_color="#e3f2fd", border_color="#3498db", border_width=2)
    announce_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nswe")

    # Configure grid for announce_frame
    announce_frame.grid_rowconfigure(1, weight=1)
    announce_frame.grid_columnconfigure(0, weight=1)

    # Announce something title
    announce_title_label = ctk.CTkLabel(announce_frame, text="Announce something", font=("Arial", 16), fg_color="#3498db", text_color="#fff", height=40)
    announce_title_label.grid(row=0, column=0, sticky="we")

    # Announcement text box (covering entire frame)
    announcement_textbox = ctk.CTkTextbox(announce_frame, font=("Arial", 14), wrap="word")
    announcement_textbox.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

    # Set default text in the text box
    announcement_textbox.insert("1.0", "There will be no classes tomorrow due to public holiday.\n\nNew assignment added to the module 2.")

    # Submit button
    submit_button = ctk.CTkButton(content_frame, text="Submit", fg_color="#3498db", text_color="#fff", command=submit_announcement)
    submit_button.grid(row=2, column=0, padx=10, pady=20, sticky="w")

def submit_announcement():
    announcement_text = announcement_textbox.get("1.0", "end-1c").strip()  # Get text from the textbox

    # Validate input
    if not announcement_text:
        messagebox.showerror("Input Error", "Announcement description cannot be empty!")
        return

    try:
        # Create a connection to the SQLite database
        conn = create_connection('assignment.db')  # Adjust database name if needed

        # Define the columns and values to insert
        columns = ("description",)
        values = (announcement_text,)

        # Insert the announcement into the database using create_record
        create_record(conn, "announcements", columns, values)

        # Show a success message
        messagebox.showinfo("Success", "Announcement added successfully!")

    except sqlite3.Error as e:
        # Handle any database errors
        messagebox.showerror("Database Error", str(e))

    finally:
        if conn:
            conn.close()

    # Clear the text box
    announcement_textbox.delete("1.0", "end")
