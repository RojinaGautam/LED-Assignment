import customtkinter as ctk
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from side_topbar import create_sidebar
from dashboard import create_dashboard_content
from settings import create_settings_content
from attendance import create_attendance_content
from tasks import create_task_content
from results import create_result_content
from profile import create_self_profile
from database.connection import create_connection

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
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Retrieve user ID from command-line arguments
user_id = sys.argv[1] if len(sys.argv) > 1 else None

conn = create_connection('assignment.db')

def switch_view(view_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    if view_name == "dashboard":
        create_dashboard_content(content_frame)
    elif view_name == "settings":
        create_settings_content(content_frame,user_id,conn)
    elif view_name == "attendance":
        create_attendance_content(content_frame)
    elif view_name == "tasks":
        create_task_content(content_frame)
    elif view_name == "results":
        create_result_content(content_frame)
    elif view_name == "profile":
        create_self_profile(content_frame,user_id,conn)
    # Add more elif blocks for other views as needed

# Create the sidebar and top bar
create_sidebar(app, switch_view)

# Create the initial dashboard content
content_frame = ctk.CTkFrame(app, fg_color="#fff")
content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)
switch_view("dashboard")

# Display the user ID in the title bar or a label
if user_id:
    label_user_id = ctk.CTkLabel(app, text=f"User ID: {user_id}", font=ctk.CTkFont(size=16, weight="bold"))
    label_user_id.grid(row=0, column=1, pady=10)

# Run the application
app.mainloop()
