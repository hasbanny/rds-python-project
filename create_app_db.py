from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Successfully connected to RDS MySQL database")
        cursor = connection.cursor()
       
        cursor.execute("CREATE DATABASE myapp_db")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

