import sqlite3

# Connect/Create Database
conn = sqlite3.connect("events.db")

# Create Cursor
cursor = conn.cursor()

# Create Events Table
cursor.execute("""

CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_name TEXT NOT NULL,

    event_date TEXT NOT NULL,

    event_location TEXT,

    event_description TEXT,

    status TEXT DEFAULT 'Pending'

)

""")

print("Database and Events table created successfully!")

# CREATE REGISTRATIONS TABLE

cursor.execute("""

CREATE TABLE IF NOT EXISTS registrations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    firstname TEXT NOT NULL,

    lastname TEXT NOT NULL,

    email TEXT NOT NULL,

    event_name TEXT NOT NULL,

    event_date TEXT NOT NULL,

    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")

# Save changes
conn.commit()

# Close connection
conn.close()