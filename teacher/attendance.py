import customtkinter as ctk
import sqlite3
from database.connection import create_connection

def create_attendance_content(master):
    # Create the frame for the table
    table_frame = ctk.CTkFrame(master, fg_color="#f8f9fa", corner_radius=10)
    table_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    # Define column headers
    columns = ["Student Name", "Date", "Attendance Status"]

    # Create table header
    for col, column in enumerate(columns):
        header_label = ctk.CTkLabel(table_frame, text=column, font=("Arial", 14, "bold"))
        header_label.grid(row=0, column=col, padx=10, pady=10)

    # Fetch and display attendance data
    conn = create_connection("assignment.db")
    query = """
    SELECT 
        s.name AS student_name,
        a.date,
        CASE 
            WHEN a.present_days > 0 THEN 'Present' 
            ELSE 'Absent' 
        END AS attendance_status
    FROM 
        students s
    LEFT JOIN 
        attendance a ON s.name = a.username AND a.date = DATE('now')
    WHERE 
        s.type = 'Student'
    ORDER BY 
        s.name, a.date;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    # Populate table with data
    for row_index, row in enumerate(rows):
        for col_index, item in enumerate(row):
            item_label = ctk.CTkLabel(table_frame, text=item, font=("Arial", 12))
            item_label.grid(row=row_index + 1, column=col_index, padx=10, pady=5)


