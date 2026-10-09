"""
wsgi.py — PythonAnywhere WSGI Entry Point for SentixAI
Username: ck2837
Site URL: https://ck2837.pythonanywhere.com

INSTRUCTIONS:
1. On PythonAnywhere, go to Web tab → click the WSGI configuration file link
2. Delete everything in that file
3. Paste the contents of THIS file
4. Replace 'YOUR_MYSQL_PASSWORD' with the MySQL password you set in the Databases tab
"""

import sys
import os

# ─────────────────────────────────────────────────────────────────
# 1. Add project folder to Python path
# ─────────────────────────────────────────────────────────────────
project_home = '/home/ck2837/sentiment-analysis-project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ─────────────────────────────────────────────────────────────────
# 2. Production environment variables
#    ONLY change: YOUR_MYSQL_PASSWORD  ← the password you set on PythonAnywhere
# ─────────────────────────────────────────────────────────────────
os.environ['DB_HOST'] = 'ck2837.mysql.pythonanywhere-services.com'
os.environ['DB_USER'] = 'ck2837'
os.environ['DB_PASSWORD'] = 'YOUR_MYSQL_PASSWORD'   # ← CHANGE THIS ONE VALUE
os.environ['DB_NAME'] = 'ck2837$sentiment_analysis'
os.environ['SECRET_KEY'] = 'sentixai-production-key-2026-xK9mP3qR7vL2'
os.environ['FLASK_DEBUG'] = 'False'

# ─────────────────────────────────────────────────────────────────
# 3. Import the Flask app
# ─────────────────────────────────────────────────────────────────
from app import app as application  # noqa
