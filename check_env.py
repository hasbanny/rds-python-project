# Dotenv is a library/module that loads environment variables 
# from a `.env` file into your application's runtime environment, 
# securely managing sensitive data like API keys without 
# hardcoding them.
from dotenv import load_dotenv

# module to access functions to interact with the OS
import os

load_dotenv()
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_NAME:", os.getenv("DB_NAME"))