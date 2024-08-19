import customtkinter as ctk
from tkinter import messagebox
from database.connection import create_connection
from database.handler import create_record
from PIL import Image

def admin_dashboard(master):
    global content_frame
    # Main content frame
    content_frame = ctk.CTkFrame(master, fg_color="#fff")
    content_frame.grid(row=1, column=1, sticky="nsew")
    master.grid_columnconfigure(1, weight=1)
    master.grid_rowconfigure(1, weight=1)
    
    # Top bar frame
    top_bar = ctk.CTkFrame(content_frame, fg_color="#fff", height=60)
    top_bar.grid(row=0, column=0, sticky="ew")
    content_frame.grid_columnconfigure(0, weight=1)
    
    # Top bar content
    webinar_label = ctk.CTkLabel(top_bar, text="Learn how to launch faster\nwatch our webinar for tips from our experts and get a limited time offer.", 
                                 font=("Arial", 16))
    webinar_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
    
    notification_button = ctk.CTkButton(top_bar, text="", width=20, height=20, fg_color="#3498db")
    notification_button.grid(row=0, column=1, padx=(0, 10))
    
    logout_button = ctk.CTkButton(top_bar, text="Log out", fg_color="#3498db")
    logout_button.grid(row=0, column=2, padx=10)
    
    top_bar.grid_columnconfigure(0, weight=1)
    
    # Horizontal line
    line = ctk.CTkFrame(content_frame, height=2, fg_color="#e0e0e0")
    line.grid(row=1, column=0, sticky="ew", pady=(0, 20))
    
    # Welcome Label
    welcome_label = ctk.CTkLabel(content_frame, text="Welcome to your dashboard, Academiahub", 
                                 font=("Arial", 24, "bold"))
    welcome_label.grid(row=2, column=0, pady=(20, 10), padx=20, sticky="ew")
    
    # User Email Label
    email_label = ctk.CTkLabel(content_frame, text="Academiahub/teacher/@teachable.com", 
                               font=("Arial", 16))
    email_label.grid(row=3, column=0, pady=(0, 40), padx=20, sticky="ew")
    
    # Options frame
    options_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    options_frame.grid(row=4, column=0, pady=(0, 40), padx=20, sticky="nsew")
    content_frame.grid_rowconfigure(4, weight=1)
    options_frame.grid_columnconfigure(0, weight=1)
    options_frame.grid_columnconfigure(1, weight=3)
    
    def create_option(row, icon, text, description):
        icon_label = ctk.CTkLabel(options_frame, text="", image=icon, width=30, height=30)
        icon_label.grid(row=row, column=0, padx=(0, 20), pady=(0, 30), sticky="w")
        
        text_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        text_frame.grid(row=row, column=1, sticky="w")
        
        option_label = ctk.CTkLabel(text_frame, text=text, font=("Arial", 18, "bold"))
        option_label.grid(row=0, column=0, sticky="w")
        
        desc_label = ctk.CTkLabel(text_frame, text=description, font=("Arial", 14), text_color="gray")
        desc_label.grid(row=1, column=0, pady=(5, 0), sticky="w")

    # Creating options
    admin_icon = ctk.CTkImage(Image.open("./images/tution.png"), size=(30, 30))
    create_option(0, admin_icon, "Add other admins", 
                  "Create rich course content and coaching products for your students.\nWhen you give them a pricing plan, they'll appear on your site!")
    
    classes_icon = ctk.CTkImage(Image.open("./images/tution.png"), size=(30, 30))
    create_option(1, classes_icon, "Add classes", 
                  "Create rich course content and coaching products for your students.\nWhen you give them a pricing plan, they'll appear on your site!")
    
    students_icon = ctk.CTkImage(Image.open("./images/tution.png"), size=(30, 30))
    create_option(2, students_icon, "Add students", 
                  "Create rich course content and coaching products for your students.\nWhen you give them a pricing plan, they'll appear on your site!")


