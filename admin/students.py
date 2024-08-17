import customtkinter as ctk
from PIL import Image
from database.connection import create_connection
from database.handler import read_records, delete_record, update_record

def create_student_content(master, switch_view):
    global content_frame
    global search_bar
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_rowconfigure(1, weight=0)
    content_frame.grid_rowconfigure(2, weight=0)
    content_frame.grid_rowconfigure(3, weight=1)  # Allow for scrolling area
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=0)
    content_frame.grid_columnconfigure(2, weight=0)
    content_frame.grid_columnconfigure(3, weight=0)

    # Add the "Students" label at the top left
    students_label = ctk.CTkLabel(content_frame, text="Students", font=("Arial", 20))
    students_label.grid(row=0, column=0, sticky="w", pady=10)

    # Add search bar
    search_bar = ctk.CTkEntry(content_frame, placeholder_text="Search for a user by name or email", width=300)
    search_bar.grid(row=1, column=0, padx=150, pady=10, sticky="ew")
    search_bar.bind("<KeyRelease>", lambda event: update_student_list())

    add_student_button = ctk.CTkButton(
        content_frame,
        text="Add User",
        fg_color="#3498db",
        text_color="#fff",
        command=lambda: switch_view("add_student")
    )
    add_student_button.grid(row=1, column=1, sticky="e", padx=10)

    # Create a canvas to allow for scrolling
    canvas = ctk.CTkCanvas(content_frame)
    canvas.grid(row=3, column=0, columnspan=3, sticky="nsew")

    # Add scrollbar
    scrollbar = ctk.CTkScrollbar(content_frame, orientation="vertical", command=canvas.yview)
    scrollbar.grid(row=3, column=2, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the student list
    global student_list_frame
    student_list_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=student_list_frame, anchor="nw")

    # Configure row and column weights
    student_list_frame.grid_rowconfigure(0, weight=0)
    student_list_frame.grid_columnconfigure(0, weight=1)

    update_student_list()  # Initial display of students

    # Update the canvas scrolling region
    student_list_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def update_student_list():
    """
    Update the student list based on the search query.
    """
    global student_list_frame
    global search_bar
    global empty_state_frame

    try:
        # Clear existing records
        for widget in student_list_frame.winfo_children():
            widget.destroy()

        # Hide empty state frame if it exists
        if 'empty_state_frame' in globals() and empty_state_frame:
            empty_state_frame.grid_forget()

        # Get search query
        query = search_bar.get().lower()

        # Retrieve student records from the database
        conn = create_connection("assignment.db")
        if conn is None:
            raise Exception("Database connection failed")

        if query:
            students = read_records(conn, "students", columns='*',
                                    where_clause=f"(name LIKE '%{query}%' OR email LIKE '%{query}%')")
        else:
            students = read_records(conn, "students", columns='*')

        if students:
            # Fetch column names and exclude "id"
            cursor = conn.execute('SELECT * FROM students LIMIT 1')
            column_names = [description[0] for description in cursor.description][1:]  # Exclude "id"

            # Display column headers
            for col_idx, column_name in enumerate(column_names):
                header_label = ctk.CTkLabel(student_list_frame, text=column_name.capitalize(),
                                            font=("Arial", 16, "bold"))
                header_label.grid(row=0, column=col_idx, padx=5, pady=5)

            # Add "Actions" column header
            actions_label = ctk.CTkLabel(student_list_frame, text="Actions", font=("Arial", 16, "bold"))
            actions_label.grid(row=0, column=len(column_names), padx=5, pady=5, sticky="e")

            # Display records in a table format
            for i, student in enumerate(students, start=1):
                for col_idx, value in enumerate(student[1:]):  # Skip the first column (id)
                    value_label = ctk.CTkLabel(student_list_frame, text=value, font=("Arial", 14))
                    value_label.grid(row=i, column=col_idx, padx=5, pady=5, sticky="w")

                # Edit button
                edit_button = ctk.CTkButton(
                    student_list_frame,
                    text="Edit",
                    fg_color="#2ecc71",
                    text_color="#fff",
                    width=80,
                    command=lambda student=student: open_edit_popup(student)
                )
                edit_button.grid(row=i, column=len(column_names), sticky="e", padx=5)

                # Delete button
                delete_button = ctk.CTkButton(
                    student_list_frame,
                    text="Delete",
                    fg_color="#e74c3c",
                    text_color="#fff",
                    width=80,
                    command=lambda student_id=student[0]: delete_student(student_id, student_list_frame, i)
                )
                delete_button.grid(row=i, column=len(column_names) + 1, sticky="e", padx=5)

        else:
            # Create empty state frame if it does not exist
            if 'empty_state_frame' not in globals() or not empty_state_frame:
                empty_state_frame = ctk.CTkFrame(student_list_frame, fg_color="#f8f8f8", corner_radius=0)
                empty_state_frame.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=(20, 0))

                # Configure grid layout for empty_state_frame
                empty_state_frame.grid_rowconfigure(0, weight=1)
                empty_state_frame.grid_columnconfigure(0, weight=1)

                # Load and display the image
                sleeping_cat_image = ctk.CTkImage(Image.open("./images/sleeping_cat.png"), size=(200, 200))
                empty_image_label = ctk.CTkLabel(empty_state_frame, image=sleeping_cat_image, text="")
                empty_image_label.grid(row=0, column=0, pady=10, sticky="n")

                # No students label
                no_students_label = ctk.CTkLabel(empty_state_frame, text="No students at this time", font=("Arial", 18))
                no_students_label.grid(row=1, column=0, pady=10)

                # Subtext label
                subtext_label = ctk.CTkLabel(empty_state_frame,
                                             text="Students will appear here after they enroll in your school.",
                                             font=("Arial", 12))
                subtext_label.grid(row=2, column=0, pady=(0, 20))

        # Update the canvas scrolling region
        student_list_frame.update_idletasks()

        # Find the canvas widget
        canvas = None
        for widget in student_list_frame.winfo_children():
            if isinstance(widget, ctk.CTkCanvas):
                canvas = widget
                break

        if canvas:
            canvas.config(scrollregion=canvas.bbox("all"))

    except Exception as e:
        show_error_popup(f"An error occurred: {str(e)}")
def show_error_popup(message):
    """
    Display an error popup with the given message.
    """
    popup = ctk.CTkToplevel()
    popup.title("Error")
    popup.geometry("300x150")

    label = ctk.CTkLabel(popup, text=message, wraplength=250)
    label.pack(pady=20)

    ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=10)

    popup.grab_set()  # Make the popup modal
    popup.wait_window()  # Wait for the popup to be closed before continuing

def open_edit_popup(student):
    """
    Open a popup window to edit the student's information.
    """
    popup = ctk.CTkToplevel()
    popup.title("Edit Student")

    details_frame = ctk.CTkFrame(popup)
    details_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Name
    name_label = ctk.CTkLabel(details_frame, text="Name", font=("Arial", 14))
    name_label.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))

    name_entry = ctk.CTkEntry(details_frame, placeholder_text="Name")
    name_entry.grid(row=1, column=0, padx=20, pady=5, sticky="we")
    name_entry.insert(0, student[1])  # Assuming name is the second column

    # Class
    class_label = ctk.CTkLabel(details_frame, text="Class", font=("Arial", 14))
    class_label.grid(row=0, column=1, sticky="w", padx=20, pady=(10, 0))

    class_entry = ctk.CTkComboBox(details_frame, values=["Class 1", "Class 2", "Class 3"])
    class_entry.grid(row=1, column=1, padx=20, pady=5, sticky="we")
    class_entry.set(student[2])  # Assuming class is the third column

    # Gender
    gender_label = ctk.CTkLabel(details_frame, text="Gender", font=("Arial", 14))
    gender_label.grid(row=0, column=2, sticky="w", padx=20, pady=(10, 0))

    gender_entry = ctk.CTkComboBox(details_frame, values=["Male", "Female", "Other"])
    gender_entry.grid(row=1, column=2, padx=20, pady=5, sticky="we")
    gender_entry.set(student[3])  # Assuming gender is the fourth column

    # Type
    type_label = ctk.CTkLabel(details_frame, text="Type", font=("Arial", 14))
    type_label.grid(row=0, column=3, sticky="w", padx=20, pady=(10, 0))

    type_entry = ctk.CTkComboBox(details_frame, values=["Teacher", "Student"])
    type_entry.grid(row=1, column=3, padx=20, pady=5, sticky="we")
    type_entry.set(student[4])  # Assuming type is the fifth column

    # Email
    email_label = ctk.CTkLabel(details_frame, text="Email address", font=("Arial", 14))
    email_label.grid(row=2, column=0, sticky="w", padx=20, pady=(10, 0))

    email_entry = ctk.CTkEntry(details_frame, placeholder_text="Email address")
    email_entry.grid(row=3, column=0, padx=20, pady=5, sticky="we")
    email_entry.insert(0, student[5])  # Assuming email is the sixth column

    # Phone
    phone_label = ctk.CTkLabel(details_frame, text="Phone number", font=("Arial", 14))
    phone_label.grid(row=2, column=1, sticky="w", padx=20, pady=(10, 0))

    phone_entry = ctk.CTkEntry(details_frame, placeholder_text="Phone number")
    phone_entry.grid(row=3, column=1, padx=20, pady=5, sticky="we")
    phone_entry.insert(0, student[6])  # Assuming phone is the seventh column

    # Password
    password_label = ctk.CTkLabel(details_frame, text="Password", font=("Arial", 14))
    password_label.grid(row=2, column=2, sticky="w", padx=20, pady=(10, 0))

    password_entry = ctk.CTkEntry(details_frame, placeholder_text="Password", show="*")
    password_entry.grid(row=3, column=2, padx=20, pady=5, sticky="we")
    password_entry.insert(0, student[7])  # Assuming password is the eighth column

    # Save button
    save_button = ctk.CTkButton(
        details_frame,
        text="Save",
        fg_color="#2ecc71",
        text_color="#fff",
        command=lambda: save_changes(student[0], name_entry.get(), class_entry.get(), gender_entry.get(), type_entry.get(), email_entry.get(), phone_entry.get(), password_entry.get(), popup)
    )
    save_button.grid(row=4, column=0, columnspan=4, pady=10)

def save_changes(student_id, name, class_, gender, type_, email, phone, password, popup):
    """
    Save changes to the database and update the UI.
    """
    conn = create_connection("assignment.db")

    # Define the updates as a dictionary
    updates = {
        "name": name,
        "class": class_,
        "gender": gender,
        "type": type_,
        "email": email,
        "phone": phone,
        "password": password
    }

    # Define the WHERE clause to update the specific student
    where_clause = f"id = {student_id}"

    # Call the update_record function with the correct parameters
    update_record(conn, "students", updates, where_clause)

    popup.destroy()
    update_student_list()  # Refresh the student list after saving changes

def delete_student(student_id, parent_frame, row):
    """
    Delete the student record and remove the corresponding row from the GUI.
    """
    # Connect to the database and delete the student
    conn = create_connection("assignment.db")
    delete_record(conn, "students", f"id={student_id}")

    # Remove the row from the GUI
    for widget in parent_frame.grid_slaves(row=row):
        widget.grid_forget()
    update_student_list()  # Refresh the student list after deletion
