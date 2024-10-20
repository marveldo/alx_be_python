import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL server host
            user='root',  # Replace with your MySQL username
            password='Winner174'  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            # Create the database alx_book_store if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message if there's a failure
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()