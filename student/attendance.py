import customtkinter as ctk

def create_attendance_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")

    # Title
    title_label = ctk.CTkLabel(
        content_frame, 
        text="My Monthly Attendance", 
        font=("Arial", 30, "bold"), 
        text_color="#000"
    )
    title_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    # Attendance Data
    months = ["Oct 2023", "Nov 2023", "Dec 2023"]
    percentages = ["100%", "99%", "76%"]
    total_days = [50, 40, 40]
    present_days = [50, 39, 25]
    colors = ["#00bfff", "#00bfff", "#ff6347"]

    for i in range(3):
        attendance_frame = ctk.CTkFrame(content_frame, fg_color="#f9f9f9", corner_radius=10)
        attendance_frame.grid(row=1, column=i, padx=10, pady=10, sticky="nswe")

        month_label = ctk.CTkLabel(attendance_frame, text=months[i], font=("Arial", 16, "bold"))
        month_label.pack(pady=10)

        percentage_label = ctk.CTkLabel(
            attendance_frame, 
            text=percentages[i], 
            font=("Arial", 40, "bold"), 
            text_color=colors[i]
        )
        percentage_label.pack(pady=20)

        total_days_label = ctk.CTkLabel(
            attendance_frame, 
            text=f"Total days: {total_days[i]}", 
            font=("Arial", 14), 
            text_color="#000"
        )
        total_days_label.pack()

        present_days_label = ctk.CTkLabel(
            attendance_frame, 
            text=f"Present days: {present_days[i]}", 
            font=("Arial", 14), 
            text_color="#000"
        )
        present_days_label.pack()

