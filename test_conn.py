
from db_conn import connect_db

# Test the database connection
test = connect_db()

if test is not None:
    print("Database connected successfully.")
else:
    print("Failed to connect to database.")
