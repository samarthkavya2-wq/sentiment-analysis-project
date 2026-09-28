"""
report_builder/ch8_deployment.py
Chapter 8: Deployment for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption,
    add_code_block
)

def build_chapter_8(doc):
    add_chapter_title(doc, "8", "Deployment", is_first=False)

    add_section_h1(doc, "8.1", "Deployment Environment & Topology")
    add_body_p(doc, "Transitioning SentixAI from a local workstation prototype to a hardened, globally accessible cloud deployment requires a robust runtime environment capable of managing concurrent web traffic, isolated package runtimes, and persistent relational data storage. The production deployment targets PythonAnywhere—a specialized, cloud-hosted Python Platform-as-a-Service (PaaS) providing integrated Linux execution containers, managed WSGI servers, and native MySQL database infrastructure.")

    add_section_h1(doc, "8.2", "Production Configuration Hardening")
    add_body_p(doc, "Prior to public deployment, critical configuration flags were systematically modified to eliminate development-mode vulnerabilities:")
    add_bullet_item(doc, "Flask's debug mode (debug=True) was deactivated in production (debug=False). This disables the Werkzeug interactive debugger, preventing unauthorized arbitrary code execution via browser error overlays.", "Debug Deactivation: ")
    add_bullet_item(doc, "The application entry point was decoupled from the local single-threaded server. In production, requests are dispatched via WSGI interfaces (Gunicorn / uWSGI) capable of spawning worker processes.", "WSGI Entry Decoupling: ")
    add_bullet_item(doc, "Dynamic environment binding ensures that host ('0.0.0.0') and port variables (os.environ.get('PORT', 5000)) adapt automatically to host operating environments.", "Dynamic Port Binding: ")
    add_bullet_item(doc, "Cross-Origin Resource Sharing (CORS) is enabled for programmatic API endpoints (/api/*), permitting integration tests from external evaluators without browser security violations.", "CORS Production Policy: ")

    add_section_h1(doc, "8.3", "Cloud Database Schema Migration & Seeding")
    add_body_p(doc, "Database provisioning on the cloud MySQL server is automated via the 'init_db.py' utility. The script executes 'database/setup.sql' and 'database/seed_data.sql' using active environment variables:")
    add_bullet_item(doc, "Creates 'users' and 'posts' tables with proper primary keys, unique constraints, and foreign key references with ON DELETE CASCADE.", "DDL Schema Generation: ")
    add_bullet_item(doc, "Seeds the default Administrator account (username: 'admin', password: 'admin123' with PBKDF2 hash) and populates 9 academic baseline political posts submitted by user 'nirbhay'.", "Data Seeding: ")

    add_section_h1(doc, "8.4", "Virtual Environment & Dependency Isolation")
    add_body_p(doc, "To prevent library version collisions with host system packages, a dedicated Python 3.10 virtual environment ('venv') is instantiated on the cloud host. The complete list of production dependencies is documented in 'requirements.txt':")

    req_code = (
        "flask==3.0.0\n"
        "mysql-connector-python>=8.2.0\n"
        "textblob>=0.18.0\n"
        "nltk>=3.8.1\n"
        "python-dotenv>=1.0.0\n"
        "flask-cors>=4.0.0\n"
        "gunicorn>=21.2.0"
    )
    add_code_block(doc, req_code, "Configuration 8.1 — requirements.txt (Production Dependencies)")

    add_section_h1(doc, "8.5", "Step-by-Step Production Hosting on PythonAnywhere")
    add_body_p(doc, "The end-to-end production deployment on PythonAnywhere follows seven sequential phases:")
    add_bullet_item(doc, "Register a free Beginner account on PythonAnywhere (e.g. username 'kavyasamarth'). This establishes a persistent public URL: https://kavyasamarth.pythonanywhere.com.", "Phase 1: Account Creation: ")
    add_bullet_item(doc, "Navigate to the 'Databases' tab, configure the MySQL password, and create database 'kavyasamarth$sentiment_analysis'. Record the host address 'kavyasamarth.mysql.pythonanywhere-services.com'.", "Phase 2: Cloud MySQL Setup: ")
    add_bullet_item(doc, "Open a Cloud Bash Console and clone the repository: 'git clone https://github.com/samarthkavya2-wq/sentiment-analysis-project.git'.", "Phase 3: Repository Cloning: ")
    add_bullet_item(doc, "Create and activate a virtualenv ('python3.10 -m venv venv', 'source venv/bin/activate') and install dependencies ('pip install -r requirements.txt').", "Phase 4: Dependency Setup: ")
    add_bullet_item(doc, "Create the production '.env' file containing cloud database credentials and run 'python init_db.py' to initialize tables and seed data.", "Phase 5: Database Seeding: ")
    add_bullet_item(doc, "Under the 'Web' tab, create a Python 3.10 web app, configure virtualenv path ('/home/kavyasamarth/sentiment-analysis-project/venv'), and map static files ('/static/' to '/home/kavyasamarth/sentiment-analysis-project/static').", "Phase 6: Web App & Static Mapping: ")
    add_bullet_item(doc, "Edit the WSGI configuration file to load environment variables and import 'from app import app as application', then click 'Reload'.", "Phase 7: WSGI Activation: ")

    wsgi_code = (
        "# PythonAnywhere WSGI Configuration (/var/www/username_pythonanywhere_com_wsgi.py)\n"
        "import sys\n"
        "import os\n\n"
        "project_home = '/home/kavyasamarth/sentiment-analysis-project'\n"
        "if project_home not in sys.path:\n"
        "    sys.path.insert(0, project_home)\n\n"
        "from dotenv import load_dotenv\n"
        "load_dotenv(os.path.join(project_home, '.env'))\n\n"
        "from app import app as application"
    )
    add_code_block(doc, wsgi_code, "Configuration 8.2 — Production WSGI Script")

    add_section_h1(doc, "8.6", "Version Control & GitHub Repository Integration")
    add_body_p(doc, "The project is version-controlled using Git and hosted at https://github.com/samarthkavya2-wq/sentiment-analysis-project.git. The repository includes strict '.gitignore' directives protecting credentials:")
    add_bullet_item(doc, "Strictly excludes local '.env' containing MySQL passwords.", ".env Exclusion: ")
    add_bullet_item(doc, "Excludes Python bytecode ('__pycache__/', '*.pyc') and virtualenv folders ('venv/', '.venv/').", "Runtime Exclusion: ")
    add_bullet_item(doc, "Tracks '.env.example', 'Procfile', 'requirements.txt', and 'init_db.py' to enable reproducible cloud deployment.", "Deployment Manifests: ")

    add_section_h1(doc, "8.7", "Public Access & Live System Verification")
    add_body_p(doc, "Upon reloading the web application, the system is globally accessible via HTTPS at: https://kavyasamarth.pythonanywhere.com. The live deployment can be instantly verified using the diagnostic health probe endpoint: https://kavyasamarth.pythonanywhere.com/health.")

    print("[+] Chapter 8 constructed.")
