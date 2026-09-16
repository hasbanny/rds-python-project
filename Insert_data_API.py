from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
import requests
from datetime import datetime, timedelta
import random

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

#fetch data from api
response=requests.get("https://dummyjson.com/products?limit=30")
data = response.json()
products = data["products"]

#generate random sales date
def random_sale_date():
    #date within the last 90 days
    days_ago=random.randint(0,90)
    return(datetime.now()-timedelta(days=days_ago)).date()

#connect to db
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Successfully connected to RDS MySQL database")
        cursor = connection.cursor()

        #insert data into db
        for product in products:
            product_name = product["title"]
            quantity = product["stock"]
            unit_price = round(product["price"],2)
            total_amount = round(quantity * unit_price,2)
            sale_date = random_sale_date()

            insert_query = """
            INSERT INTO raw_sales (product_name, quantity, unit_price, total_amount, sale_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (product_name, quantity, unit_price, total_amount, sale_date))

        connection.commit()
        print(f"{cursor.rowcount} records inserted successfully into raw_sales table")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")