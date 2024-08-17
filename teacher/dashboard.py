import customtkinter as ctk
import sqlite3
from tkinter import simpledialog, messagebox
from database.connection import create_connection
from database.handler import read_records, update_record, create_record, delete_record


def create_dashboard_content(master):
    global content_frame
    global bottom_right_frame

    content_frame = ctk.CTkFrame(master, fg_color="#f8f9fa")
    content_frame.grid(row=2, column=2, sticky="nswe", padx=50, pady=50)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(0, weight=0)
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_rowconfigure(2, weight=1)
    content_frame.grid_columnconfigure(0, weight=2)
    content_frame.grid_columnconfigure(1, weight=1)

    # Top section with Welcome text and illustration
    top_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 20))
    top_frame.grid_columnconfigure(0, weight=1)
    top_frame.grid_columnconfigure(1, weight=1)

    welcome_label = ctk.CTkLabel(top_frame, text="Welcome back", font=("Arial", 24, "bold"))
    welcome_label.grid(row=0, column=0, sticky="w", padx=10)

    progress_label = ctk.CTkLabel(top_frame, text="Your students completed 80% of the tasks\nProgress is very good!!",
                                  font=("Arial", 16))
    progress_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    # Add the illustration placeholder on the right
    illustration_placeholder = ctk.CTkLabel(top_frame, text="Illustration Here", font=("Arial", 16), width=200,
                                            height=150, corner_radius=10, fg_color="#e9ecef")
    illustration_placeholder.grid(row=0, column=1, rowspan=2, sticky="e", padx=20)

    # Add Subject Button at the top of the content_frame
    add_subject_button = ctk.CTkButton(content_frame, text="Add Subject", width=120, height=30, font=("Arial", 14),
                                       command=lambda: add_subject())
    add_subject_button.grid(row=1, column=0, sticky="w", padx=10, pady=(10, 10))

    # Bottom left section with circular progress
    bottom_left_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    bottom_left_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    working_hours_label = ctk.CTkLabel(bottom_left_frame, text="Working Hours", font=("Arial", 18))
    working_hours_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    today_label = ctk.CTkLabel(bottom_left_frame, text="Today", font=("Arial", 16, "bold"), fg_color="#e9ecef",
                               corner_radius=5, width=50)
    today_label.grid(row=0, column=1, sticky="e", padx=10, pady=10)

    progress_frame = ctk.CTkFrame(bottom_left_frame, fg_color="#fff", width=200, height=200, corner_radius=10)
    progress_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    progress_label = ctk.CTkLabel(progress_frame, text="84%", font=("Arial", 30, "bold"))
    progress_label.place(relx=0.5, rely=0.5, anchor="center")

    # Bottom right section with lessons table
    bottom_right_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    bottom_right_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    lessons_label = ctk.CTkLabel(bottom_right_frame, text="Lessons", font=("Arial", 18, "bold"))
    lessons_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Load and display lessons
    refresh_lessons()

    # Calendar placeholder
    calendar_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    calendar_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

    calendar_label = ctk.CTkLabel(calendar_frame, text="Calendar Here", font=("Arial", 16), width=200, height=200,
                                  corner_radius=10, fg_color="#e9ecef")
    calendar_label.place(relx=0.5, rely=0.5, anchor="center")


def add_subject():
    subject = simpledialog.askstring("Input", "Enter the new subject:")
    if subject:
        conn = create_connection("assignment.db")
        create_record(conn, "modules", columns=("title", "isactive", "lessons_completed", "total_lessons"),
                      values=(subject, 'Y', 0, 0))
        conn.close()
        messagebox.showinfo("Success", "Subject added successfully.")
        refresh_lessons()


def add_assignment(module_id):
    assignment_title = simpledialog.askstring("Input", "Enter the assignment title:")
    description = simpledialog.askstring("Input", "Enter the assignment description:")
    due_date = simpledialog.askstring("Input", "Enter the due date (YYYY-MM-DD):")

    if assignment_title and description and due_date:
        conn = create_connection("assignment.db")
        create_record(conn, "assignments", columns=("module_id", "assignment_title", "description", "due_date"),
                      values=(module_id, assignment_title, description, due_date))

        # print(module_id)
        conn.close()
        messagebox.showinfo("Success", "Assignment added successfully.")
    else:
        messagebox.showwarning("Warning", "Please fill out all fields.")


def delete_lesson(lesson_title):
    conn = create_connection("assignment.db")
    try:
        update_record(conn, "modules", {"isactive": 'N'}, f"title='{lesson_title}'")
        messagebox.showinfo("Success", f"Subject '{lesson_title}' marked as inactive.")
        refresh_lessons()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error updating subject: {e}")
    conn.close()


def refresh_lessons():
    global bottom_right_frame

    for widget in bottom_right_frame.winfo_children():
        widget.destroy()

    conn = create_connection("assignment.db")
    lessons_data = read_records(conn, "modules", columns=["id", "title"], where_clause="isactive is not 'N'")

    for i, (lesson_id, lesson) in enumerate(lessons_data):
        lesson_label = ctk.CTkLabel(bottom_right_frame, text=lesson, font=("Arial", 16))
        lesson_label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

        action_button = ctk.CTkButton(bottom_right_frame, text="Add Assignment", width=150, height=30,
                                      command=lambda l_id=lesson_id: add_assignment(l_id))
        action_button.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)

        delete_button = ctk.CTkButton(bottom_right_frame, text="Delete", width=80, height=25,
                                      command=lambda l=lesson: delete_lesson(l))
        delete_button.grid(row=i + 1, column=2, sticky="e", padx=10, pady=5)

    conn.close()
