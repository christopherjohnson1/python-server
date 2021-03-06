import sqlite3
import json
from models import Employee

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                        data['location_id'])

        return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        # Initialize an empty list to hold employee representations
        employees = []

        data = db_cursor.fetchall()

        # Create an animal instance from the current row
        for row in data:

            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])

            employees.append(employee.__dict__)

        # Return the JSON serialized animal object
        return json.dumps(employees)

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

        rows_affected = db_cursor.rowcount # 0 or 1

        if rows_affected == 0:
            return False
        else:
            return True