import customtkinter as ctk
import os
from datetime import datetime
from database.handler import read_records, create_record, update_record


def show_login(conn):
    # Initialize the CustomTkinter application
    app = ctk.CTk()
    app.title("Login Form")
    app.geometry("400x300")

    def login():
        username = entry_username.get()
        password = entry_password.get()

        # Hardcoded admin check
        if username == 'admin' and password == 'password':
            print("Admin login successful")
            app.destroy()  # Close the login window
            os.system('python ./admin/main.py')  # Redirect to admin/main.py
            return

        # For non-admin users, check credentials in the database
        users = read_records(conn, 'students', where_clause=f"name = '{username}' AND password = '{password}'")

        if users:
            user = users[0]  # Get the first (and should be only) user
            user_type = user[4]  # Assuming 'type' is the 5th column (index 4)
            print(f"Login successful for user: {username}")

            # Update attendance only if user is a student
            if user_type == 'Student':
                current_date = datetime.now().strftime("%Y-%m-%d")  # e.g., "2024-08-17"

                # Check if attendance record exists for the current date
                existing_attendance = read_records(conn, 'attendance',
                                                   columns=['*'],
                                                   where_clause=f"username = '{username}' AND date = '{current_date}'")

                print(existing_attendance)
                total_days = 1  # Only one day of attendance per login
                present_days = 1  # Increment present days by 1
                percentage = f"{(present_days / total_days) * 100:.2f}%"
                color = "#ff0000"  # Example color

                if not existing_attendance:
                    # Create new attendance record
                    create_record(conn, 'attendance',
                                  columns=('username', 'date', 'total_days', 'present_days', 'percentage', 'color'),
                                  values=(username, current_date, total_days, present_days, percentage, color))
                    print(f"New attendance record created for {username}")
                else:
                    # Update existing attendance record
                    update_record(conn, 'attendance',
                                  updates={
                                      'present_days': present_days,
                                      'percentage': percentage,
                                      'color': color
                                  },
                                  where_clause=f"username = '{username}' AND date = '{current_date}'")
                    print(f"Attendance record updated for {username}")

            app.destroy()  # Close the login window

            if user_type == 'Student':
                os.system('python ./student/main.py')  # Redirect to student/main.py
            elif user_type == 'Teacher':
                os.system('python ./teacher/main.py')  # Redirect to teacher/main.py
            else:
                print(f"Unknown user type: {user_type}")
        else:
            print("Invalid username or password")

    # Title label
    label_title = ctk.CTkLabel(app, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
    label_title.pack(pady=20)

    # Username label and entry
    label_username = ctk.CTkLabel(app, text="Username:")
    label_username.pack(pady=10)
    entry_username = ctk.CTkEntry(app, width=300)
    entry_username.pack()

    # Password label and entry
    label_password = ctk.CTkLabel(app, text="Password:")
    label_password.pack(pady=10)
    entry_password = ctk.CTkEntry(app, width=300, show="*")
    entry_password.pack()

    # Login button
    button_login = ctk.CTkButton(app, text="Login", command=login)
    button_login.pack(pady=20)

    # Run the CustomTkinter main loop
    app.mainloop()
