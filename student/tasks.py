import customtkinter as ctk

def create_task_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")

    # Title
    title_label = ctk.CTkLabel(
        content_frame, 
        text="My Task", 
        font=("Arial", 30, "bold"), 
        text_color="#000"
    )
    title_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # Task sections frame with blue background
    task_sections_frame = ctk.CTkFrame(content_frame, fg_color="#1E90FF", height=150)
    task_sections_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")

    task_sections_frame.grid_columnconfigure(0, weight=1)
    task_sections_frame.grid_columnconfigure(1, weight=1)

    # Completed Tasks
    completed_frame = ctk.CTkFrame(task_sections_frame, fg_color="#fff")
    completed_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    completed_label = ctk.CTkLabel(completed_frame, text="COMPLETED", font=("Arial", 16, "bold"))
    completed_label.grid(row=0, column=0, padx=10, pady=5)

    completed_tasks = [
        ("COMPUTER Task", "Rewrite the following codes."),
        ("SCIENCE Task", "Name the chemicals used in lab.")
    ]

    for task, description in completed_tasks:
        task_frame = ctk.CTkFrame(completed_frame, fg_color="#f9f9f9")
        task_frame.grid(sticky="ew", padx=5, pady=2)
        task_label = ctk.CTkLabel(task_frame, text=f"{task}", width=20, anchor="w")
        task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        description_label = ctk.CTkLabel(task_frame, text=f"{description}", anchor="w")
        description_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Incomplete Tasks
    incomplete_frame = ctk.CTkFrame(task_sections_frame, fg_color="#87CEEB")
    incomplete_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    incomplete_label = ctk.CTkLabel(incomplete_frame, text="INCOMPLETED", font=("Arial", 16, "bold"))
    incomplete_label.grid(row=0, column=0, padx=10, pady=5)

    incomplete_tasks = [
        ("Chemistry", "Rewrite the following codes."),
        ("Maths Task", "Solve algebra")
    ]

    for task, description in incomplete_tasks:
        task_frame = ctk.CTkFrame(incomplete_frame, fg_color="#f9f9f9")
        task_frame.grid(sticky="ew", padx=5, pady=2)
        task_label = ctk.CTkLabel(task_frame, text=f"{task}", width=20, anchor="w")
        task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        description_label = ctk.CTkLabel(task_frame, text=f"{description}", anchor="w")
        description_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

