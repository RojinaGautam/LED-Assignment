import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os

def create_sidebar_button(master, text, icon_path):
    # Load the icon image
    if os.path.isfile(icon_path):
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20))  # Resize the icon to fit the button
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
        width=180,  # Set a fixed width for alignment
        anchor="w"  # Align text to the left
    )
    
    # Keep a reference to the icon to prevent it from being garbage collected
    button.icon = icon
    
    return button

# Set up the main application window
app = ctk.CTk()
app.title("AcademiaHub")

# Get screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set window size to screen width and height
app.geometry(f"{screen_width}x{screen_height}+0+0")

# Set the theme and scaling
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configure grid layout for the app
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Define buttons and their corresponding icon paths
buttons = [
    ("Dashboard", "./images/button-icons/dashboard.png"),
    ("Teachers", "./images/button-icons/dashboard.png"),
    ("Students/classes", "./images/button-icons/teacher_copy.png"),
    ("Fees", "./images/button-icons/bank.png"),
    ("Settings and profile", "./images/button-icons/setting-2.png"),
    ("Notice", "./images/button-icons/chart-square.png")
]

# Create the sidebar frame
sidebar_frame = ctk.CTkFrame(app, width=200, fg_color="#3FAEFF")
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
for idx, (text, icon_path) in enumerate(buttons):
    button = create_sidebar_button(sidebar_frame, text=text, icon_path=icon_path)
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

# Create the main content area frame
content_frame = ctk.CTkFrame(app, fg_color="#fff")
content_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

# Configure grid layout for content_frame
content_frame.grid_rowconfigure(3, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Add a top bar with a "Log out" button and a notification icon
top_bar_frame = ctk.CTkFrame(content_frame)
top_bar_frame.grid(row=0, column=0, sticky="we")

logout_button = ctk.CTkButton(top_bar_frame, text="Log out", width=100)
logout_button.pack(side="right", padx=10)

notification_icon = tk.Label(top_bar_frame, text="🔔")
notification_icon.pack(side="right", padx=10)

# Add the "My Learnings" label and search bar
my_learnings_label = ctk.CTkLabel(content_frame, text="My Learnings", font=("Arial", 20))
my_learnings_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

search_bar = ctk.CTkEntry(content_frame, placeholder_text="Search By title")
search_bar.grid(row=2, column=0, sticky="we", padx=10, pady=10)

# Create a frame for the learning modules
modules_frame = ctk.CTkFrame(content_frame, fg_color="#fff")
modules_frame.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)

# Example modules
modules = [
    ("Mathematics", 5, 15),
    ("Science", 8, 15),
    ("Computer Science", 6, 15)
]

for module in modules:
    module_frame = ctk.CTkFrame(modules_frame)
    module_frame.pack(pady=10, fill="x")

    title_label = ctk.CTkLabel(module_frame, text=module[0], font=("Arial", 16))
    title_label.grid(row=0, column=0, sticky="w")

    progress_label = ctk.CTkLabel(module_frame, text=f"Lesson completed {module[1]}/{module[2]}")
    progress_label.grid(row=1, column=0, sticky="w")

    go_button = ctk.CTkButton(module_frame, text="GO TO MODULE")
    go_button.grid(row=1, column=1, padx=10)

# Run the application
app.mainloop()
