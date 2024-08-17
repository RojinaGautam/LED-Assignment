import customtkinter as ctk

def create_self_profile(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(3, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Create a blue header for the title
    header_frame = ctk.CTkFrame(content_frame, fg_color="#3498db")
    header_frame.grid(row=0, column=0, columnspan=2, sticky="we")
    

    # Add a tab frame for "Your Personal Details" and "Documents"
    tab_frame = ctk.CTkFrame(content_frame, fg_color="#ecf0f1")
    tab_frame.grid(row=1, column=0, columnspan=2, sticky="we", padx=20, pady=10)
    
    personal_details_button = ctk.CTkButton(tab_frame, text="Your Personal Details", width=150, fg_color="#ffffff", hover_color="#3498db")
    personal_details_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    documents_button = ctk.CTkButton(tab_frame, text="Documents", width=100, fg_color="#3498db", hover_color="#2980b9")
    documents_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Create a profile details frame
    details_frame = ctk.CTkFrame(content_frame, fg_color="#fff")
    details_frame.grid(row=2, column=0, columnspan=2, sticky="nswe", padx=20, pady=20)

    # Left-side details
    left_frame = ctk.CTkFrame(details_frame, fg_color="#fff")
    left_frame.grid(row=0, column=0, padx=20, pady=10)

    gender_label = ctk.CTkLabel(left_frame, text="Gender", font=("Arial", 14))
    gender_label.grid(row=0, column=0, sticky="w", pady=5)
    gender_entry = ctk.CTkEntry(left_frame, width=150)
    gender_entry.grid(row=1, column=0, sticky="w", pady=5)

    contact_label = ctk.CTkLabel(left_frame, text="Contact no.", font=("Arial", 14))
    contact_label.grid(row=2, column=0, sticky="w", pady=5)
    contact_entry = ctk.CTkEntry(left_frame, width=150)
    contact_entry.grid(row=3, column=0, sticky="w", pady=5)

    parents_name_label = ctk.CTkLabel(left_frame, text="Parents Name", font=("Arial", 14))
    parents_name_label.grid(row=4, column=0, sticky="w", pady=5)
    parents_name_entry = ctk.CTkEntry(left_frame, width=150)
    parents_name_entry.grid(row=5, column=0, sticky="w", pady=5)

    # Center avatar
    avatar_frame = ctk.CTkFrame(details_frame, fg_color="#ffffff", width=200, height=200)
    avatar_frame.grid(row=0, column=1, padx=50, pady=10, sticky="n")
    
    avatar_label = ctk.CTkLabel(avatar_frame, text="👤", font=("Arial", 72), text_color="#7f8c8d")
    avatar_label.place(relx=0.5, rely=0.5, anchor="center")

    # Right-side details
    right_frame = ctk.CTkFrame(details_frame, fg_color="#fff")
    right_frame.grid(row=0, column=2, padx=20, pady=10)

    address_label = ctk.CTkLabel(right_frame, text="Address", font=("Arial", 14))
    address_label.grid(row=0, column=0, sticky="w", pady=5)
    address_entry = ctk.CTkEntry(right_frame, width=150)
    address_entry.grid(row=1, column=0, sticky="w", pady=5)

    school_label = ctk.CTkLabel(right_frame, text="School", font=("Arial", 14))
    school_label.grid(row=2, column=0, sticky="w", pady=5)
    school_entry = ctk.CTkEntry(right_frame, width=150)
    school_entry.grid(row=3, column=0, sticky="w", pady=5)

    parents_email_label = ctk.CTkLabel(right_frame, text="Parents email", font=("Arial", 14))
    parents_email_label.grid(row=4, column=0, sticky="w", pady=5)
    parents_email_entry = ctk.CTkEntry(right_frame, width=150)
    parents_email_entry.grid(row=5, column=0, sticky="w", pady=5)
