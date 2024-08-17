import customtkinter as ctk
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from side_topbar import create_sidebar
from settings import create_settings_content
from dashboard import create_dashboard_content
from courses import create_courses_content
from students import create_students_content
from attendance import create_attendance_content

from database.connection import create_connection
from database.handler import create_record,read_records


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

def switch_view(view_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
 
    if view_name == "settings":
        create_settings_content(content_frame)
    elif view_name == "dashboard":
        create_dashboard_content(content_frame)
    elif view_name == "courses":
        create_courses_content(content_frame)
    elif view_name == "students":
        create_students_content(content_frame)
    elif view_name == "attendance":
        create_attendance_content(content_frame)


# Create the sidebar and top bar
create_sidebar(app, switch_view)


# Create the initial dashboard content
content_frame = ctk.CTkFrame(app, fg_color="#fff")
content_frame.grid(row=1, column=1, sticky="nswe", padx=20, pady=20)
switch_view("dashboard")

# Run the application
app.mainloop()
