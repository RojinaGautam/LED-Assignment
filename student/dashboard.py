import customtkinter as ctk
import sqlite3
from tkinter import Toplevel

def create_dashboard_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(3, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Add the "My Learnings" label and center it
    my_learnings_label = ctk.CTkLabel(content_frame, text="My Learnings", font=("Arial", 20))
    my_learnings_label.grid(row=1, column=0, columnspan=2, sticky="n", pady=10)

    # Add the search bar and center it
    search_bar = ctk.CTkEntry(content_frame, placeholder_text="Search By title", width=200)
    search_bar.grid(row=2, column=0, columnspan=2, pady=10)

    # Create a frame for the learning modules
    modules_frame = ctk.CTkFrame(content_frame, fg_color="#fff")
    modules_frame.grid(row=3, column=0, columnspan=2, sticky="nswe", padx=10, pady=10)

    # Example modules
    modules = get_modules_from_db()

    for module in modules:
        module_frame = ctk.CTkFrame(modules_frame)
        module_frame.pack(pady=10, fill="x")

        title_label = ctk.CTkLabel(module_frame, text=module[1], font=("Arial", 16))
        title_label.grid(row=0, column=0, sticky="w")

        progress_label = ctk.CTkLabel(module_frame, text=f"Lesson completed {module[2]}/{module[3]}")
        progress_label.grid(row=1, column=0, sticky="w")

        go_button = ctk.CTkButton(module_frame, text="GO TO MODULE", command=lambda m_id=module[0]: view_assignments(m_id))
        go_button.grid(row=1, column=1, padx=10)

def get_modules_from_db():
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM modules where isactive is not "N" ')
    modules = cursor.fetchall()
    conn.close()
    return modules

def view_assignments(module_id):
    # Create a new window to display assignments
    assignments_window = Toplevel()
    assignments_window.title("Assignments")

    # Fetch assignments from the database
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    cursor.execute('SELECT assignment_title, due_date FROM assignments WHERE module_id = ?', (module_id,))
    assignments = cursor.fetchall()
    conn.close()

    # Create a frame for assignments
    assignments_frame = ctk.CTkFrame(assignments_window, fg_color="#fff")
    assignments_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Add assignment labels
    for i, assignment in enumerate(assignments):
        title_label = ctk.CTkLabel(assignments_frame, text=f"Assignment: {assignment[0]}", font=("Arial", 14))
        title_label.grid(row=i, column=0, sticky="w", pady=5)

        due_date_label = ctk.CTkLabel(assignments_frame, text=f"Due Date: {assignment[1]}", font=("Arial", 12))
        due_date_label.grid(row=i, column=1, sticky="w", pady=5)
