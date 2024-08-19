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
            user = users[0]
            user_id = user[0]  # Assume user ID is the first column
            user_type = user[4]  # Assume user type is the fifth column
            print(f"Login successful for user: {username}")

            # Update attendance only if user is a student
            if user_type == 'Student':
                current_date = datetime.now().strftime("%Y-%m-%d")

                # Check if attendance record exists for the current date
                existing_attendance = read_records(conn, 'attendance',
                                                   columns=['*'],
                                                   where_clause=f"username = '{username}' AND date = '{current_date}'")

                total_days = 1
                present_days = 1
                percentage = f"{(present_days / total_days) * 100:.2f}%"
                color = "#ff0000"

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
                os.system(f'python ./student/main.py {user_id}')  # Pass the user ID to the student script
            elif user_type == 'Teacher':
                os.system(f'python ./teacher/main.py {user_id}')  # Pass the user ID to the teacher script
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
