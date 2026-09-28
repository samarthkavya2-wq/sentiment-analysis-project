"""
build_deployment_guide_doc.py
Generates a complete, professionally formatted Microsoft Word (.docx)
deployment document for the SentixAI Political Sentiment Analysis System.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="D1D5DB", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def set_callout_border(cell, color="1B365D", sz="24"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def create_document():
    doc = docx.Document()

    # Page Margins: 1 inch all around
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Set base font
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    # -------------------------------------------------------------
    # COVER / HEADER TITLE BLOCK
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    run_title = title_p.add_run("COMPLETE PRODUCTION DEPLOYMENT GUIDE")
    run_title.bold = True
    run_title.font.size = Pt(22)
    run_title.font.color.rgb = RGBColor(0x0F, 0x2C, 0x59)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(12)
    run_sub = sub_p.add_run("Filtering Political Sentiment in Social Media from Textual Information Using MySQL")
    run_sub.font.size = Pt(14)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0x2B, 0x4C, 0x7E)

    # Metadata Card
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_info = [
        ("Project System Name:", "SentixAI — Political Sentiment Analysis Platform"),
        ("Student / Developer:", "Kavya Samarth (Roll No: 9122)"),
        ("Academic Program:", "T.Y.B.Sc (Computer Science) — Project Submission & Viva"),
        ("GitHub Repository:", "https://github.com/samarthkavya2-wq/sentiment-analysis-project.git")
    ]

    for i, (label, val) in enumerate(meta_info):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_background(c0, "F0F4F8")
        set_cell_background(c1, "F8FAFC")
        set_cell_margins(c0, 80, 80, 120, 120)
        set_cell_margins(c1, 80, 80, 120, 120)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    set_table_borders(meta_table, "CBD5E1", "6")

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(8)
    p_spacer.paragraph_format.space_after = Pt(8)

    # Helper function for headings
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x0F, 0x2C, 0x59)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(12.5)
        run.font.color.rgb = RGBColor(0x2B, 0x4C, 0x7E)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x0E, 0x83, 0x88)
        return p

    def add_para(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.bold = True
            r_bold.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        p.add_run(text)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.bold = True
            r_bold.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        p.add_run(text)
        return p

    def add_code(code_str):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.rows[0].cells[0]
        cell.width = Inches(6.5)
        set_cell_background(cell, "F4F6F8")
        set_callout_border(cell, "1B365D", "24")
        set_cell_margins(cell, 100, 100, 140, 140)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(code_str)
        run.font.name = 'Consolas'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)

        spacer = doc.add_paragraph()
        spacer.paragraph_format.space_before = Pt(4)
        spacer.paragraph_format.space_after = Pt(4)

    def add_note_box(title, text, box_type='note'):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.rows[0].cells[0]
        cell.width = Inches(6.5)

        bg = "EBF3FB" if box_type == 'note' else "FEF9E7"
        border_col = "1B365D" if box_type == 'note' else "D97706"

        set_cell_background(cell, bg)
        set_callout_border(cell, border_col, "24")
        set_cell_margins(cell, 100, 100, 140, 140)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        r_title = p.add_run(f"[{title.upper()}] ")
        r_title.bold = True
        r_title.font.size = Pt(10)
        r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) if box_type == 'note' else RGBColor(0x92, 0x40, 0x0E)

        r_text = p.add_run(text)
        r_text.font.size = Pt(9.5)
        r_text.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

        spacer = doc.add_paragraph()
        spacer.paragraph_format.space_before = Pt(4)
        spacer.paragraph_format.space_after = Pt(4)

    def add_table_data(headers, rows_data, widths=None):
        tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        # Header Row
        hdr_row = tbl.rows[0]
        hdr_row._tr.get_or_add_trPr().append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        for j, h in enumerate(headers):
            c = hdr_row.cells[j]
            if widths and j < len(widths):
                c.width = Inches(widths[j])
            set_cell_background(c, "1B365D")
            set_cell_margins(c, 100, 100, 120, 120)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(h)
            run.bold = True
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Data Rows
        for i, row in enumerate(rows_data):
            r = tbl.rows[i + 1]
            bg_col = "F8FAFC" if i % 2 == 1 else "FFFFFF"
            for j, val in enumerate(row):
                c = r.cells[j]
                if widths and j < len(widths):
                    c.width = Inches(widths[j])
                set_cell_background(c, bg_col)
                set_cell_margins(c, 80, 80, 100, 100)
                p = c.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                run = p.add_run(str(val))
                run.font.size = Pt(9.0)
                run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

        set_table_borders(tbl, "CBD5E1", "6")
        spacer = doc.add_paragraph()
        spacer.paragraph_format.space_before = Pt(4)
        spacer.paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 1: EXECUTIVE SUMMARY & SYSTEM OVERVIEW
    # -------------------------------------------------------------
    add_h1("1. Executive Summary & Project Identification")
    add_para("The SentixAI Political Sentiment Analysis System is an academic, full-stack web application engineered to ingest unstructured social media discourse (e.g., political posts, tweets, and legislative commentary), sanitize textual artifacts using automated regular expression pipelines, compute mathematical sentiment polarity scores using Natural Language Processing (NLP), and persist structured results in a relational MySQL database.")
    add_para("This guide provides the complete, authoritative documentation for transitioning the local development build into a resilient, publicly accessible production deployment suitable for academic evaluation, project viva examination, and real-world demonstration.")

    # -------------------------------------------------------------
    # SECTION 2: SYSTEM ARCHITECTURE & FILE BREAKDOWN
    # -------------------------------------------------------------
    add_h1("2. System Architecture & Project Structure")
    add_para("The system strictly implements a Three-Tier Software Architecture comprising Presentation, Application/Business Logic, and Data layers:")

    arch_headers = ["Layer", "Implementation Technologies", "Key Files", "Functional Responsibility"]
    arch_rows = [
        ["Presentation Layer (Front-End)", "HTML5, CSS3, JavaScript (Vanilla), Jinja2 Templates, Chart.js, FontAwesome", "templates/*.html\nstatic/css/style.css\nstatic/js/script.js", "Renders 7 dynamic user interfaces, interactive forms, live character counters, KPI cards, and responsive doughnut charts."],
        ["Application Layer (Business Logic)", "Python 3.10+, Flask 3.0, TextBlob NLP, NLTK, Werkzeug Security, Flask-CORS", "app.py\nsentiment.py\nrequirements.txt", "Handles 11 HTTP route endpoints, session authentication, password hashing, regex text preprocessing, polarity scoring, and 3-way distribution."],
        ["WSGI Web Server Layer", "Gunicorn 21.2 (WSGI HTTP Server)", "Procfile", "Provides multi-threaded production HTTP request handling and process management for cloud Linux environments."],
        ["Data Layer (Database)", "MySQL 8.0 / MySQL Connector Python", "database.py\ndatabase/setup.sql\ndatabase/seed_data.sql", "Stores persistent user accounts and analyzed sentiment records with foreign key integrity and cascading deletions."]
    ]
    add_table_data(arch_headers, arch_rows, [1.5, 1.6, 1.4, 2.0])

    add_h2("Complete Directory Tree")
    tree_text = (
        "sentiment-analysis-project/\n"
        "├── app.py                  # Core Flask web server & 11 route handlers\n"
        "├── database.py             # Database connection module (environment-aware)\n"
        "├── sentiment.py            # Text cleaning (regex) & TextBlob NLP engine\n"
        "├── init_db.py              # Automated 1-click cloud database setup & seeder\n"
        "├── Procfile                # WSGI process definition for cloud platforms (gunicorn)\n"
        "├── requirements.txt        # Production Python dependencies\n"
        "├── .env                    # Local secrets (host, passwords) — NEVER uploaded to Git\n"
        "├── .env.example            # Environment variables template for cloud hosting\n"
        "├── .gitignore              # Ignores .env, __pycache__, and virtualenvs\n"
        "├── database/\n"
        "│   ├── setup.sql           # Database schema & admin account creation\n"
        "│   └── seed_data.sql       # Academic demo dataset (5 users + 9 analyzed posts)\n"
        "├── static/\n"
        "│   ├── css/style.css       # Custom dark-theme styling (~1,480 lines)\n"
        "│   └── js/script.js        # Client validation & auto-dismiss flash alerts\n"
        "└── templates/\n"
        "    ├── base.html           # Master navigation layout & footer\n"
        "    ├── index.html          # Public landing page with workflow cards\n"
        "    ├── login.html          # User authentication screen\n"
        "    ├── register.html       # Student/researcher registration screen\n"
        "    ├── analyze.html        # Main sentiment inference & regex comparison\n"
        "    ├── dashboard.html      # Personal analytics with Chart.js & KPI metrics\n"
        "    ├── results.html        # Historical records with live search & stance filtering\n"
        "    └── admin.html          # Platform administrator & content moderation dashboard"
    )
    add_code(tree_text)

    # -------------------------------------------------------------
    # SECTION 3: PRODUCTION CONFIGURATION & CODE UPGRADES
    # -------------------------------------------------------------
    add_h1("3. Production Configurations Implemented")
    add_para("To transition the application from a local prototype to a hardened production service, key architectural enhancements were coded and committed to the Git repository:")

    add_bullet(" Added Gunicorn 21.2 WSGI Server: Configured a cloud Procfile ('web: gunicorn app:app'). This eliminates the single-threaded development server warning and guarantees high-concurrency request handling.", "WSGI Server: ")
    add_bullet(" Dynamic Port & Host Binding: app.py was modified to listen on host '0.0.0.0' and read the cloud-assigned environment port via 'os.environ.get(\"PORT\", 5000)'.", "Port Configuration: ")
    add_bullet(" Cross-Origin Resource Sharing (CORS): Configured 'flask-cors' across '/api/*' endpoints to enable external frontends or automated evaluation suites to connect without CORS errors.", "CORS Integration: ")
    add_bullet(" Universal Database Compatibility: database.py supports both individual variables (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT) and unified cloud connection strings (DATABASE_URL) with automated SSL negotiation and 10-second timeout handling.", "Database Engine: ")
    add_bullet(" Liveness Health Check (/health): Added an automated diagnostic endpoint returning HTTP 200 and JSON status ('healthy', 'connected') for cloud platforms and evaluators.", "Health Probe: ")
    add_bullet(" Programmatic REST API (/api/analyze): Implemented a clean JSON input/output endpoint for external automated grading or integration tests.", "REST API: ")
    add_bullet(" Automated Cloud Database Initializer (init_db.py): Created a terminal utility that reads the active environment and provisions tables and demo records in one step.", "Database Automation: ")

    # -------------------------------------------------------------
    # SECTION 4: SENSITIVE DATA & ENVIRONMENT VARIABLES
    # -------------------------------------------------------------
    add_h1("4. Managing Sensitive Information & Secrets")
    add_para("Hardcoding database credentials or secret session keys inside source code creates severe academic and enterprise security vulnerabilities. The project separates configuration from code:")

    add_h2("The Local .env File")
    add_para("Stored at C:\\Users\\Kavya\\Desktop\\sentiment-analysis-project\\.env, this file holds local credentials and is strictly excluded from version control via .gitignore:")
    add_code(
        "SECRET_KEY=sentiment_analysis_secret_key_2024\n"
        "DB_HOST=localhost\n"
        "DB_PORT=3306\n"
        "DB_USER=root\n"
        "DB_PASSWORD=applet\n"
        "DB_NAME=sentiment_analysis"
    )

    add_h2("The Production .env.example Template")
    add_para("The repository includes .env.example as a public guide for administrators setting up cloud hosting:")
    add_code(
        "# Production Environment Variables Template\n"
        "SECRET_KEY=your-random-production-secret-key\n"
        "DB_HOST=your-cloud-db-host\n"
        "DB_PORT=3306\n"
        "DB_USER=your-cloud-db-username\n"
        "DB_PASSWORD=your-cloud-db-password\n"
        "DB_NAME=sentiment_analysis\n\n"
        "# Optional unified database URL (Render / Railway)\n"
        "# DATABASE_URL=mysql://user:pass@host:port/dbname\n\n"
        "# Server configuration\n"
        "PORT=5000\n"
        "FLASK_DEBUG=0"
    )

    add_note_box("Security Notice", "Never un-ignore .env in .gitignore or commit production passwords to GitHub. Cloud hosting dashboards provide secure 'Environment Variables' input forms that inject these secrets directly into the server memory.", "warn")

    # -------------------------------------------------------------
    # SECTION 5: LOCAL TESTING & VERIFICATION
    # -------------------------------------------------------------
    add_h1("5. How to Test the Website Locally Before Deployment")
    add_para("Execute the following verification steps on your local machine to ensure all business logic, database queries, and templates are functioning perfectly:")

    add_bullet(" Open PowerShell terminal and enter the project folder:", "Step 1: ")
    add_code("cd C:\\Users\\Kavya\\Desktop\\sentiment-analysis-project")

    add_bullet(" Verify Database Integrity and Seed Test Records:", "Step 2: ")
    add_code("python init_db.py")
    add_para("Expected terminal output:")
    add_code(
        "============================================================\n"
        "  SentixAI Database Initialization\n"
        "============================================================\n"
        "1. Creating database tables...\n"
        "[+] Successfully executed setup.sql\n"
        "2. Seeding administrator and demonstration data...\n"
        "[+] Successfully executed seed_data.sql\n"
        "Database setup complete! You are ready to log in:\n"
        "  - Admin: admin / admin123\n"
        "  - User:  nirbhay"
    )

    add_bullet(" Launch Local Flask Application Server:", "Step 3: ")
    add_code("python app.py")

    add_bullet(" Inspect Live Routes in Browser:", "Step 4: ")
    add_bullet(" Healthcheck: http://localhost:5000/health (verifies DB status 'connected')")
    add_bullet(" Landing Page: http://localhost:5000/ (checks workflow presentation)")
    add_bullet(" Admin Login: http://localhost:5000/login (User: 'admin', Password: 'admin123')")
    add_bullet(" Sentiment Analysis: http://localhost:5000/analyze (run sample inputs)")
    add_bullet(" Press Ctrl + C in PowerShell to stop the server when testing is complete.")

    # -------------------------------------------------------------
    # SECTION 6: HOSTING PLATFORM RECOMMENDATIONS
    # -------------------------------------------------------------
    add_h1("6. Recommended Hosting Platforms for Academic Deployment")
    add_para("A comprehensive comparative analysis of free and low-cost deployment platforms evaluated for this project:")

    host_headers = ["Platform", "Cost", "Hosted MySQL", "Public URL Format", "Sleep / Cold Start", "Suitability Rating"]
    host_rows = [
        ["PythonAnywhere (Top Recommended)", "100% Free (No credit card)", "Free MySQL Included On-Platform", "https://username.pythonanywhere.com", "None (Always active 24/7)", "⭐⭐⭐⭐⭐ (Ideal for academic submissions & college vivas)"],
        ["Render + TiDB Cloud", "Free Tier", "External Free Cloud MySQL Required", "https://app-name.onrender.com", "Spins down after 15 min idle (50s delay)", "⭐⭐⭐⭐ (Modern Git CI/CD, but has sleep delay)"],
        ["Railway.app", "Trial Credit ($5)", "Built-in MySQL Plugin", "https://app-name.up.railway.app", "Fast, zero sleep during trial", "⭐⭐⭐ (Requires credit card or expires after trial)"],
        ["ngrok Live Tunnel", "100% Free", "Uses Localhost MySQL Directly", "https://xxxx.ngrok-free.app", "Instant live, active while PC runs", "⭐⭐⭐⭐ (Best 30-second live demonstration tool)"]
    ]
    add_table_data(host_headers, host_rows, [1.4, 1.0, 1.3, 1.4, 1.4, 1.0])

    add_note_box("Recommendation Rationale", "PythonAnywhere is the #1 choice for this project because it hosts BOTH Python Flask and MySQL on the exact same server at zero cost without requiring external database links or credit cards, and the web application never goes to sleep.", "note")

    # -------------------------------------------------------------
    # SECTION 7: STEP-BY-STEP DEPLOYMENT: PYTHONANYWHERE
    # -------------------------------------------------------------
    add_h1("7. Step-by-Step Deployment: PythonAnywhere (All-in-One)")
    add_para("Follow this exact step-by-step walkthrough to deploy the frontend, backend, and MySQL database onto PythonAnywhere:")

    add_h2("Step 7.1: Register a Free Beginner Account")
    add_bullet(" Navigate to https://www.pythonanywhere.com in your web browser.")
    add_bullet(" Click 'Pricing & signup' and choose 'Create a Beginner account'.")
    add_bullet(" Select a professional username (e.g., 'kavyasamarth'). Your live public URL will be: https://kavyasamarth.pythonanywhere.com.")

    add_h2("Step 7.2: Create the Cloud MySQL Database")
    add_bullet(" In the PythonAnywhere top menu, click on the 'Databases' tab.")
    add_bullet(" Under 'MySQL password', create a secure database password (e.g., 'SentixPass2026!') and click 'Set password'.")
    add_bullet(" Record the connection parameters displayed on the page:")
    add_bullet(" Host: username.mysql.pythonanywhere-services.com")
    add_bullet(" User: username")
    add_bullet(" Under 'Create database', enter database name: 'sentiment_analysis' and click 'Create'.")
    add_bullet(" Your complete database name is created as: username$sentiment_analysis.")

    add_h2("Step 7.3: Clone Repository in PythonAnywhere Cloud Bash")
    add_bullet(" Click on the 'Consoles' tab in the top menu.")
    add_bullet(" Under 'Start a new console', click 'Bash'. A cloud terminal will open.")
    add_bullet(" Clone your GitHub repository by entering:")
    add_code("git clone https://github.com/samarthkavya2-wq/sentiment-analysis-project.git")
    add_bullet(" Navigate into the cloned folder:")
    add_code("cd sentiment-analysis-project")

    add_h2("Step 7.4: Set Up Virtual Environment & Dependencies")
    add_bullet(" In the Bash console, create a Python 3.10 virtual environment:")
    add_code("python3.10 -m venv venv")
    add_bullet(" Activate the virtual environment:")
    add_code("source venv/bin/activate")
    add_bullet(" Install all project dependencies:")
    add_code("pip install -r requirements.txt")

    add_h2("Step 7.5: Configure Production Environment Variables")
    add_bullet(" In the Bash console, create your production .env file using nano:")
    add_code("nano .env")
    add_bullet(" Paste the following configuration (replace 'YOUR_USERNAME' and 'YOUR_PASSWORD' with your actual PythonAnywhere credentials):")
    add_code(
        "SECRET_KEY=sentix_production_key_academic_2026\n"
        "DB_HOST=YOUR_USERNAME.mysql.pythonanywhere-services.com\n"
        "DB_PORT=3306\n"
        "DB_USER=YOUR_USERNAME\n"
        "DB_PASSWORD=YOUR_PASSWORD\n"
        "DB_NAME=YOUR_USERNAME$sentiment_analysis"
    )
    add_bullet(" Press Ctrl + O then Enter to save, then Ctrl + X to exit nano.")

    add_h2("Step 7.6: Initialize Tables & Seed Demo Dataset")
    add_bullet(" In the Bash console, execute the automated database initializer:")
    add_code("python init_db.py")
    add_para("The script will connect to your cloud MySQL instance, create the 'users' and 'posts' tables, and seed the default administrator ('admin' / 'admin123') and 9 academic demonstration posts.")

    add_h2("Step 7.7: Configure Web App & WSGI Script")
    add_bullet(" In the PythonAnywhere dashboard, click on the 'Web' tab.")
    add_bullet(" Click 'Add a new web app', click 'Next', select 'Manual configuration (including virtualenv)', choose 'Python 3.10', and click 'Next'.")
    add_bullet(" Configure the following settings on the Web tab:")
    add_bullet(" Virtualenv section: click 'Enter path to a virtualenv' and enter:")
    add_code("/home/YOUR_USERNAME/sentiment-analysis-project/venv")
    add_bullet(" Code section: set 'Source code' to:")
    add_code("/home/YOUR_USERNAME/sentiment-analysis-project")
    add_bullet(" Code section: set 'Working directory' to:")
    add_code("/home/YOUR_USERNAME/sentiment-analysis-project")
    add_bullet(" Static Files section: map URL '/static/' to Directory:")
    add_code("/home/YOUR_USERNAME/sentiment-analysis-project/static")
    add_bullet(" Click on the 'WSGI configuration file' link (e.g. /var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py). Delete all existing content and paste:")
    add_code(
        "import sys\n"
        "import os\n\n"
        "project_home = '/home/YOUR_USERNAME/sentiment-analysis-project'\n"
        "if project_home not in sys.path:\n"
        "    sys.path.insert(0, project_home)\n\n"
        "from dotenv import load_dotenv\n"
        "load_dotenv(os.path.join(project_home, '.env'))\n\n"
        "from app import app as application"
    )
    add_bullet(" Click the green 'Save' button in the top right corner.")

    add_h2("Step 7.8: Reload Web Application")
    add_bullet(" Return to the 'Web' tab and click the large green button: 'Reload YOUR_USERNAME.pythonanywhere.com'.")
    add_bullet(" Visit your live website: https://YOUR_USERNAME.pythonanywhere.com.")

    # -------------------------------------------------------------
    # SECTION 8: STEP-BY-STEP DEPLOYMENT: RENDER + TIDB
    # -------------------------------------------------------------
    add_h1("8. Step-by-Step Deployment: Render + TiDB Cloud")
    add_para("For continuous deployment where every 'git push' triggers an automatic redeployment:")

    add_h2("Step 8.1: Create Free Cloud MySQL on TiDB")
    add_bullet(" Sign up at https://tidbcloud.com and create a free 'TiDB Serverless' cluster.")
    add_bullet(" Click 'Connect' → 'General' → 'MySQL CLI' and note: Host, Port (4000), User, Password.")
    add_bullet(" Open the TiDB SQL Editor and paste and run the contents of 'database/setup.sql' and 'database/seed_data.sql'.")

    add_h2("Step 8.2: Connect GitHub Repository on Render")
    add_bullet(" Visit https://render.com and sign in using your GitHub account.")
    add_bullet(" Click 'New +' → 'Web Service' and select 'samarthkavya2-wq/sentiment-analysis-project'.")
    add_bullet(" Build & Runtime Settings:")
    add_bullet(" Environment: Python 3")
    add_bullet(" Build Command: pip install -r requirements.txt")
    add_bullet(" Start Command: gunicorn app:app")
    add_bullet(" Instance Type: Free")
    add_bullet(" Under 'Environment Variables', add:")
    add_code(
        "SECRET_KEY = production_secret_key_9122\n"
        "DB_HOST    = your-tidb-host\n"
        "DB_PORT    = 4000\n"
        "DB_USER    = your-tidb-username\n"
        "DB_PASSWORD= your-tidb-password\n"
        "DB_NAME    = sentiment_analysis\n"
        "DB_SSL_MODE= REQUIRED"
    )
    add_bullet(" Click 'Create Web Service'. Render will provision the server and provide your public URL: https://sentiment-analysis-project-xxxx.onrender.com.")

    # -------------------------------------------------------------
    # SECTION 9: 30-SECOND VIVA TUNNEL: NGROK
    # -------------------------------------------------------------
    add_h1("9. Instant 30-Second Viva Live Tunnel (Ngrok)")
    add_para("If an evaluator requests an immediate live link during a viva examination without waiting for cloud DNS propagation:")
    add_bullet(" Open terminal and run local server: 'python app.py'.")
    add_bullet(" Open a second terminal and expose port 5000 to the public internet:")
    add_code("ngrok http 5000")
    add_bullet(" Ngrok will generate an instant public HTTPS link (e.g., 'https://9a2f-103-21-125-8.ngrok-free.app').")
    add_bullet(" Share this link with your evaluator. Any visitor worldwide can access your local application in real time.")

    # -------------------------------------------------------------
    # SECTION 10: FRONTEND-BACKEND INTEGRATION & REST API
    # -------------------------------------------------------------
    add_h1("10. Frontend-Backend Architecture & REST API Integration")
    add_para("The application implements a Monolithic Server-Side Rendered (SSR) pattern with an integrated REST API:")
    add_bullet(" Unified Monolith: Flask dynamically renders Jinja2 templates directly to the browser. Static CSS and JS are routed via url_for('static', filename='...'), ensuring seamless routing without CORS complexity.", "Web Interface: ")
    add_bullet(" Programmatic API Endpoint: A dedicated JSON endpoint (/api/analyze) is available for external client applications, mobile apps, or automated evaluator test harnesses.", "REST API: ")

    add_h2("REST API Request Specification")
    add_code(
        "POST /api/analyze HTTP/1.1\n"
        "Host: kavyasamarth.pythonanywhere.com\n"
        "Content-Type: application/json\n\n"
        "{\n"
        '  "text": "The government launched an ambitious welfare and education scheme."\n'
        "}"
    )

    add_h2("REST API Response Specification")
    add_code(
        "HTTP/1.1 200 OK\n"
        "Content-Type: application/json\n\n"
        "{\n"
        '  "success": true,\n'
        '  "result": {\n'
        '    "original_text": "The government launched an ambitious welfare and education scheme.",\n'
        '    "cleaned_text": "The government launched an ambitious welfare and education scheme.",\n'
        '    "sentiment": "Positive",\n'
        '    "polarity": 0.25,\n'
        '    "subjectivity": 0.1,\n'
        '    "confidence": 38,\n'
        '    "pos_pct": 38,\n'
        '    "neu_pct": 52,\n'
        '    "neg_pct": 10\n'
        "  }\n"
        "}"
    )

    # -------------------------------------------------------------
    # SECTION 11: DATABASE SCHEMA & SEED DATA SPECIFICATION
    # -------------------------------------------------------------
    add_h1("11. Production Database Schema & Seed Data Specification")
    add_para("The MySQL relational database ('sentiment_analysis') consists of two normalized tables linked by a One-to-Many (1:M) foreign key constraint with cascade deletion:")

    add_h2("Table 1: 'users' Schema")
    u_headers = ["Column", "Data Type", "Constraint", "Description"]
    u_rows = [
        ["id", "INT", "PRIMARY KEY, AUTO_INCREMENT", "Unique user identification number"],
        ["username", "VARCHAR(50)", "UNIQUE, NOT NULL", "Unique handle used for login authentication"],
        ["email", "VARCHAR(100)", "UNIQUE, NOT NULL", "User email address"],
        ["password", "VARCHAR(255)", "NOT NULL", "Scrypt-hashed password (never stored in plain text)"],
        ["is_admin", "TINYINT(1)", "DEFAULT 0", "Role flag: 0 = Standard Researcher, 1 = Administrator"],
        ["created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Automatic account creation timestamp"]
    ]
    add_table_data(u_headers, u_rows, [1.2, 1.4, 2.1, 1.8])

    add_h2("Table 2: 'posts' Schema")
    p_headers = ["Column", "Data Type", "Constraint", "Description"]
    p_rows = [
        ["id", "INT", "PRIMARY KEY, AUTO_INCREMENT", "Unique post identification number"],
        ["user_id", "INT", "FOREIGN KEY → users(id) ON DELETE CASCADE", "Links submission to authoring user account"],
        ["text_content", "TEXT", "NOT NULL", "Raw social media or political statement text"],
        ["sentiment", "VARCHAR(20)", "NOT NULL", "Computed class: 'Positive', 'Negative', or 'Neutral'"],
        ["polarity", "FLOAT", "NOT NULL", "TextBlob polarity score (-1.0 to +1.0)"],
        ["subjectivity", "FLOAT", "NOT NULL", "Opinion intensity score (0.0 factual to 1.0 opinion)"],
        ["confidence", "FLOAT", "NOT NULL", "Dominant category percentage (e.g., 50.0%)"],
        ["created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Submission timestamp"]
    ]
    add_table_data(p_headers, p_rows, [1.2, 1.4, 2.1, 1.8])

    add_h2("Demonstration Accounts Seeded in Production")
    d_headers = ["User ID", "Username", "Role", "Password", "Purpose in Evaluation"]
    d_rows = [
        ["#7", "admin", "Administrator", "admin123", "Full moderation panel, view all registered accounts, platform-wide stats."],
        ["#4", "nirbhay", "Standard User", "(Created locally)", "Associated with 9 pre-analyzed political posts in historical charts."],
        ["#1", "KAVYA", "Standard User", "(Created locally)", "Developer personal demonstration account."]
    ]
    add_table_data(d_headers, d_rows, [1.0, 1.2, 1.3, 1.2, 1.8])

    # -------------------------------------------------------------
    # SECTION 12: TROUBLESHOOTING & ERROR RESOLUTION
    # -------------------------------------------------------------
    add_h1("12. Comprehensive Troubleshooting & Error Resolution")
    add_para("Detailed diagnostic procedures for resolving common production deployment issues:")

    err_headers = ["Error Symptom", "Probable Root Cause", "Exact Resolution Procedure"]
    err_rows = [
        ["Error 2003 (HY000): Can't connect to MySQL server", "Incorrect DB_HOST or DB_PORT in .env. Note: Free PythonAnywhere accounts cannot connect to external databases, only to their local MySQL service.", "Open .env and ensure DB_HOST matches 'username.mysql.pythonanywhere-services.com' and DB_PORT is 3306."],
        ["Error 1045 (28000): Access denied for user", "Incorrect database password or username mismatch.", "Verify DB_USER is identical to your PythonAnywhere username. Reset your MySQL password under the Databases tab if necessary."],
        ["Error 1049 (42000): Unknown database", "Database not yet created on cloud service.", "In PythonAnywhere Databases tab, enter 'sentiment_analysis' and click Create. Use 'username$sentiment_analysis' in .env."],
        ["CORS Block Error (No Access-Control-Allow-Origin)", "External client attempting cross-origin API call.", "Resolved in code: flask-cors is configured across app.py for all '/api/*' routes."],
        ["HTTP 500 Internal Server Error", "Unhandled Python exception or missing library.", "On PythonAnywhere, open the Web tab and click the 'Error log' link (/var/log/username.error.log) to inspect the traceback."],
        ["Port Bind Error / Address already in use", "Server hardcoded to port 5000 on cloud environment.", "Resolved in code: app.py reads 'os.environ.get(\"PORT\", 5000)' and binds to '0.0.0.0'. Gunicorn manages ports via Procfile."],
        ["Static CSS or JS Files Return 404", "Web server not mapping static asset directory.", "In PythonAnywhere Web tab under 'Static Files', ensure URL '/static/' maps to '/home/username/sentiment-analysis-project/static'."]
    ]
    add_table_data(err_headers, err_rows, [1.6, 1.7, 3.2])

    # -------------------------------------------------------------
    # SECTION 13: POST-DEPLOYMENT VERIFICATION CHECKLIST
    # -------------------------------------------------------------
    add_h1("13. Post-Deployment Verification & Audit Checklist")
    add_para("Perform this comprehensive functional walkthrough once your public website is live:")

    checklist_items = [
        ("Production Health Probe:", "Visit /health. Ensure HTTP 200 with JSON payload showing database 'connected'."),
        ("Public Homepage:", "Visit /. Confirm hero section, metric badges, and 4 workflow explanation cards render properly."),
        ("Administrator Access:", "Log in with username 'admin' and password 'admin123'. Confirm automatic redirect to /admin."),
        ("Admin Moderation:", "Verify global statistics cards (Platform Users, Total Ingestions), registered user table, and post audit log."),
        ("User Authentication:", "Log out and sign in as 'nirbhay'. Verify personal dashboard displays KPI cards and Chart.js doughnut chart."),
        ("Text Ingestion & NLP:", "Navigate to /analyze. Click a quick dataset card or paste political text. Click 'Analyze & Record Entry'."),
        ("Inference Display:", "Confirm the 3-way distribution bars (Positive/Neutral/Negative) and original vs. regex-sanitized text comparison appear."),
        ("Search & Filter:", "Visit /results. Test stance filtering ('Positive', 'Negative', 'Neutral') and keyword search (e.g., 'welfare', 'assembly')."),
        ("New Account Creation:", "Navigate to /register. Create a new test user to verify password hashing and MySQL INSERT logic.")
    ]

    for label, desc in checklist_items:
        add_bullet(f" {desc}", f"[PASS] {label}")

    # -------------------------------------------------------------
    # SECTION 14: EVALUATOR SUBMISSION TEMPLATE
    # -------------------------------------------------------------
    add_h1("14. Academic Viva & Evaluator Submission Template")
    add_para("Copy and customize this formal project submission email when sharing the live system with your college guide, teacher, or external viva examiner:")

    submission_email = (
        "Subject: Academic Project Submission: Filtering Political Sentiment in Social Media from Textual Information\n\n"
        "Respected Guide / Project Evaluator,\n\n"
        "I have completed the development and production deployment of my semester project titled:\n"
        "'Filtering Political Sentiment in Social Media from Textual Information Using MySQL'.\n\n"
        "The web application is live, hardened for production, and publicly accessible at the following URL:\n\n"
        "  Live Public Web URL:\n"
        "  https://kavyasamarth.pythonanywhere.com\n\n"
        "  System Health & Database Probe:\n"
        "  https://kavyasamarth.pythonanywhere.com/health\n\n"
        "  GitHub Source Code Repository:\n"
        "  https://github.com/samarthkavya2-wq/sentiment-analysis-project\n\n"
        "Evaluation Credentials:\n"
        "1. Platform Administrator Account (System Oversight & Content Moderation):\n"
        "   - Username: admin\n"
        "   - Password: admin123\n"
        "   - Privileges: Global system metrics, user account management, and content moderation audit.\n\n"
        "2. Standard Researcher Account (Pre-loaded with 9 sample analyses):\n"
        "   - Username: nirbhay\n"
        "   - Privileges: Personal analytics dashboard, text ingestion, NLP inference, and history filtering.\n"
        "   (New accounts can also be created freely via the Registration portal)\n\n"
        "Technology Stack Summary:\n"
        "- Presentation Layer: HTML5, CSS3, JavaScript, Jinja2, Chart.js, FontAwesome\n"
        "- Application Layer: Python 3, Flask 3.0, TextBlob NLP, NLTK, Werkzeug, Flask-CORS\n"
        "- Web Server: Gunicorn WSGI Production Server\n"
        "- Data Layer: MySQL Relational Database (Normalized Schema with Foreign Key Cascade)\n\n"
        "Thank you,\n"
        "Kavya Samarth\n"
        "Roll Number: 9122\n"
        "T.Y.B.Sc (Computer Science)"
    )
    add_code(submission_email)

    # Save to both project folder and Desktop
    project_doc_path = r"C:\Users\Kavya\Desktop\sentiment-analysis-project\Deployment_Guide_SentixAI.docx"
    desktop_doc_path = r"C:\Users\Kavya\Desktop\Deployment_Guide_SentixAI.docx"

    doc.save(project_doc_path)
    doc.save(desktop_doc_path)

    print(f"[+] Successfully generated Word document at:")
    print(f"    1. {project_doc_path}")
    print(f"    2. {desktop_doc_path}")

if __name__ == '__main__':
    create_document()
