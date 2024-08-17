# main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import create_connection
from login import show_login 

def main():
    db_path = 'assignment.db'
    
    # Check if the database file exists
    if not os.path.isfile(db_path):
        print(f"The database file '{db_path}' does not exist.")
        return

    # Establish a connection to the existing database
    conn = create_connection(db_path)
    
    if conn:
        # Show the login form
        show_login(conn)

        # Close the database connection after the login form is handled
        conn.close()

if __name__ == "__main__":
    main()

