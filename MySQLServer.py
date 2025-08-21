# File: MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',      # MySQL host
            user='root',           # MySQL username
            password=''            # MySQL password
        )

        # Check if connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle any error while connecting or executing SQL
        print(f"Error: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__mai
