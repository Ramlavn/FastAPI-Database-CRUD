
from db_conn import conn_db

# Test the database connection
test = conn_db()

if test is not None:
    print("Database connected successfully.")
else:
    print("Failed to connect to database.")
