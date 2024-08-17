import customtkinter as ctk

def create_settings_content(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")

    # Create a shadowed border effect
    border_frame = ctk.CTkFrame(content_frame, fg_color="#ddd", width=400, height=400)
    border_frame.pack(padx=10, pady=10, expand=True, fill='both')

    inner_frame = ctk.CTkFrame(border_frame, fg_color="#fff")
    inner_frame.pack(padx=10, pady=10, expand=True, fill='both')

    settings_label = ctk.CTkLabel(inner_frame, text="Settings and Profile", font=("Arial", 20))
    settings_label.pack(pady=20)

    # Search Bar
    search_frame = ctk.CTkFrame(inner_frame, fg_color="#f0f0f0")
    search_frame.pack(pady=10, fill='x')
    
    search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search...")
    search_entry.pack(pady=5, padx=10, fill='x')

    # Link-like buttons
    buttons_frame = ctk.CTkFrame(inner_frame, fg_color="#fff")
    buttons_frame.pack(pady=10, fill='x')

    button_names = ["Account Information", "Update Password", "Notification", "About"]
    for name in button_names:
        button = ctk.CTkButton(
            buttons_frame,
            text=name,
            fg_color="#fff",
            text_color="#000",  # Set text color to black
            hover_color="#e0e0e0",
            width=300,
            height=40
        )
        button.pack(pady=5)