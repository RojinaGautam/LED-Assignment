import customtkinter as ctk
from PIL import Image, ImageTk

def create_courses_content(master):
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_rowconfigure(1, weight=2)
    content_frame.grid_rowconfigure(2, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=2)

    # Left container frame (for search bar and subjects)
    left_frame = ctk.CTkFrame(content_frame,height=50,width=200)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Search bar section inside left frame
    search_bar = ctk.CTkEntry(left_frame, placeholder_text="Search Anything", width=400)
    search_bar.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="we")

    # Subjects section inside left frame
    subjects_frame = ctk.CTkFrame(left_frame, fg_color="#fff", corner_radius=10,height=25)
    subjects_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    subjects = ["Mathematics", "English", "Science", "Comp. Science"]

    for i, subject in enumerate(subjects):
        subject_button = ctk.CTkButton(subjects_frame, text=subject, width=100, height=25)
        subject_button.grid(row=0, column=i, padx=5, pady=5)

    # Right container frame (for image)
    right_frame = ctk.CTkFrame(content_frame,height=50,width=200)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Load and display image inside right frame
    image = Image.open("./images/courses.png")
    image = image.resize((400, 300))  # Resize image if necessary
    image_tk = ImageTk.PhotoImage(image)
    image_label = ctk.CTkLabel(right_frame, image=image_tk, text="")
    image_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    # Progress Chart section
    progress_frame = ctk.CTkFrame(content_frame, fg_color="#fff", corner_radius=10)
    progress_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    progress_label = ctk.CTkLabel(progress_frame, text="Course Progress", font=("Arial", 18, "bold"))
    progress_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

    last_month_label = ctk.CTkLabel(progress_frame, text="Last month", font=("Arial", 14))
    last_month_label.grid(row=0, column=1, sticky="e", padx=10, pady=(10, 0))

    image_path = "./images/chart.png"
    pil_image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(pil_image)

    # Placeholder for chart
    chart_placeholder = ctk.CTkLabel(progress_frame, image=tk_image, text="", width=400, height=200, fg_color="#e9ecef", corner_radius=10)
    chart_placeholder.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    # Timetable section
    timetable_frame = ctk.CTkFrame(content_frame, fg_color="#fff", corner_radius=10)
    timetable_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    timetable_label = ctk.CTkLabel(timetable_frame, text="Timetable", font=("Arial", 18, "bold"))
    timetable_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # Timetable with alternating colors
    days = ["Sun", "Mon", "Tue", "Thu", "Fri", "Sat"]
    for i, day in enumerate(days):
        day_label = ctk.CTkLabel(timetable_frame, text=day, width=50, fg_color="#fff", corner_radius=10)
        day_label.grid(row=1, column=i, padx=5, pady=5, sticky="nsew")

    time_slots = ["8 to 3"] * len(days)
    for i, slot in enumerate(time_slots):
        slot_color = "#fff" if i % 2 == 0 else "#E1E5F0"
        slot_label = ctk.CTkLabel(timetable_frame, text=slot, width=50, fg_color=slot_color, corner_radius=10)
        slot_label.grid(row=2, column=i, padx=5, pady=5, sticky="nsew")


