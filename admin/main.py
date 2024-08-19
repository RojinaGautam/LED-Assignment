import os
import sys
import customtkinter as ctk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from side_topbar import create_sidebar
from students import create_student_content
from announcement import create_announcement_content
from tution import create_tuition_schedule

# from dashboard import admin_dashboard
from admin.addstudent import addstudent_content


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

# Create the initial content frame
content_frame = ctk.CTkFrame(app, fg_color="#fff")
content_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

def switch_view(view_name):
    # Clear current content
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Load the selected view
    if view_name == "student":
        create_student_content(content_frame, switch_view)
    elif view_name == "add_student":
        addstudent_content(content_frame)
    elif view_name == "announcement":
        create_announcement_content(content_frame)
    elif view_name == "tutions":
        create_tuition_schedule(content_frame)
    # elif view_name == "dashboard":
    #     admin_dashboard(content_frame)

# Create the sidebar and top bar
create_sidebar(app, switch_view)

# Load the initial dashboard content
switch_view("dashboard")

# Run the application
app.mainloop()
