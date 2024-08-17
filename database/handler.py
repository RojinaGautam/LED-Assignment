import sqlite3

def create_record(conn, table, columns, values):
    """
    Create a new record in the specified table.
    :param conn: Connection object
    :param table: Table name
    :param columns: Tuple of column names
    :param values: Tuple of values to insert
    """
    placeholders = ', '.join(['?'] * len(values))
    sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Record created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating record: {e}")

def read_records(conn, table, columns='*', where_clause=None):
    """
    Read records from the specified table.
    :param conn: Connection object
    :param table: Table name
    :param columns: Columns to select (default is all columns)
    :param where_clause: Optional WHERE clause to filter records
    :return: List of records (rows)
    """
    sql = f"SELECT {', '.join(columns)} FROM {table}"
    if where_clause:
        sql += f" WHERE {where_clause}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error reading records: {e}")
        return []

def update_record(conn, table, updates, where_clause):
    """
    Update an existing record in the specified table.
    :param conn: Connection object
    :param table: Table name
    :param updates: Dictionary of column-value pairs to update
    :param where_clause: WHERE clause to specify which record(s) to update
    """
    set_clause = ', '.join([f"{col} = ?" for col in updates.keys()])
    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

    try:
        cur = conn.cursor()
        cur.execute(sql, tuple(updates.values()))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

def delete_record(conn, table, where_clause):
    """
    Delete a record from the specified table.
    :param conn: Connection object
    :param table: Table name
    :param where_clause: WHERE clause to specify which record(s) to delete
    """
    sql = f"DELETE FROM {table} WHERE {where_clause}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting record: {e}")
