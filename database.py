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
    Create tables, seed demo users (with known passwords), and insert
    sample posts so the site looks populated during demos and viva.
    Called automatically when the Flask app starts.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # ── Create users table ────────────────────────────────────────
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

    # ── Create posts table ────────────────────────────────────────
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

    # ── Seed demo users ───────────────────────────────────────────
    # All passwords are hashed with werkzeug scrypt.
    # Plain-text passwords are shown in comments for reference.
    demo_users = [
        # (id, username, email, hashed_password, is_admin)
        (1, 'KAVYA',   'samarthkavya2@gmail.com',
         'scrypt:32768:8:1$dpadtWasz8t4PU9t$a046ca8bd09440d2efec9fc4e6b11b7f278965fdec446f31c5ef6be72159c6138588e0982bf8f3fc515015a03e2b37bd8e246f7f6371aa0d73b93716dc750e13',
         0),   # password: kavya123

        (2, 'krish',   'krishshinde@gmail.com',
         'scrypt:32768:8:1$agucB1F5pxEccdpx$5c6152bdc922f2676eec8eaeb54a4b8ae8d32fffc0dadba1c5d94951966c82fec5704a0b17511a5c4c18d30c5094349c985181718e2a0547467e3c1343432104',
         0),   # password: krish123

        (3, 'kavya',   'kavya@gmail.com',
         'scrypt:32768:8:1$igevq01aVmFhAwqd$6632b653456ed1aeaf91d3b452acac827a4ce87a7da97139070b2db0c76c5f1e28ff40b00b30fc68995eab60a3c3bdcec8952ae4b6b8a218c79032886b3d931b',
         0),   # password: kavya123

        (4, 'nirbhay', 'nirbhayshinde@gmail.com',
         'scrypt:32768:8:1$JVoIfkKDEcja7xPX$e8012de9205d3bdbbdf5c44593fa35df1438f10310c23bfbc98a68774f808ff8e0d9f7cd184a340942050627a038a481e1df9587d71913c0f1dc623b5e669fa4',
         0),   # password: nirbhay123

        (7, 'admin',   'admin@sentix.ai',
         'scrypt:32768:8:1$DwkOn76BkPQcWDYT$fa3dd32db66a23a5604e72b09938f215d42edcbd28def9dc739c9062d41589d18ec38976e501c8ad025e1a4d28cee7c10b96da323c9c7c138f963c9d0cdd2ed4',
         1),   # password: admin123
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO users (id, username, email, password, is_admin)
        VALUES (?, ?, ?, ?, ?)
    ''', demo_users)

    # ── Seed sample posts (analyzed by nirbhay, user_id=4) ────────
    sample_posts = [
        (1, 4, 'The newly announced economic welfare initiative is exceptional. Thousands of low-income families will receive direct support and healthcare subsidies. A truly transformative policy!',
         'Positive', 0.282, 0.5136, 28.2, '2026-09-07 13:18:52'),

        (2, 4, 'The legislative assembly convened at 10 AM to discuss proposed amendments to the trade bill. Delegates from multiple parties submitted written remarks.',
         'Neutral', 0.0, 0.0, 50.0, '2026-09-07 13:19:05'),

        (3, 4, 'The state administration has utterly failed to regulate price spikes on essentials. Rampant inflation and broken campaign pledges have severely harmed citizens.',
         'Negative', -0.45, 0.35, 45.0, '2026-09-07 13:19:14'),

        (4, 4, 'PM Modi announced a ₹10,000 crore infrastructure push for rural connectivity. Opposition parties have called for a detailed audit of fund allocation.',
         'Neutral', 0.05, 0.2, 50.0, '2026-09-08 10:00:00'),

        (5, 4, 'Historic peace agreement signed between two neighbouring nations after decades of conflict. Global leaders applaud the diplomatic breakthrough.',
         'Positive', 0.55, 0.6, 55.0, '2026-09-09 14:30:00'),

        (6, 4, 'Israel PM Netanyahu plans quick 24-hour trip to New York as Mayor Zohran Mamdani calls for his arrest.',
         'Positive', 0.1399, 0.3182, 13.99, '2026-09-10 01:15:30'),

        (7, 4, 'If Iran wants to fight, that will be the official end of Iran. Never threaten the United States again!',
         'Positive', 0.25, 0.1, 25.0, '2026-09-10 01:47:16'),

        (8, 4, 'Government announces free health insurance for all citizens below poverty line. Critics question funding sustainability.',
         'Neutral', 0.1, 0.4, 50.0, '2026-09-11 09:00:00'),

        (9, 4, 'Massive corruption scandal rocks the ruling party. Several ministers implicated; public demands immediate resignation and independent inquiry.',
         'Negative', -0.6, 0.7, 60.0, '2026-09-12 11:20:00'),
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO posts
            (id, user_id, text_content, sentiment, polarity, subjectivity, confidence, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_posts)

    conn.commit()
    conn.close()
    print(f"[DATABASE] SQLite database ready at: {DB_PATH}")
    print("[DATABASE] Demo users and sample posts seeded.")
