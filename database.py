"""
database.py — Database Connection Module

This file handles the connection between Python and MySQL.
Think of it as the "bridge" between your website and your database.

Every time the website needs to store or retrieve data, it uses
the function in this file to connect to MySQL.
"""

import mysql.connector  # This is the library that lets Python talk to MySQL
import os  # Used to read environment variables


def get_db_connection():
    """
    Create and return a connection to the MySQL database.
    
    In production (PythonAnywhere), the database connection details
    come from environment variables. This keeps passwords safe.
    Locally, it reads from the .env file via python-dotenv.
    
    The os.environ.get('VAR', 'default') means:
    - First try to read the environment variable 'VAR'
    - If it doesn't exist, use 'default' as the fallback value
    """
    connection = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'applet'),
        database=os.environ.get('DB_NAME', 'sentiment_analysis')
    )
    return connection
