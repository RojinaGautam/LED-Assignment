import customtkinter as ctk
from database.handler import read_records

def create_self_profile(master, user_id, conn):
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

    name_label = ctk.CTkLabel(left_frame, text="Name", font=("Arial", 14))
    name_label.grid(row=0, column=0, sticky="w", pady=5)
    name_entry = ctk.CTkEntry(left_frame, width=150)
    name_entry.grid(row=1, column=0, sticky="w", pady=5)

    gender_label = ctk.CTkLabel(left_frame, text="Gender", font=("Arial", 14))
    gender_label.grid(row=2, column=0, sticky="w", pady=5)
    gender_entry = ctk.CTkEntry(left_frame, width=150)
    gender_entry.grid(row=3, column=0, sticky="w", pady=5)

    phone_label = ctk.CTkLabel(left_frame, text="Phone", font=("Arial", 14))
    phone_label.grid(row=4, column=0, sticky="w", pady=5)
    phone_entry = ctk.CTkEntry(left_frame, width=150)
    phone_entry.grid(row=5, column=0, sticky="w", pady=5)

    # Center avatar
    avatar_frame = ctk.CTkFrame(details_frame, fg_color="#ffffff", width=200, height=200)
    avatar_frame.grid(row=0, column=1, padx=50, pady=10, sticky="n")
    
    avatar_label = ctk.CTkLabel(avatar_frame, text="👤", font=("Arial", 72), text_color="#7f8c8d")
    avatar_label.place(relx=0.5, rely=0.5, anchor="center")

    # Right-side details
    right_frame = ctk.CTkFrame(details_frame, fg_color="#fff")
    right_frame.grid(row=0, column=2, padx=20, pady=10)

    email_label = ctk.CTkLabel(right_frame, text="Email", font=("Arial", 14))
    email_label.grid(row=0, column=0, sticky="w", pady=5)
    email_entry = ctk.CTkEntry(right_frame, width=150)
    email_entry.grid(row=1, column=0, sticky="w", pady=5)

    # Fetch user details from the database
    user_details = read_records(conn, 'students', columns=['name', 'gender', 'phone', 'email'],
                                where_clause=f"id = {user_id}")

    if user_details:
        user = user_details[0]
        name_entry.insert(0, user[0])
        gender_entry.insert(0, user[1])
        phone_entry.insert(0, user[2])
        email_entry.insert(0, user[3])
