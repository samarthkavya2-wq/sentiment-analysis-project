"""
database.py — Database Connection Module (SQLite version)

Switched from MySQL to SQLite for free hosting on Render.com.
SQLite stores data in a single file (sentixai.db) — no server needed.

The database file is automatically created on first run.
"""

import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Path to the SQLite database file
# On Render: stored in /opt/render/project/src/sentixai.db (persistent disk)
# Locally:   stored in the project folder
DB_PATH = os.environ.get('DB_PATH', os.path.join(os.path.dirname(__file__), 'sentixai.db'))


def get_db_connection():
    """
    Create and return a connection to the SQLite database.

    Returns rows as dictionaries (same behaviour as MySQL's dictionary=True cursor).
    The database file is created automatically if it does not exist.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # rows behave like dicts: row['column_name']
    conn.execute('PRAGMA journal_mode=WAL')   # better concurrent read performance
    conn.execute('PRAGMA foreign_keys = ON')  # enforce ON DELETE CASCADE
    return conn


def init_db():
    """
    Create tables and seed the admin account if they don't already exist.
    Called automatically when the Flask app starts.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            username  TEXT UNIQUE NOT NULL,
            email     TEXT UNIQUE NOT NULL,
            password  TEXT NOT NULL,
            is_admin  INTEGER DEFAULT 0,
            created_at TEXT DEFAULT (datetime('now'))
        )
    ''')

    # Create posts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER NOT NULL,
            text_content TEXT NOT NULL,
            sentiment    TEXT NOT NULL,
            polarity     REAL NOT NULL,
            subjectivity REAL NOT NULL,
            confidence   REAL NOT NULL,
            created_at   TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')

    # Seed default admin account (password: admin123)
    cursor.execute('''
        INSERT OR IGNORE INTO users (id, username, email, password, is_admin)
        VALUES (
            7,
            'admin',
            'admin@sentix.ai',
            'scrypt:32768:8:1$DwkOn76BkPQcWDYT$fa3dd32db66a23a5604e72b09938f215d42edcbd28def9dc739c9062d41589d18ec38976e501c8ad025e1a4d28cee7c10b96da323c9c7c138f963c9d0cdd2ed4',
            1
        )
    ''')

    conn.commit()
    conn.close()
    print(f"[DATABASE] SQLite database ready at: {DB_PATH}")
