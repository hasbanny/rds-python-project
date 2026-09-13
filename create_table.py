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

CREAT_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS raw_sales(
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    sale_date DATE NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Successfully connected to RDS MySQL database")
        cursor = connection.cursor()
        
        cursor.execute("SELECT DATABASE();")
        print(cursor.fetchone())

        cursor.execute(CREAT_TABLE_QUERY)
        connection.commit()
        print("Table 'raw_sales' created successfully")

        cursor.execute("show tables;")
        tables = cursor.fetchall()
        print(f"Tables in database:", tables)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")