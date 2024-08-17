import customtkinter as ctk
from PIL import Image

def create_tuition_schedule(master):
    global content_frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)

    # Configure grid layout for content_frame
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Log out button at the top right
    logout_button = ctk.CTkButton(content_frame, text="Log out", fg_color="#3498db", text_color="#fff")
    logout_button.grid(row=0, column=1, sticky="ne", padx=20, pady=10)

    # Tuition Schedule Title
    schedule_title = ctk.CTkLabel(content_frame, text="Tuition Schedule 2023/2024", font=("Arial", 18))
    schedule_title.grid(row=0, column=0, sticky="n", pady=10)

    # Image in the middle (replace with the appropriate image path)
    image_path = "./images/tution.png" 
    image = Image.open(image_path)  
    ctk_image = ctk.CTkImage(image, size=(120, 120))
    image_label = ctk.CTkLabel(content_frame, image=ctk_image, text="")
    image_label.grid(row=1, column=0, pady=10)

    # Tuition table frame
    table_frame = ctk.CTkFrame(content_frame, fg_color="#e3f2fd", border_color="#3498db", border_width=2)
    table_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nswe")

    # Configure grid for table_frame
    table_frame.grid_columnconfigure((0, 1, 2), weight=1)

    # Table Headers
    headers = ["Tuition Category", "Tuition Per Annum", "Tuition per Month"]
    for i, header in enumerate(headers):
        header_label = ctk.CTkLabel(table_frame, text=header, font=("Arial", 14, "bold"), fg_color="#3498db", text_color="#fff")
        header_label.grid(row=0, column=i, sticky="we", padx=2, pady=2)

    # Table Content
    rows = [
        ("Elementary School students", "Rs: 5,000", "RS 8,000 to 12,500"),
        ("Secondary School students", "Rs: 6,000", "RS 13,000 to 15,000"),
        ("Middle school students", "Rs: 10,000", "RS 16,000 to 20,000"),
        ("High school students", "Rs: 5,500", "RS 21,000 to 25,000"),
    ]

    for i, row in enumerate(rows, start=1):
        for j, item in enumerate(row):
            content_label = ctk.CTkLabel(table_frame, text=item, font=("Arial", 14), anchor="w")
            content_label.grid(row=i, column=j, sticky="we", padx=2, pady=2)

