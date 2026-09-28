"""
database.py — Database Connection Module

This file handles the connection between Python and MySQL.
Think of it as the "bridge" between your website and your database.

In production (PythonAnywhere, Render, Railway, etc.), the database 
connection details come from environment variables. This keeps passwords safe.
Locally, it reads from the .env file via python-dotenv.
"""

import os
import urllib.parse
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """
    Create and return a connection to the MySQL database.
    
    Supports:
    1. Direct DATABASE_URL (common on cloud hosts like Render/Railway):
       mysql://username:password@hostname:port/database_name
    2. Individual environment variables:
       - DB_HOST (default: localhost)
       - DB_PORT (default: 3306)
       - DB_USER (default: root)
       - DB_PASSWORD (default: applet)
       - DB_NAME (default: sentiment_analysis)
    3. Optional SSL configuration for cloud databases (Aiven, TiDB, etc.)
    """
    db_url = os.environ.get('DATABASE_URL')
    
    if db_url:
        parsed = urllib.parse.urlparse(db_url)
        conn_config = {
            'host': parsed.hostname or 'localhost',
            'port': parsed.port or 3306,
            'user': parsed.username or 'root',
            'password': urllib.parse.unquote(parsed.password or ''),
            'database': (parsed.path.lstrip('/') if parsed.path else 'sentiment_analysis')
        }
    else:
        conn_config = {
            'host': os.environ.get('DB_HOST', 'localhost'),
            'port': int(os.environ.get('DB_PORT', 3306)),
            'user': os.environ.get('DB_USER', 'root'),
            'password': os.environ.get('DB_PASSWORD', 'applet'),
            'database': os.environ.get('DB_NAME', 'sentiment_analysis')
        }
        
    # SSL support for cloud databases (e.g. Aiven, TiDB Cloud)
    ssl_ca = os.environ.get('DB_SSL_CA')
    if ssl_ca:
        conn_config['ssl_ca'] = ssl_ca
    elif os.environ.get('DB_SSL_MODE') == 'REQUIRED':
        conn_config['ssl_disabled'] = False
        
    # Set connection timeout to 10 seconds to avoid hanging on network delays
    conn_config['connection_timeout'] = int(os.environ.get('DB_TIMEOUT', 10))

    try:
        connection = mysql.connector.connect(**conn_config)
        return connection
    except mysql.connector.Error as err:
        print(f"[DATABASE ERROR] Could not connect to MySQL: {err}")
        print(f"[DATABASE CONFIG] Host: {conn_config.get('host')}:{conn_config.get('port')}, User: {conn_config.get('user')}, DB: {conn_config.get('database')}")
        raise err
