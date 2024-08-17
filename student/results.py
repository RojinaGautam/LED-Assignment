import customtkinter as ctk

def create_result_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(3, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Create a blue header for the title
    header_frame = ctk.CTkFrame(content_frame, fg_color="#3498db")
    header_frame.grid(row=0, column=0, columnspan=2, sticky="we")
    
    results_label = ctk.CTkLabel(header_frame, text="Results", font=("Arial", 24, "bold"), text_color="white")
    results_label.grid(row=0, column=0, pady=10, padx=20, sticky="w")


    # Create the table header
    table_header_frame = ctk.CTkFrame(content_frame, fg_color="#2c3e50")
    table_header_frame.grid(row=1, column=0, columnspan=2, sticky="we", padx=20, pady=10)

    headers = ["Subjects", "Exam date", "Subject Mark", "Grade", "Total grade"]
    for i, header in enumerate(headers):
        header_label = ctk.CTkLabel(table_header_frame, text=header, font=("Arial", 16, "bold"), text_color="white")
        header_label.grid(row=0, column=i, padx=10, pady=5)

    # Create the table content
    table_content_frame = ctk.CTkFrame(content_frame, fg_color="#ecf0f1")
    table_content_frame.grid(row=2, column=0, columnspan=2, sticky="we", padx=20, pady=10)

    results = [
        ("MATHS", "16th June", "66", "B", ""),
        ("COMPUTER", "18th June", "83", "A", ""),
        ("SCIENCE", "20th June", "75", "B+", "")
    ]

    for i, result in enumerate(results):
        for j, item in enumerate(result):
            result_label = ctk.CTkLabel(table_content_frame, text=item, font=("Arial", 14), text_color="black")
            result_label.grid(row=i, column=j, padx=10, pady=5, sticky="we")

        # Add alternating background colors to the rows
        table_content_frame.grid_rowconfigure(i, weight=1)
        if i % 2 == 0:
            table_content_frame.grid_rowconfigure(i, fg_color="#bdc3c7")

    # Add a grade circle to the right of the table
    grade_frame = ctk.CTkFrame(content_frame, width=80, height=80, fg_color="#bdc3c7", corner_radius=40)
    grade_frame.grid(row=2, column=2, sticky="e", padx=20)

    grade_label = ctk.CTkLabel(grade_frame, text="A", font=("Arial", 36, "bold"), text_color="black")
    grade_label.place(relx=0.5, rely=0.5, anchor="center")
