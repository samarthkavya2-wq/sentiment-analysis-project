"""
report_builder/ch5_architecture.py
Chapter 5: Architecture Design for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption,
    add_figure_with_caption, add_code_block
)

def build_chapter_5(doc):
    add_chapter_title(doc, "5", "Architecture Design", is_first=False)

    add_section_h1(doc, "5.1", "Three-Tier Architecture Overview")
    add_body_p(doc, "SentixAI is architected upon a strictly decoupled Three-Tier (Three-Layer) architectural paradigm. The Three-Tier model enforces an absolute separation of concerns between user interaction, computational business logic, and persistent relational storage, ensuring high maintainability, code modularity, and operational security:")

    tier_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                 THREE-TIER APPLICATION ARCHITECTURE DECOMPOSITION                 |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  1. PRESENTATION TIER (Front-End Layer)\n"
        "     +-----------------------------------------------------------------------------+\n"
        "     |  HTML5 Jinja2 Templates (base.html, index.html, analyze.html, etc.)          |\n"
        "     |  Custom CSS3 Styling (style.css — variables, dark theme, responsive grid)   |\n"
        "     |  Vanilla JavaScript (script.js — form validation, live character counter)   |\n"
        "     |  Chart.js Canvas Component (dynamic sentiment distribution doughnut chart)  |\n"
        "     +-----------------------------------------------------------------------------+\n"
        "                                           ^   |\n"
        "                               HTTP Pages  |   | HTTP GET / POST Requests\n"
        "                                           |   v\n"
        "  2. APPLICATION TIER (Business Logic & NLP Layer)\n"
        "     +-----------------------------------------------------------------------------+\n"
        "     |  app.py: Flask Web Framework Controller, Route Handlers, Session State      |\n"
        "     |  sentiment.py: Text Preprocessing Regex Engine, TextBlob NLP Classifier     |\n"
        "     |  3-Way Proportional Distribution Engine (pos_pct, neu_pct, neg_pct)        |\n"
        "     |  database.py: MySQL Connection Bridge & Environment-Aware Configuration     |\n"
        "     |  Security: Werkzeug Cryptographic PBKDF2 Password Hashing                   |\n"
        "     +-----------------------------------------------------------------------------+\n"
        "                                           ^   |\n"
        "                              Result Sets  |   | Parameterized SQL (%s)\n"
        "                                           |   v\n"
        "  3. DATA TIER (Relational Database Layer)\n"
        "     +-----------------------------------------------------------------------------+\n"
        "     |  MySQL 8.0 Relational Database Engine ('sentiment_analysis')               |\n"
        "     |  Table 1: 'users' (User authentication records, roles, registration dates)  |\n"
        "     |  Table 2: 'posts' (Analyzed political statements, polarity, confidence)    |\n"
        "     |  Integrity: 1:M Referential Foreign Key Constraints with ON DELETE CASCADE  |\n"
        "     +-----------------------------------------------------------------------------+\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 5.1 — Three-Tier Architectural Decomposition", tier_ascii)

    add_section_h1(doc, "5.2", "Front-End Architecture")
    add_body_p(doc, "The Presentation Layer operates as a Server-Side Rendered (SSR) web client driven by Flask's native Jinja2 templating engine. The architecture eschews complex, unstable client frameworks in favor of high-performance standard web technologies:")
    add_bullet_item(doc, "Base Template Inheritance: All application views inherit from 'templates/base.html', which establishes a persistent top-navigation bar, contextual user status badges, dynamic flash message rendering, and a responsive footer.", "Template Hierarchy: ")
    add_bullet_item(doc, "Modular CSS3 Architecture: Encapsulated within 'static/css/style.css' (~1,480 lines of clean custom code), the styling utilizes CSS Custom Properties (variables) defining design tokens for dark background gradients, card elevations, color-coded stance badges, and progress bar animations. Zero bulky external CSS frameworks (such as Bootstrap) are utilized.", "Design System: ")
    add_bullet_item(doc, "Client-Side Scripting: Contained within 'static/js/script.js', client-side behaviors include automatic 5-second fadeout for alert notifications, empty submission interception, and live character counting for the discourse input textarea.", "Interactivity: ")
    add_bullet_item(doc, "Dynamic Data Visualizations: The personal dashboard embeds Chart.js via CDN, dynamically instantiating an interactive HTML5 canvas doughnut chart based on aggregate sentiment counts passed directly from the Flask controller.", "Analytics Visualization: ")

    add_section_h1(doc, "5.3", "Backend Architecture")
    add_body_p(doc, "The Application Layer is anchored in Python 3 utilizing the Flask 3.0 microframework. Flask serves as the central WSGI application controller, coordinating request-response lifecycles, executing security policies, dispatching text to the sentiment engine, and managing database connections.")
    add_body_p(doc, "Every incoming HTTP request undergoes a standardized controller pipeline: (1) Route matching; (2) Session authentication validation; (3) Input sanitation; (4) Business logic or NLP execution; (5) Transactional database operation; and (6) Dynamic template rendering with contextual feedback.")

    add_section_h1(doc, "5.4", "Natural Language Processing Pipeline Design")
    add_body_p(doc, "The sentiment analysis engine encapsulated within 'sentiment.py' executes a four-stage sequential pipeline designed to clean, parse, score, and normalize textual political statements:")

    nlp_pipeline_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|              NATURAL LANGUAGE PROCESSING (NLP) PIPELINE ARCHITECTURE              |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  [ Raw Input Text ]\n"
        "          |  Example: 'PM @narendramodi Ji with the ultimate \"Angry Phuphaji\" reference'\n"
        "          v\n"
        "  +-------------------------------------------------------------------------------+\n"
        "  | STAGE 1: REGEX TEXT PREPROCESSING (clean_text)                               |\n"
        "  |  1. URL Removal: re.sub(r'http\\S+|www\\S+', '', text)                        |\n"
        "  |  2. User @Mention Removal: re.sub(r'@\\w+', '', text)                         |\n"
        "  |  3. Hashtag Removal: re.sub(r'#\\w+', '', text)                               |\n"
        "  |  4. Whitespace Normalization & Trimming: re.sub(r'\\s+', ' ', text).strip()    |\n"
        "  +-------------------------------------------------------------------------------+\n"
        "          |  Cleaned Text: 'PM Ji with the ultimate \"Angry Phuphaji\" reference'\n"
        "          v\n"
        "  +-------------------------------------------------------------------------------+\n"
        "  | STAGE 2: LEXICAL SCORING (TextBlob PatternAnalyzer)                          |\n"
        "  |  - Computes continuous Polarity: P in [-1.0, +1.0]                           |\n"
        "  |  - Computes continuous Subjectivity: S in [0.0, 1.0]                          |\n"
        "  +-------------------------------------------------------------------------------+\n"
        "          |  Extracted: Polarity = -0.2500, Subjectivity = 0.0000\n"
        "          v\n"
        "  +-------------------------------------------------------------------------------+\n"
        "  | STAGE 3: 3-WAY PROPORTIONAL DISTRIBUTION ENGINE                               |\n"
        "  |  - Computes dynamic positive, negative, and neutral weight distributions      |\n"
        "  |  - Normalizes raw weights into exact integer percentages summing to 100%       |\n"
        "  +-------------------------------------------------------------------------------+\n"
        "          |  Computed: pos_pct = 12%, neu_pct = 50%, neg_pct = 38% (Sum = 100%)\n"
        "          v\n"
        "  +-------------------------------------------------------------------------------+\n"
        "  | STAGE 4: DOMINANT CLASSIFICATION & CONFIDENCE SCORING                         |\n"
        "  |  - Classification Rule: Highest percentage wins                              |\n"
        "  |  - Result: Dominant Stance = 'Neutral', Confidence = 50.0%                    |\n"
        "  +-------------------------------------------------------------------------------+\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 5.2 — Natural Language Processing (NLP) Pipeline Architecture", nlp_pipeline_ascii)

    add_section_h2(doc, "5.4.1", "Mathematical Formulation of the 3-Way Distribution Algorithm")
    add_body_p(doc, "Unlike elementary sentiment classifiers that reduce discourse to a coarse binary sign, SentixAI calculates fine-grained proportional weights. Given a polarity score P in [-1.0, +1.0]:")
    add_bullet_item(doc, "If P > 0 (Positive leaning): raw_pos = 0.20 + (P * 0.70); raw_neg = max(0.05, 0.15 - (P * 0.12)); raw_neu = max(0.10, 1.0 - (raw_pos + raw_neg)).")
    add_bullet_item(doc, "If P < 0 (Negative leaning): raw_neg = 0.20 + (|P| * 0.70); raw_pos = max(0.05, 0.15 - (|P| * 0.12)); raw_neu = max(0.10, 1.0 - (raw_neg + raw_pos)).")
    add_bullet_item(doc, "If P = 0 (Completely neutral): raw_pos = 0.10; raw_neg = 0.10; raw_neu = 0.80.")
    add_body_p(doc, "Let W_total = raw_pos + raw_neu + raw_neg. Normalized percentages are calculated as:")
    add_body_p(doc, "pos_pct = round((raw_pos / W_total) * 100)\nneg_pct = round((raw_neg / W_total) * 100)\nneu_pct = 100 - (pos_pct + neg_pct)")
    add_body_p(doc, "This mathematical formulation guarantees that the three proportions strictly sum to exactly 100%, eliminating rounding drift and providing a balanced diagnostic reflection of text polarity.")

    add_section_h1(doc, "5.5", "Database Architecture & Schema Specification")
    add_body_p(doc, "The persistent storage tier is implemented in MySQL 8.0. In strict accordance with the verified source of truth, the database consists of exactly two tables: 'users' and 'posts'.")

    # Table 5.1: users table
    u_headers = ["Field", "Data Type", "Key", "Null", "Default", "Description"]
    u_rows = [
        ["id", "INT", "PK", "NO", "AUTO_INCREMENT", "Primary Key: Unique auto-incrementing user identification."],
        ["username", "VARCHAR(50)", "UNI", "NO", "None", "Unique user handle (minimum 3 characters)."],
        ["email", "VARCHAR(100)", "UNI", "NO", "None", "Unique verified email address."],
        ["password", "VARCHAR(255)", "None", "NO", "None", "Cryptographically hashed password (PBKDF2 SHA-256)."],
        ["is_admin", "TINYINT(1)", "None", "NO", "0", "Role flag: 0 = Standard Researcher, 1 = Administrator."],
        ["created_at", "TIMESTAMP", "None", "NO", "CURRENT_TIMESTAMP", "Automatic account creation timestamp."]
    ]
    add_table_with_caption(doc, "Table 5.1 — MySQL Database Schema: 'users' Table Definition", u_headers, u_rows, [0.9, 1.3, 0.6, 0.6, 1.5, 1.6])

    # Table 5.2: posts table
    p_headers = ["Field", "Data Type", "Key", "Null", "Default", "Description"]
    p_rows = [
        ["id", "INT", "PK", "NO", "AUTO_INCREMENT", "Primary Key: Unique auto-incrementing post identification."],
        ["user_id", "INT", "FK", "NO", "None", "Foreign Key referencing users(id) ON DELETE CASCADE."],
        ["text_content", "TEXT", "None", "NO", "None", "Raw political statement submitted for analysis."],
        ["sentiment", "VARCHAR(20)", "None", "NO", "None", "Classified stance: 'Positive', 'Negative', or 'Neutral'."],
        ["polarity", "FLOAT", "None", "NO", "None", "Computed continuous polarity score (-1.0 to +1.0)."],
        ["subjectivity", "FLOAT", "None", "NO", "None", "Computed subjectivity score (0.0 to 1.0)."],
        ["confidence", "FLOAT", "None", "NO", "None", "Dominant stance confidence percentage."],
        ["created_at", "TIMESTAMP", "None", "NO", "CURRENT_TIMESTAMP", "Submission date and time timestamp."]
    ]
    add_table_with_caption(doc, "Table 5.2 — MySQL Database Schema: 'posts' Table Definition", p_headers, p_rows, [0.9, 1.3, 0.6, 0.6, 1.5, 1.6])

    add_section_h1(doc, "5.6", "Flask Route & Endpoint Structure")
    add_body_p(doc, "The controller layer in 'app.py' implements exactly 11 core application routes, complemented by production health and API endpoints:")

    r_headers = ["Route URL", "HTTP Method(s)", "Controller Function", "Auth Level", "Functional Description"]
    r_rows = [
        ["/", "GET", "index()", "Public", "Renders landing page introducing workflow cards and system metrics."],
        ["/register", "GET, POST", "register()", "Public", "Handles student/researcher account creation with unique validation."],
        ["/login", "GET, POST", "login()", "Public", "Authenticates credentials, checks PBKDF2 hash, creates session."],
        ["/logout", "GET", "logout()", "User", "Clears server session dictionary and redirects to homepage."],
        ["/analyze", "GET, POST", "analyze()", "User", "Primary feature: ingests text, cleans via regex, scores, saves."],
        ["/results", "GET", "results()", "User", "Archival history table supporting stance filter and keyword search."],
        ["/dashboard", "GET", "dashboard()", "User", "Aggregates personal metrics and supplies data to Chart.js."],
        ["/delete/<id>", "POST", "delete_post(id)", "User (Scoped)", "Deletes user's own post (enforcing user_id ownership check)."],
        ["/admin", "GET", "admin_dashboard()", "Admin Only", "Global platform oversight: users list, posts audit, global KPIs."],
        ["/admin/delete-post/<id>", "POST", "admin_delete_post(id)", "Admin Only", "Administrative moderation: deletes any inappropriate post."],
        ["/admin/delete-user/<id>", "POST", "admin_delete_user(id)", "Admin Only", "Admin user management: deletes user and cascades posts."],
        ["/health", "GET", "health()", "Public", "Production probe verifying web server and database connectivity."],
        ["/api/analyze", "POST", "api_analyze()", "Public (CORS)", "REST API returning JSON sentiment classification results."]
    ]
    add_table_with_caption(doc, "Table 5.3 — Complete Flask Route and Endpoint Specification", r_headers, r_rows, [1.3, 1.1, 1.3, 1.0, 1.8])

    add_section_h1(doc, "5.7", "Security Architecture")
    add_body_p(doc, "SentixAI implements defense-in-depth security principles across the software stack:")
    add_bullet_item(doc, "Passwords are cryptographically transformed using Werkzeug's generate_password_hash function implementing the PBKDF2 algorithm with HMAC SHA-256 and salt. Plain text passwords are never stored in the database.", "Cryptographic Password Hashing: ")
    add_bullet_item(doc, "All database queries utilize parameterized SQL statements with '%s' placeholders executed through mysql-connector-python. String concatenation is strictly prohibited, neutralizing SQL injection vectors.", "SQL Injection Immunity: ")
    add_bullet_item(doc, "Sensitive credentials including database passwords and secret session keys are stored in an uncommitted '.env' file and parsed at runtime via python-dotenv.", "Environment Variable Isolation: ")
    add_bullet_item(doc, "Session cookies are hardened with HttpOnly flags and SameSite=Lax attributes to protect against cross-site scripting (XSS) session hijacking.", "Session Security: ")
    add_bullet_item(doc, "Administrative endpoints strictly inspect session['is_admin'] == True, and deletion operations enforce user_id validation to prevent cross-tenant data tampering.", "Role-Based Access Control (RBAC): ")

    print("[+] Chapter 5 constructed.")
