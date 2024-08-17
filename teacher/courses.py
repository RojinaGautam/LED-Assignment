import customtkinter as ctk

def create_courses_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#f8f9fa")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_rowconfigure(1, weight=2)
    content_frame.grid_rowconfigure(2, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=2)

    # Search bar section
    search_bar = ctk.CTkEntry(content_frame, placeholder_text="Search Anything", width=400)
    search_bar.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="we")

    # Subjects section
    subjects_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    subjects_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    subjects = ["Mathematics", "English", "Science", "Comp. Science"]

    for i, subject in enumerate(subjects):
        subject_button = ctk.CTkButton(subjects_frame, text=subject, width=150, height=50)
        subject_button.grid(row=0, column=i, padx=5, pady=5)
        
    # Progress Chart section
    progress_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    progress_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    progress_label = ctk.CTkLabel(progress_frame, text="Course Progress", font=("Arial", 18, "bold"))
    progress_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

    last_month_label = ctk.CTkLabel(progress_frame, text="Last month", font=("Arial", 14))
    last_month_label.grid(row=0, column=1, sticky="e", padx=10, pady=(10, 0))

    # Placeholder for chart
    chart_placeholder = ctk.CTkLabel(progress_frame, text="Chart Here", width=400, height=200, fg_color="#e9ecef", corner_radius=10)
    chart_placeholder.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
    
    # Timetable section
    timetable_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    timetable_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    timetable_label = ctk.CTkLabel(timetable_frame, text="Timetable", font=("Arial", 18, "bold"))
    timetable_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # Placeholder for timetable
    timetable_placeholder = ctk.CTkLabel(timetable_frame, text="8 to 3", width=150, height=50, fg_color="#e9ecef", corner_radius=10)
    timetable_placeholder.grid(row=1, column=0, pady=10, padx=10)

    # Activities section
    activities_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    activities_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

    activities_label = ctk.CTkLabel(activities_frame, text="Activities", font=("Arial", 18, "bold"))
    activities_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # Placeholder for activities
    activities_placeholder = ctk.CTkLabel(activities_frame, text="Quizzes, Test, Surveys", width=200, height=100, fg_color="#e9ecef", corner_radius=10)
    activities_placeholder.grid(row=1, column=0, pady=10, padx=10)
    
    # Badges section
    badges_frame = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10)
    badges_frame.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    badges_label = ctk.CTkLabel(badges_frame, text="Badges", font=("Arial", 18, "bold"))
    badges_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # Placeholder for badges
    badges_placeholder = ctk.CTkLabel(badges_frame, text="Award Your Students", width=200, height=50, fg_color="#e9ecef", corner_radius=10)
    badges_placeholder.grid(row=1, column=0, pady=10, padx=10)
