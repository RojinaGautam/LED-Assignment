import customtkinter as ctk
import os
from PIL import Image, ImageTk

def create_sidebar_button(master, text, icon_path, command):
    # Load the icon image
    if os.path.isfile(icon_path):
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20))  
        icon = ImageTk.PhotoImage(icon_image)
    else:
        icon = None

    # Create the CTkButton with the given text and icon
    button = ctk.CTkButton(
        master,
        text=text,
        fg_color="#154892",
        text_color="white",
        image=icon,
        compound="left",
        width=180, 
        anchor="w",
        command=command
    )
    
    button.icon = icon
    
    return button

def create_sidebar(master, switch_view):
    # Define buttons and their corresponding icon paths
    buttons = [
        ("Users", "./images/button-icons/dashboard.png", lambda: switch_view("student")),
        ("Announcement", "./images/button-icons/dashboard.png", lambda: switch_view("announcement")),
        ("Tutions", "./images/button-icons/teacher_copy.png", lambda: switch_view("tutions")),
        ("Fees", "./images/button-icons/bank.png", lambda: switch_view("fees")),
        ("Settings and profile", "./images/button-icons/setting-2.png", lambda: switch_view("settings")),
        ("Dashboard", "./images/button-icons/chart-square.png", lambda: switch_view("dashboard"))
    ]

    # Create the sidebar frame
    sidebar_frame = ctk.CTkFrame(master, width=200, fg_color="#3FAEFF")
    sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nswe")

    # Configure grid layout for sidebar_frame
    sidebar_frame.grid_rowconfigure(len(buttons) + 2, weight=1)  # Added +2 for image and title rows

    # Load and display the top image
    if os.path.isfile("./images/top-image.png"):
        top_image = Image.open("./images/top-image.png")
        top_image = top_image.resize((180, 100))  # Resize the image to fit the sidebar
        top_photo = ImageTk.PhotoImage(top_image)
    else:
        top_photo = None

    top_image_label = ctk.CTkLabel(sidebar_frame, image=top_photo, bg_color="#3FAEFF")
    top_image_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    # Keep a reference to the image to prevent it from being garbage collected
    top_image_label.image = top_photo

    # Add the AcademiaHub text label below the image
    title_label = ctk.CTkLabel(sidebar_frame, text="AcademiaHub", font=("Arial", 16, "bold"), fg_color="#3FAEFF", text_color="white")
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky="n")

    # Add buttons to the sidebar with icons
    for idx, (text, icon_path, command) in enumerate(buttons):
        button = create_sidebar_button(sidebar_frame, text=text, icon_path=icon_path, command=command)
        button.grid(row=idx + 2, column=0, padx=10, pady=5, sticky="we")  # Adjusted row index

    # Add the "Features" section with yellow color
    features_frame = ctk.CTkFrame(sidebar_frame, fg_color="yellow")
    features_frame.grid(row=len(buttons) + 2, column=0, padx=20, pady=10, sticky="we")

    # Load and display the icon
    if os.path.isfile("./images/button-icons/bank.png"):
        icon_image = Image.open("./images/button-icons/bank.png")
        icon_image = icon_image.resize((20, 20))  # Resize the icon to fit the label
        icon = ImageTk.PhotoImage(icon_image)
    else:
        icon = None

    icon_label = ctk.CTkLabel(features_frame, image=icon, bg_color="yellow")
    icon_label.pack(side="left", padx=5)

    # Keep a reference to the icon to prevent it from being garbage collected
    icon_label.image = icon

    # Add the Features text
    features_label = ctk.CTkLabel(features_frame, text="Features", fg_color="yellow", text_color="black")
    features_label.pack(side="left")

    # Add the "NEW" label inside a grey circular background
    new_frame = ctk.CTkFrame(features_frame, width=30, height=30, corner_radius=15, fg_color="grey")
    new_frame.pack(side="right", padx=5, pady=5)

    new_label = ctk.CTkLabel(new_frame, text="NEW", text_color="white")
    new_label.pack(expand=True, fill="both")
