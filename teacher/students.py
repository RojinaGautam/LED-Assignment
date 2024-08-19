import customtkinter as ctk
from PIL import Image, ImageTk

def create_students_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#f8f9fa")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_rowconfigure(2, weight=2)
    content_frame.grid_columnconfigure(0, weight=2)
    content_frame.grid_columnconfigure(1, weight=1)

    # Top section with Welcome text and illustration
    top_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 20))
    top_frame.grid_columnconfigure(0, weight=1)
    top_frame.grid_columnconfigure(1, weight=1)

    welcome_label = ctk.CTkLabel(top_frame, text="Welcome,", font=("Arial", 24, "bold"))
    welcome_label.grid(row=0, column=0, sticky="w", padx=10)

    # Illustration on the right
    illustration_image = Image.open("./images/students.png")
    illustration_image = illustration_image.resize((200, 150))
    illustration_photo = ImageTk.PhotoImage(illustration_image)
    illustration_label = ctk.CTkLabel(top_frame, image=illustration_photo, text="")
    illustration_label.image = illustration_photo  # Keep a reference to avoid garbage collection
    illustration_label.grid(row=0, column=1, rowspan=2, sticky="e", padx=20)

    # Bottom section with two rows and two columns
    bottom_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    bottom_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    bottom_frame.grid_columnconfigure(0, weight=1)
    bottom_frame.grid_columnconfigure(1, weight=1)
    bottom_frame.grid_rowconfigure(0, weight=1)
    bottom_frame.grid_rowconfigure(1, weight=1)

    # Classes section
    classes_frame = ctk.CTkFrame(bottom_frame, fg_color="#fff", corner_radius=10)
    classes_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    classes_label = ctk.CTkLabel(classes_frame, text="Classes", font=("Arial", 18, "bold"))
    classes_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    class_buttons = [
        ("All Classes", "+"),
        ("Mathematics", "+"),
        ("Science", "+"),
        ("English", "+"),
    ]

    for i, (class_name, action) in enumerate(class_buttons):
        class_label = ctk.CTkLabel(classes_frame, text=class_name, font=("Arial", 16))
        class_label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

        action_button = ctk.CTkButton(classes_frame, text=action, fg_color="transparent", text_color="#000", width=10, height=10)
        action_button.grid(row=i+1, column=1, sticky="e", padx=10, pady=5)

    # Progress section
    progress_frame = ctk.CTkFrame(bottom_frame, fg_color="#f8f9fa", corner_radius=10)
    progress_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    task_button = ctk.CTkButton(progress_frame, text="18 Assigned Tasks", font=("Arial", 14), fg_color="#C0EAF9", text_color="#000", corner_radius=5, width=100, height=100)
    task_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    completed_button = ctk.CTkButton(progress_frame, text="15 Assignments Completed", font=("Arial", 14), fg_color="#C0EAF9", text_color="#000", corner_radius=5, width=100, height=100)
    completed_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    standards_button = ctk.CTkButton(progress_frame, text="09 Standards Completed", font=("Arial", 14), fg_color="#C0EAF9", text_color="#000", corner_radius=5, width=100, height=100)
    standards_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    # New Students section
    students_frame = ctk.CTkFrame(bottom_frame, fg_color="#fff", corner_radius=10)
    students_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    students_label = ctk.CTkLabel(students_frame, text="Students", font=("Arial", 18, "bold"))
    students_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    student_buttons = [
        ("All Students", "+"),
        ("John Doe", "+"),
        ("Jane Smith", "+"),
        ("Emily Davis", "+"),
    ]

    for i, (student_name, action) in enumerate(student_buttons):
        student_label = ctk.CTkLabel(students_frame, text=student_name, font=("Arial", 16))
        student_label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

        action_button = ctk.CTkButton(students_frame, text=action, fg_color="transparent", text_color="#000", width=10, height=10)
        action_button.grid(row=i+1, column=1, sticky="e", padx=10, pady=5)

    # Chart section
    chart_frame = ctk.CTkFrame(bottom_frame, fg_color="#f8f9fa", corner_radius=10)
    chart_frame.grid(row=1, column=1, sticky="nsew", padx=(100, 40), pady=(0, 100))



    chart_image = Image.open("./images/student-chart.png")
    chart_image = chart_image.resize((300, 200))
    chart_photo = ImageTk.PhotoImage(chart_image)
    chart_label = ctk.CTkLabel(chart_frame, image=chart_photo, text="")
    chart_label.image = chart_photo  # Keep a reference to avoid garbage collection
    chart_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
