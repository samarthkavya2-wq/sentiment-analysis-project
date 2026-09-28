"""
report_builder/ch6_development.py
Chapter 6: Application Development for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption,
    add_figure_with_caption, add_code_block
)

def build_chapter_6(doc):
    add_chapter_title(doc, "6", "Application Development", is_first=False)

    add_section_h1(doc, "6.1", "Front-End Implementation & Design System")
    add_body_p(doc, "The front-end presentation layer of SentixAI was developed using standards-compliant HTML5, custom CSS3, and vanilla JavaScript ES6. The visual design system prioritizes legibility, cognitive hierarchy, and responsive adaptation across viewport dimensions without relying on heavy third-party CSS frameworks.")
    add_body_p(doc, "The visual styling encapsulated in 'static/css/style.css' uses CSS Custom Properties defining a modern, professional dark palette: primary background (#0b1329 to #101d42 gradient), surface card containers (#16224f with subtle box shadows and glassmorphism borders), semantic accent colors (Positive Emerald: #10b981, Neutral Slate: #64748b, Negative Crimson: #ef4444), and typography loaded via Google Fonts ('Plus Jakarta Sans' for structural UI and 'Space Grotesk' for technical data badges).")

    add_section_h1(doc, "6.2", "Backend Implementation")
    add_body_p(doc, "The backend application layer is structured across three core Python modules:")
    add_bullet_item(doc, "The central web application controller orchestrating routes, handling HTTP GET and POST verbs, enforcing session authorization, and rendering Jinja2 templates.", "app.py (Controller): ")
    add_bullet_item(doc, "The analytical computation engine housing the clean_text() regular expression pipeline and the analyze_sentiment() scoring algorithm.", "sentiment.py (NLP Engine): ")
    add_bullet_item(doc, "The environment-aware MySQL database connection manager supporting both local .env parameters and cloud production connection strings.", "database.py (Database Bridge): ")

    add_section_h1(doc, "6.3", "Database Integration")
    add_body_p(doc, "Database communication utilizes mysql-connector-python with dictionary cursors (cursor(dictionary=True)), returning query result sets as native Python dictionaries. Key query types implemented include:")
    add_bullet_item(doc, "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", "Account Insertion: ")
    add_bullet_item(doc, "SELECT * FROM users WHERE username = %s", "Credential Retrieval: ")
    add_bullet_item(doc, "INSERT INTO posts (user_id, text_content, sentiment, polarity, subjectivity, confidence) VALUES (%s, %s, %s, %s, %s, %s)", "Sentiment Ingestion: ")
    add_bullet_item(doc, "SELECT sentiment, COUNT(*) as count FROM posts WHERE user_id = %s GROUP BY sentiment", "Dashboard Grouped Aggregation: ")
    add_bullet_item(doc, "SELECT u.*, COUNT(p.id) as post_count FROM users u LEFT JOIN posts p ON u.id = p.user_id GROUP BY u.id", "Admin Relational Join: ")
    add_bullet_item(doc, "DELETE FROM posts WHERE id = %s AND user_id = %s", "Scoped User Deletion: ")

    add_section_h1(doc, "6.4", "Input Validation & Error Handling")
    add_body_p(doc, "To protect system stability and provide immediate feedback, multi-tiered input validation is enforced:")
    add_bullet_item(doc, "HTML5 attributes (required, minlength='3', type='email') validate inputs before submission. JavaScript intercepts empty textarea submissions, displays immediate alert dialogs, and manages live character counts.", "Client-Side Validation: ")
    add_bullet_item(doc, "The Flask controller checks for empty or whitespace-only inputs, field length violations, and duplicate username/email collisions, providing user-friendly feedback via Flask flash notifications.", "Server-Side Validation: ")
    add_bullet_item(doc, "All database interactions are wrapped in try-except-finally blocks, ensuring cursor and connection objects are deterministically closed even upon query errors.", "Database Resilience: ")

    add_section_h1(doc, "6.5", "Module-Wise Implementation Breakdown")
    add_section_h2(doc, "6.5.1", "Text Preprocessing Module (clean_text)")
    add_body_p(doc, "Social media commentary contains significant lexical noise that introduces bias into NLP pattern analyzers. The clean_text() function executes four sequential regex operations:")

    reg_headers = ["Preprocessing Step", "Regex Expression Applied", "Input Sample", "Transformed Output"]
    reg_rows = [
        ["1. Remove Hyperlinks", "re.sub(r'http\\S+|www\\S+', '', text)", "New bill passed https://news.com/392 #Gov", "New bill passed  #Gov"],
        ["2. Strip @Mentions", "re.sub(r'@\\w+', '', text)", "PM @narendramodi announces welfare", "PM  announces welfare"],
        ["3. Strip #Hashtags", "re.sub(r'#\\w+', '', text)", "Economy is growing #GDP #Growth", "Economy is growing  "],
        ["4. Whitespace Clean", "re.sub(r'\\s+', ' ', text).strip()", "   Multiple   spaces   in text   ", "Multiple spaces in text"]
    ]
    add_table_with_caption(doc, "Table 6.1 — Text Preprocessing Regex Cleaning Transformations", reg_headers, reg_rows, [1.5, 2.1, 1.5, 1.4])

    add_section_h2(doc, "6.5.2", "Demonstration Accounts Seeded in the Database")
    add_body_p(doc, "To enable immediate evaluation by academic reviewers, the production database is seeded with verified user accounts and historical analyses matching the project architecture documentation:")

    seed_headers = ["User ID", "Username", "Email Address", "Role Authority", "Seeded Posts Count"]
    seed_rows = [
        ["#7", "admin", "admin@sentix.ai", "Administrator (is_admin = 1)", "0 (System Moderator)"],
        ["#4", "nirbhay", "nirbhayshinde@gmail.com", "Standard User (is_admin = 0)", "9 Analyzed Political Posts"],
        ["#1", "KAVYA", "samarthkavya2@gmail.com", "Standard User (is_admin = 0)", "0 (Developer Account)"],
        ["#2", "krish", "krishshinde@gmail.com", "Standard User (is_admin = 0)", "0 (Test Account)"],
        ["#3", "kavya", "kavya@gmail.com", "Standard User (is_admin = 0)", "0 (Test Account)"]
    ]
    add_table_with_caption(doc, "Table 6.2 — Academic Demonstration Accounts Seeded in Database", seed_headers, seed_rows, [0.8, 1.1, 2.0, 1.5, 1.1])

    add_section_h1(doc, "6.6", "Visual Representations of Actual Application Interfaces")
    add_body_p(doc, "Below are structural wireframe representations of all seven user interfaces, derived directly from the working application:")

    # Figure 6.1: Home
    home_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]             # Home    ->) Login    [* Get Started Free]              |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ Natural Language Processing x MySQL ]                                          |\n"
        "|  Filtering & Classifying Political Sentiment in Social Media                     |\n"
        "|                                                                                   |\n"
        "|  An intelligent academic analytics platform designed to extract public opinion   |\n"
        "|  polarity, subjectivity metrics, and sentiment distribution across discourse.     |\n"
        "|                                                                                   |\n"
        "|  [ * Get Started Free ]       [ ->) Sign In ]                                     |\n"
        "|                                                                                   |\n"
        "|  [ 3-Class Pos/Neg/Neu ]      [ Real-Time NLP Scoring ]     [ Relational MySQL ]  |\n"
        "|                                                                                   |\n"
        "|  SYSTEM WORKFLOW: How Political Sentiment is Filtered                            |\n"
        "|  +-------------+     +---------------+     +---------------+     +--------------+ |\n"
        "|  | 01. Ingest  | --> | 02. Preprocess| --> | 03. NLP Score | --> | 04. Archive  | |\n"
        "|  | Paste text  |     | Regex clean   |     | TextBlob calc |     | MySQL store  | |\n"
        "|  +-------------+     +---------------+     +---------------+     +--------------+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.1 — User Interface Wireframe: Public Landing Page (index.html)", home_ascii)

    # Figure 6.2: Login
    login_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]                                         # Home    ->) Login          |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|                            +-----------------------------------+                  |\n"
        "|                            | [L] Welcome Back                  |                  |\n"
        "|                            | Access your sentiment analytics   |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | @ Account Username                |                  |\n"
        "|                            | [ admin                         ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | K Security Password               |                  |\n"
        "|                            | [ *********                     ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | [ Sign In to Dashboard ->       ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | New to SentixAI?                  |                  |\n"
        "|                            | [ & Create Academic Account     ] |                  |\n"
        "|                            +-----------------------------------+                  |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.2 — User Interface Wireframe: User Login Page (login.html)", login_ascii)

    # Figure 6.3: Register
    reg_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]                                         # Home    ->) Login          |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|                            +-----------------------------------+                  |\n"
        "|                            | [&] Create Academic Account       |                  |\n"
        "|                            | Join SentixAI Analytics Platform  |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | @ Preferred Username              |                  |\n"
        "|                            | [ Choose a distinct username    ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | @ Email Address                   |                  |\n"
        "|                            | [ name@university.edu           ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | K Security Password               |                  |\n"
        "|                            | [ Create password (min 4 ch.)   ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | [ Complete Registration ->      ] |                  |\n"
        "|                            |                                   |                  |\n"
        "|                            | Already registered?               |                  |\n"
        "|                            | [ ->) Sign In to Existing Acc.  ] |                  |\n"
        "|                            +-----------------------------------+                  |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.3 — User Interface Wireframe: Registration Page (register.html)", reg_ascii)

    # Figure 6.4: Analyze Input
    analyze_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]  # Home  % Dashboard  / Analyze  = History      @ nirbhay  [-> Logout|\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ NLP SENTIMENT ENGINE ]                                                         |\n"
        "|  Text Sentiment Classification                                                    |\n"
        "|  Submit political statements or social commentary to inspect polarity metrics.    |\n"
        "|                                                                                   |\n"
        "|  +------------------------------------------------------------------------------+ |\n"
        "|  | / Input Discourse Content                         Cleaned via regex pipeline | |\n"
        "|  | +--------------------------------------------------------------------------+ | |\n"
        "|  | | PM @narendramodi Ji with the ultimate \"Angry Phuphaji\" reference          | | |\n"
        "|  | +--------------------------------------------------------------------------+ | |\n"
        "|  | 66 characters                                                                | |\n"
        "|  | [ ? Analyze & Record Entry ]           [ ~ Clear ]                           | |\n"
        "|  +------------------------------------------------------------------------------+ |\n"
        "|                                                                                   |\n"
        "|  [!] Quick Demonstration Datasets (Click card to load):                           |\n"
        "|  +-----------------------+ +-----------------------+ +--------------------------+ |\n"
        "|  | ^ Positive Polarity   | | v Negative Polarity   | | = Neutral Polarity       | |\n"
        "|  | \"The newly announced  | | \"The state admin has  | | \"The legislative assembly| |\n"
        "|  |  welfare policy...\"   | |  utterly failed...\"   | |  convened at 10 AM...\"   | |\n"
        "|  +-----------------------+ +-----------------------+ +--------------------------+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.4 — User Interface Wireframe: Text Sentiment Classification (analyze.html)", analyze_ascii)

    # Figure 6.5: Diagnostic Results
    diag_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ COMPUTED INFERENCE ]                                                           |\n"
        "|  Sentiment Diagnostics                                          (= Neutral Badge) |\n"
        "|                                                                                   |\n"
        "|  +---------------------+   +---------------------+   +--------------------------+ |\n"
        "|  | ^ POSITIVE STANCE   |   | = NEUTRAL STANCE    |   | v NEGATIVE STANCE        | |\n"
        "|  | 12%                 |   | 50%                 |   | 38%                      | |\n"
        "|  | [===               ]|   | [==========         ]|   | [=======                 ]| |\n"
        "|  | Supportive tone     |   | Balanced/Factual    |   | Critical/Unfavorable     | |\n"
        "|  +---------------------+   +---------------------+   +--------------------------+ |\n"
        "|                                                                                   |\n"
        "|  +-------------------------------------+   +------------------------------------+ |\n"
        "|  | Original Raw Input Text             | ->| Sanitized Text (NLP Parsed)        | |\n"
        "|  | PM @narendramodi Ji with the        |   | PM Ji with the                     | |\n"
        "|  | ultimate \"Angry Phuphaji\" reference |   | ultimate \"Angry Phuphaji\" reference| |\n"
        "|  +-------------------------------------+   +------------------------------------+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.5 — User Interface Wireframe: Diagnostic Results with 3-Way Distribution", diag_ascii)

    # Figure 6.6: Dashboard
    dash_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]  # Home  % Dashboard  / Analyze  = History      @ nirbhay  [-> Logout|\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ RELATIONAL DATABASE INSIGHTS ]                                                 |\n"
        "|  Sentiment Intelligence Dashboard: Statistical synthesis for nirbhay              |\n"
        "|                                                                                   |\n"
        "|  +--------------+    +--------------+    +--------------+    +------------------+ |\n"
        "|  | AGGREGATE    |    | POSITIVE     |    | NEGATIVE     |    | NEUTRAL          | |\n"
        "|  | INGESTED     |    | STANCE       |    | STANCE       |    | STANCE           | |\n"
        "|  | 9 Total      |    | 5 (55.6%)    |    | 1 (11.1%)    |    | 3 (33.3%)        | |\n"
        "|  +--------------+    +--------------+    +--------------+    +------------------+ |\n"
        "|                                                                                   |\n"
        "|  +--------------------------------+   +-----------------------------------------+ |\n"
        "|  | % Distribution Breakdown       |   | [T] Recent Classifications              | |\n"
        "|  |                                |   |                              View All ->| |\n"
        "|  |      [ Chart.js Doughnut ]     |   | CONTENT         SENTIMENT   CONF.   DATE| |\n"
        "|  |       Positive: 5 (55.6%)      |   | PM @narendra..  Neutral     50%    Sep11| |\n"
        "|  |       Neutral:  3 (33.3%)      |   | If Iran wants.. Neutral     50%    Sep10| |\n"
        "|  |       Negative: 1 (11.1%)      |   | If Iran wants.. Positive    25%    Sep10| |\n"
        "|  |       (*) Pos (*) Neu (*) Neg  |   | Israel PM Net.. Positive    14%    Sep10| |\n"
        "|  +--------------------------------+   +-----------------------------------------+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.6 — User Interface Wireframe: Sentiment Intelligence Dashboard (dashboard.html)", dash_ascii)

    # Figure 6.7: History & Results
    res_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]  # Home  % Dashboard  / Analyze  = History      @ nirbhay  [-> Logout|\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ MYSQL RELATIONAL ARCHIVE ]                                                     |\n"
        "|  Analysis History & Filtering: Audit previous political sentiment inferences.     |\n"
        "|                                                                                   |\n"
        "|  Filter Stance: [ All Classifications |v]   Search Keyword: [ welfare           ] |\n"
        "|  [ o Apply Filter ]                                            + New Ingestion -> |\n"
        "|                                                                                   |\n"
        "|  Found 9 record(s) matching criteria:                                             |\n"
        "|  +---+-----------------------------+-----------+----------+-------+--------+----+ |\n"
        "|  | # | TEXTUAL STATEMENT EXCERPT   | STANCE    | POLARITY | CONF. | DATE   | ACT| |\n"
        "|  +---+-----------------------------+-----------+----------+-------+--------+----+ |\n"
        "|  | 1 | PM @narendramodi Ji with... | Neutral   | -0.2500  | 50%   | Sep 11 | [x]| |\n"
        "|  | 2 | If Iran wants to fight...   | Neutral   |  0.2500  | 50%   | Sep 10 | [x]| |\n"
        "|  | 3 | If Iran wants to fight...   | Positive  |  0.2500  | 25%   | Sep 10 | [x]| |\n"
        "|  | 4 | Israel PM Netanyahu plans.. | Positive  |  0.1399  | 14%   | Sep 10 | [x]| |\n"
        "|  | 5 | The newly announced wel...  | Positive  |  0.2820  | 28%   | Sep 07 | [x]| |\n"
        "|  +---+-----------------------------+-----------+----------+-------+--------+----+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.7 — User Interface Wireframe: Analysis History & Live Filtering (results.html)", res_ascii)

    # Figure 6.8: Admin Panel
    admin_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "| [o SentixAI]  # Home  % Dashboard  / Analyze  = History  [^ Admin Panel] @ admin  |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [ ADMINISTRATOR PRIVILEGES ]                                                     |\n"
        "|  System Administration & Moderation: Oversight of users and sentiment inferences. |\n"
        "|                                                                                   |\n"
        "|  [ 5 Users Registered ]  [ 9 Total Posts ]  [ 5 (55.6%) Pos ]  [ 1 (11.1%) Neg ]  |\n"
        "|                                                                                   |\n"
        "|  Registered User Accounts (Total: 5):                                             |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "|  | UID | USERNAME | EMAIL              | ROLE     | POSTS | JOINED | ACTION     | |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "|  | #7  | admin    | admin@sentix.ai    | Admin    | 0     | Sep 10 | (Protected)| |\n"
        "|  | #4  | nirbhay  | nirbhayshinde@g... | User     | 9     | Sep 07 | [Delete x] | |\n"
        "|  | #1  | KAVYA    | samarthkavya2@g... | User     | 0     | Sep 05 | [Delete x] | |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "|                                                                                   |\n"
        "|  Global Posts Moderation Audit (Latest Entries):                                  |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "|  | PID | AUTHOR   | TEXT EXCERPT       | STANCE   | CONF. | DATE   | ACTION     | |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "|  | #9  | nirbhay  | PM @narendramod... | Neutral  | 50%   | Sep 11 | [Purge x]  | |\n"
        "|  | #8  | nirbhay  | If Iran wants t... | Neutral  | 50%   | Sep 10 | [Purge x]  | |\n"
        "|  +-----+----------+--------------------+----------+-------+--------+------------+ |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 6.8 — User Interface Wireframe: Administrator & Moderation Panel (admin.html)", admin_ascii)

    add_section_h1(doc, "6.7", "Relevant Source Code Excerpts")
    add_body_p(doc, "The following annotated source code excerpts document the core algorithmic and architectural modules of the application:")

    # Code Excerpt 1: sentiment.py
    code_sentiment = (
        "# sentiment.py — Natural Language Processing & Sentiment Scoring Engine\n"
        "from textblob import TextBlob\n"
        "import re\n\n"
        "def clean_text(text):\n"
        "    \"\"\"Sanitizes raw social media text using regular expressions.\"\"\"\n"
        "    text = re.sub(r'http\\S+|www\\S+', '', text)   # 1. Remove URLs\n"
        "    text = re.sub(r'@\\w+', '', text)              # 2. Remove @mentions\n"
        "    text = re.sub(r'#\\w+', '', text)              # 3. Remove #hashtags\n"
        "    text = re.sub(r'\\s+', ' ', text).strip()      # 4. Normalize spaces\n"
        "    return text\n\n"
        "def analyze_sentiment(text):\n"
        "    \"\"\"Extracts polarity and calculates fine-grained 3-way distribution.\"\"\"\n"
        "    cleaned_text = clean_text(text)\n"
        "    blob = TextBlob(cleaned_text)\n"
        "    polarity = blob.sentiment.polarity          # Range: -1.0 to +1.0\n"
        "    subjectivity = blob.sentiment.subjectivity  # Range: 0.0 to 1.0\n\n"
        "    if polarity > 0:\n"
        "        raw_pos = 0.20 + (polarity * 0.70)\n"
        "        raw_neg = max(0.05, 0.15 - (polarity * 0.12))\n"
        "        raw_neu = max(0.10, 1.0 - (raw_pos + raw_neg))\n"
        "    elif polarity < 0:\n"
        "        raw_neg = 0.20 + (abs(polarity) * 0.70)\n"
        "        raw_pos = max(0.05, 0.15 - (abs(polarity) * 0.12))\n"
        "        raw_neu = max(0.10, 1.0 - (raw_neg + raw_pos))\n"
        "    else:\n"
        "        raw_pos, raw_neg, raw_neu = 0.10, 0.10, 0.80\n\n"
        "    total_weight = raw_pos + raw_neu + raw_neg\n"
        "    pos_pct = round((raw_pos / total_weight) * 100)\n"
        "    neg_pct = round((raw_neg / total_weight) * 100)\n"
        "    neu_pct = 100 - (pos_pct + neg_pct)  # Guarantees sum equals 100%\n\n"
        "    # Dominant sentiment classification\n"
        "    if pos_pct > neu_pct and pos_pct > neg_pct:\n"
        "        sentiment = 'Positive'\n"
        "    elif neg_pct > neu_pct and neg_pct > pos_pct:\n"
        "        sentiment = 'Negative'\n"
        "    else:\n"
        "        sentiment = 'Neutral'\n\n"
        "    return {\n"
        "        'original_text': text, 'cleaned_text': cleaned_text,\n"
        "        'sentiment': sentiment, 'polarity': round(polarity, 4),\n"
        "        'subjectivity': round(subjectivity, 4), 'confidence': max(pos_pct, neu_pct, neg_pct),\n"
        "        'pos_pct': pos_pct, 'neu_pct': neu_pct, 'neg_pct': neg_pct\n"
        "    }"
    )
    add_code_block(doc, code_sentiment, "Source Code 6.1 — sentiment.py (Text Cleaning & Sentiment Classification Algorithm)")

    # Code Excerpt 2: database.py
    code_database = (
        "# database.py — Environment-Aware MySQL Connection Module\n"
        "import os\n"
        "import urllib.parse\n"
        "import mysql.connector\n"
        "from dotenv import load_dotenv\n"
        "load_dotenv()\n\n"
        "def get_db_connection():\n"
        "    \"\"\"Establishes connection to MySQL supporting both URL and environment vars.\"\"\"\n"
        "    db_url = os.environ.get('DATABASE_URL')\n"
        "    if db_url:\n"
        "        parsed = urllib.parse.urlparse(db_url)\n"
        "        conn_config = {\n"
        "            'host': parsed.hostname or 'localhost',\n"
        "            'port': parsed.port or 3306,\n"
        "            'user': parsed.username or 'root',\n"
        "            'password': urllib.parse.unquote(parsed.password or ''),\n"
        "            'database': parsed.path.lstrip('/') or 'sentiment_analysis'\n"
        "        }\n"
        "    else:\n"
        "        conn_config = {\n"
        "            'host': os.environ.get('DB_HOST', 'localhost'),\n"
        "            'port': int(os.environ.get('DB_PORT', 3306)),\n"
        "            'user': os.environ.get('DB_USER', 'root'),\n"
        "            'password': os.environ.get('DB_PASSWORD', 'applet'),\n"
        "            'database': os.environ.get('DB_NAME', 'sentiment_analysis')\n"
        "        }\n"
        "    conn_config['connection_timeout'] = int(os.environ.get('DB_TIMEOUT', 10))\n"
        "    return mysql.connector.connect(**conn_config)"
    )
    add_code_block(doc, code_database, "Source Code 6.2 — database.py (Universal Database Connector)")

    print("[+] Chapter 6 constructed.")
