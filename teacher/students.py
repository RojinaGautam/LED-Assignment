import customtkinter as ctk

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

    # Add the illustration placeholder on the right
    illustration_placeholder = ctk.CTkLabel(top_frame, text="", font=("Arial", 16), width=200, height=150, corner_radius=10, fg_color="#e9ecef")
    illustration_placeholder.grid(row=0, column=1, rowspan=2, sticky="e", padx=20)

    # Bottom left section with Classes and Students
    bottom_left_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    bottom_left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    classes_label = ctk.CTkLabel(bottom_left_frame, text="Classes", font=("Arial", 18, "bold"))
    classes_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    class_buttons = [
        ("All Classes", "Add"),
        ("Mathematics", "Add"),
        ("Science", "Add"),
        ("English", "Add"),
    ]

    for i, (class_name, action) in enumerate(class_buttons):
        class_label = ctk.CTkLabel(bottom_left_frame, text=class_name, font=("Arial", 16))
        class_label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

        action_button = ctk.CTkButton(bottom_left_frame, text=action, width=50, height=30)
        action_button.grid(row=i+1, column=1, sticky="e", padx=10, pady=5)

    students_label = ctk.CTkLabel(bottom_left_frame, text="Students", font=("Arial", 18, "bold"))
    students_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)

    students = ["Nicole kc", "Ryan shah", "Nia Gurung", "Asmi Thapa"]
    for i, student in enumerate(students):
        student_label = ctk.CTkLabel(bottom_left_frame, text=student, font=("Arial", 16))
        student_label.grid(row=i+5, column=0, sticky="w", padx=10, pady=5)

        edit_button = ctk.CTkButton(bottom_left_frame, text="Edit", width=50, height=30)
        edit_button.grid(row=i+5, column=1, sticky="e", padx=10, pady=5)

    # Calendar section
    calendar_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    calendar_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    calendar_label = ctk.CTkLabel(calendar_frame, text="August", font=("Arial", 18, "bold"))
    calendar_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    calendar_placeholder = ctk.CTkLabel(calendar_frame, text="Calendar", font=("Arial", 16), width=200, height=200, corner_radius=10, fg_color="#e9ecef")
    calendar_placeholder.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Progress and stats section
    progress_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    progress_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    # Adjust grid configuration to avoid overlap
    progress_frame.grid_columnconfigure(0, weight=1)
    progress_frame.grid_columnconfigure(1, weight=1)
    progress_frame.grid_columnconfigure(2, weight=1)
    progress_frame.grid_rowconfigure(0, weight=1)
    progress_frame.grid_rowconfigure(1, weight=3)

    task_label = ctk.CTkLabel(progress_frame, text="18 Assigned Task", font=("Arial", 14), fg_color="#e9ecef", corner_radius=5)
    task_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    completed_label = ctk.CTkLabel(progress_frame, text="15 Assignment Completed", font=("Arial", 14), fg_color="#e9ecef", corner_radius=5)
    completed_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    standards_label = ctk.CTkLabel(progress_frame, text="09 Standards Completed", font=("Arial", 14), fg_color="#e9ecef", corner_radius=5)
    standards_label.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    # Progress pie chart placeholder
    chart_frame = ctk.CTkFrame(progress_frame, fg_color="#fff", width=150, height=150, corner_radius=10)
    chart_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

    chart_placeholder = ctk.CTkLabel(chart_frame, text="09\n15\n18", font=("Arial", 24, "bold"), justify="center")
    chart_placeholder.place(relx=0.5, rely=0.5, anchor="center")

    # Top performers section
    performers_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    performers_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

    performers_label = ctk.CTkLabel(performers_frame, text="Top performers", font=("Arial", 16, "bold"))
    performers_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # List of top performers
    top_performers = ["Nia Gurung", "Ryan shah"]
    for i, performer in enumerate(top_performers):
        performer_label = ctk.CTkLabel(performers_frame, text=performer, font=("Arial", 14))
        performer_label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)
