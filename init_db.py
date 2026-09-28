"""
init_db.py — Database Initialization Script

This script automatically sets up the MySQL tables and seeds the
admin account and sample data.

You can run this locally or on your deployed server (PythonAnywhere, Render, etc.):
    python init_db.py
"""

import os
import re
from database import get_db_connection

def run_sql_script(filename):
    print(f"[*] Reading {filename}...")
    if not os.path.exists(filename):
        print(f"[!] Error: File {filename} not found.")
        return False
        
    with open(filename, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    # Split SQL file into individual statements
    # Remove comments and empty lines
    lines = []
    for line in sql_content.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith('--'):
            lines.append(line)
    
    clean_sql = '\n'.join(lines)
    statements = [stmt.strip() for stmt in clean_sql.split(';') if stmt.strip()]

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        for stmt in statements:
            # Skip database creation/use if restricted by cloud MySQL provider
            if stmt.upper().startswith('CREATE DATABASE') or stmt.upper().startswith('USE '):
                print(f"    - Skipping: {stmt[:30]}... (managed by host)")
                continue
            cursor.execute(stmt)
        conn.commit()
        print(f"[+] Successfully executed {filename}")
        return True
    except Exception as err:
        print(f"[!] Error executing SQL: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print("=" * 60)
    print("  SentixAI Database Initialization")
    print("=" * 60)
    
    # 1. Setup tables
    schema_path = os.path.join(os.path.dirname(__file__), 'database', 'setup.sql')
    seed_path = os.path.join(os.path.dirname(__file__), 'database', 'seed_data.sql')

    print("\n1. Creating database tables...")
    run_sql_script(schema_path)

    print("\n2. Seeding administrator and demonstration data...")
    run_sql_script(seed_path)

    print("\n" + "=" * 60)
    print("  Database setup complete! You are ready to log in:")
    print("  - Admin Username: admin")
    print("  - Admin Password: admin123")
    print("  - User Username:  nirbhay")
    print("=" * 60)
