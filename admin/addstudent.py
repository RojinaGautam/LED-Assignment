import customtkinter as ctk
from tkinter import messagebox
from database.connection import create_connection
from database.handler import create_record

def addstudent_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(3, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Add the "Students" label at the top left
    students_label = ctk.CTkLabel(content_frame, text="Students", font=("Arial", 20))
    students_label.grid(row=0, column=0, sticky="w", pady=10)

    # Export CSV and Add Student buttons at the top right
    export_csv_button = ctk.CTkButton(content_frame, text="Export CSV", fg_color="#fff", text_color="#3498db")
    export_csv_button.grid(row=0, column=1, sticky="e", padx=(0, 5))

    add_student_button = ctk.CTkButton(content_frame, text="Add Student", fg_color="#3498db", text_color="#fff", command=add_student_to_db)
    add_student_button.grid(row=0, column=2, sticky="e", padx=10)

    # Section for "Add Students" with Manually and Import CSV options
    add_students_label = ctk.CTkLabel(content_frame, text="Add Students", font=("Arial", 24))
    add_students_label.grid(row=1, column=0, sticky="w", pady=20, padx=20)

    manual_button = ctk.CTkButton(content_frame, text="Manually", fg_color="#fff", text_color="#000")
    manual_button.grid(row=2, column=0, sticky="w", padx=20)

    import_csv_button = ctk.CTkButton(content_frame, text="Import CSV", fg_color="#fff", text_color="#000")
    import_csv_button.grid(row=2, column=1, sticky="w", padx=10)

    # Section for adding student details
    details_frame = ctk.CTkFrame(content_frame, fg_color="#fff")
    details_frame.grid(row=3, column=0, columnspan=3, pady=20, sticky="nswe")

    # Configure grid layout for details_frame
    details_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    name_label = ctk.CTkLabel(details_frame, text="Name", font=("Arial", 14))
    name_label.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))

    global name_entry
    name_entry = ctk.CTkEntry(details_frame, placeholder_text="Name")
    name_entry.grid(row=1, column=0, padx=20, pady=5, sticky="we")

    class_label = ctk.CTkLabel(details_frame, text="Class", font=("Arial", 14))
    class_label.grid(row=0, column=1, sticky="w", padx=20, pady=(10, 0))

    global class_entry
    class_entry = ctk.CTkComboBox(details_frame, values=["Class 1", "Class 2", "Class 3"])
    class_entry.grid(row=1, column=1, padx=20, pady=5, sticky="we")

    gender_label = ctk.CTkLabel(details_frame, text="Gender", font=("Arial", 14))
    gender_label.grid(row=0, column=2, sticky="w", padx=20, pady=(10, 0))

    global gender_entry
    gender_entry = ctk.CTkComboBox(details_frame, values=["Male", "Female", "Other"])
    gender_entry.grid(row=1, column=2, padx=20, pady=5, sticky="we")

    type_label = ctk.CTkLabel(details_frame, text="Type", font=("Arial", 14))
    type_label.grid(row=0, column=3, sticky="w", padx=20, pady=(10, 0))

    global type_entry
    type_entry = ctk.CTkComboBox(details_frame, values=["Teacher", "Student"])
    type_entry.grid(row=1, column=3, padx=20, pady=5, sticky="we")

    email_label = ctk.CTkLabel(details_frame, text="Email address", font=("Arial", 14))
    email_label.grid(row=2, column=0, sticky="w", padx=20, pady=(10, 0))

    global email_entry
    email_entry = ctk.CTkEntry(details_frame, placeholder_text="Email address")
    email_entry.grid(row=3, column=0, padx=20, pady=5, sticky="we")

    phone_label = ctk.CTkLabel(details_frame, text="Phone number", font=("Arial", 14))
    phone_label.grid(row=2, column=1, sticky="w", padx=20, pady=(10, 0))

    global phone_entry
    phone_entry = ctk.CTkEntry(details_frame, placeholder_text="Phone number")
    phone_entry.grid(row=3, column=1, padx=20, pady=5, sticky="we")

    password_label = ctk.CTkLabel(details_frame, text="Password", font=("Arial", 14))
    password_label.grid(row=2, column=2, sticky="w", padx=20, pady=(10, 0))

    global password_entry
    password_entry = ctk.CTkEntry(details_frame, placeholder_text="Password", show="*")
    password_entry.grid(row=3, column=2, padx=20, pady=5, sticky="we")



def add_student_to_db():
    # Gather data from the entries
    name = name_entry.get()
    student_class = class_entry.get()
    gender = gender_entry.get()
    student_type = type_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()

    # Validate input data
    if not name  or not gender or not student_type or not email or not phone or not password:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    # Define the columns and values to insert
    columns = ("name", "class", "gender", "type", "email", "phone", "password")
    values = (name, student_class, gender, student_type, email, phone, password)

    try:
        # Create a connection to the database
        conn = create_connection('assignment.db')

        # Insert the student data using the create_record function
        create_record(conn, "students", columns, values)

        # Show a success message
        messagebox.showinfo("Success", "User added successfully!")

    except sqlite3.IntegrityError as e:
        # Handle unique constraint violation (e.g., duplicate email or phone)
        if "UNIQUE constraint failed" in str(e):
            messagebox.showerror("Error", "Email or Phone number already exists.")
        else:
            messagebox.showerror("Error", str(e))

    except Exception as e:
        # Handle any other errors
        messagebox.showerror("Error", str(e))

    finally:
        # Close the database connection
        if conn:
            conn.close()

    # Clear the form fields
    name_entry.delete(0, 'end')
    class_entry.set('')
    gender_entry.set('')
    type_entry.set('')
    email_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    password_entry.delete(0, 'end')