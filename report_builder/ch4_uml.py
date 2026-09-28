"""
report_builder/ch4_uml.py
Chapter 4: System Modeling Using UML for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_figure_with_caption
)

def build_chapter_4(doc):
    add_chapter_title(doc, "4", "System Modeling Using UML", is_first=False)

    add_section_h1(doc, "4.1", "Use Case Diagram")
    add_body_p(doc, "The Unified Modeling Language (UML) Use Case Diagram formally defines the system boundary, external human actors, and distinct functional operations facilitated by the application. SentixAI partitions actor roles into the Standard User (student, researcher, political analyst) and the System Administrator.")

    uc_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                     SENTIXAI SYSTEM BOUNDARY (WEB APPLICATION)                    |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "        STANDARD USER ACTOR                              SYSTEM ADMINISTRATOR ACTOR\n"
        "               (o)                                                   (o)           \n"
        "              / | \\                                                 / | \\          \n"
        "               / \\                                                   / \\           \n"
        "                |                                                     |            \n"
        "                +---> ( UC-01: Register Account )                     |            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-02: Authenticate & Login ) <---------------+            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-03: Ingest Political Text )                |            \n"
        "                |           |                                         |            \n"
        "                |           +--<<include>>--> ( Regex Preprocessing ) |            \n"
        "                |           |                                         |            \n"
        "                |           +--<<include>>--> ( TextBlob NLP Scoring )|            \n"
        "                |           |                                         |            \n"
        "                |           +--<<include>>--> ( 3-Way Proportional    |            \n"
        "                |                               Normalization Engine )|            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-04: View Diagnostic Inference )            |            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-05: Inspect Analytics Dashboard )          |            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-06: Browse & Filter Archives )             |            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-07: Delete Own Analysis Record )           |            \n"
        "                |                                                     |            \n"
        "                |     ( UC-08: Access Moderation Console ) <----------+            \n"
        "                |                                                     |            \n"
        "                |     ( UC-09: Manage Registered Users ) <------------+            \n"
        "                |                                                     |            \n"
        "                |     ( UC-10: Audit & Moderate Global Posts ) <------+            \n"
        "                |                                                     |            \n"
        "                +---> ( UC-11: Terminate Session / Logout ) <---------+            \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.1 — Use Case Diagram for SentixAI", uc_ascii)

    add_section_h1(doc, "4.2", "Class Diagram")
    add_body_p(doc, "The Class Diagram models the static structural design of the software, detailing the primary system classes, their internal attributes, method signatures, access visibilities, and inter-class relationships:")

    class_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                                SYSTEM CLASS DIAGRAM                               |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  +-------------------------------+         +-------------------------------------+\n"
        "  |             User              |         |                Post                 |\n"
        "  +-------------------------------+         +-------------------------------------+\n"
        "  | - id: int                     | 1     * | - id: int                           |\n"
        "  | - username: string            |---------| - user_id: int                      |\n"
        "  | - email: string               | submits | - text_content: string              |\n"
        "  | - password_hash: string       |         | - sentiment: string                 |\n"
        "  | - is_admin: boolean           |         | - polarity: float                   |\n"
        "  | - created_at: datetime        |         | - subjectivity: float               |\n"
        "  +-------------------------------+         | - confidence: float                 |\n"
        "  | + register(): boolean         |         | - created_at: datetime              |\n"
        "  | + authenticate(): boolean     |         +-------------------------------------+\n"
        "  | + get_post_history(): list    |         | + create_post(): boolean            |\n"
        "  | + delete_own_post(): boolean  |         | + delete_post(): boolean            |\n"
        "  +-------------------------------+         | + filter_by_stance(s): list         |\n"
        "                                            | + search_by_keyword(k): list        |\n"
        "                                            +-------------------------------------+\n"
        "                                                               ^                   \n"
        "                                                               | uses              \n"
        "  +-------------------------------+         +------------------+------------------+\n"
        "  |       DatabaseConnector       |         |          SentimentEngine            |\n"
        "  +-------------------------------+         +-------------------------------------+\n"
        "  | - host: string                |         | + clean_text(raw_text): string      |\n"
        "  | - port: int                   |         | + extract_polarity(txt): float      |\n"
        "  | - user: string                |         | + extract_subjectivity(txt): float  |\n"
        "  | - password: string            |         | + calculate_3way_distribution():    |\n"
        "  | - database: string            |         |     tuple(pos, neu, neg)            |\n"
        "  +-------------------------------+         | + classify_dominant_stance(): string|\n"
        "  | + get_db_connection(): conn   |         +-------------------------------------+\n"
        "  | + test_liveness(): boolean    |                                                \n"
        "  +-------------------------------+                                                \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.2 — System Class Diagram", class_ascii)

    add_section_h1(doc, "4.3", "Sequence Diagrams")
    add_body_p(doc, "Sequence diagrams capture the runtime chronological exchange of messages between the Presentation Tier, the Application Controller, the NLP Business Engine, and the MySQL Relational Data Layer.")

    add_section_h2(doc, "4.3.1", "Sequence Diagram 1: User Registration & Authentication")
    seq_auth_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|             SEQUENCE: USER REGISTRATION & AUTHENTICATION LIFECYCLE                |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  User (Browser)          Flask Controller (app.py)          MySQL Database (users) \n"
        "        |                            |                                 |            \n"
        "   1.   |--- POST /register -------->|                                 |            \n"
        "        |    (user, email, pass)     |                                 |            \n"
        "   2.   |                            |--- generate_password_hash()     |            \n"
        "        |                            |    (Werkzeug PBKDF2 SHA-256)    |            \n"
        "   3.   |                            |--- INSERT INTO users ---------->|            \n"
        "   4.   |                            |<-- Confirm Insert / Success ----|            \n"
        "   5.   |<-- Flash & Redirect /login-|                                 |            \n"
        "        |                            |                                 |            \n"
        "   6.   |--- POST /login ----------->|                                 |            \n"
        "        |    (username, password)    |--- SELECT * WHERE username = %s>|            \n"
        "   7.   |                            |<-- Return User Record + Hash ---|            \n"
        "   8.   |                            |--- check_password_hash()        |            \n"
        "        |                            |    (Verifies hash match)        |            \n"
        "   9.   |                            |--- Initialize session dictionary|            \n"
        "        |                            |    [user_id, username, is_admin]|            \n"
        "  10.   |<-- Set-Cookie & Redirect --|                                 |            \n"
        "        |    (Dashboard / Admin)     |                                 |            \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.3a — Sequence Diagram: User Registration and Authentication Flow", seq_auth_ascii)

    add_section_h2(doc, "4.3.2", "Sequence Diagram 2: Political Text Ingestion & Sentiment Analysis")
    seq_nlp_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|        SEQUENCE: POLITICAL TEXT INGESTION & SENTIMENT ANALYSIS PIPELINE           |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  User (Browser)       Flask (app.py)       sentiment.py (NLP)       MySQL (posts)  \n"
        "        |                    |                      |                      |        \n"
        "   1.   |-- POST /analyze -->|                      |                      |        \n"
        "        |   (raw text post)  |                      |                      |        \n"
        "   2.   |                    |-- clean_text(raw) -->|                      |        \n"
        "        |                    |   (Regex pipeline)   |-- Strips URLs, @, #  |        \n"
        "   3.   |                    |<-- Cleaned String ---|                      |        \n"
        "   4.   |                    |-- analyze_sentiment()|                      |        \n"
        "        |                    |   (Cleaned text)     |-- TextBlob Polarity  |        \n"
        "        |                    |                      |-- TextBlob Subjectiv.|        \n"
        "        |                    |                      |-- 3-Way Distribution |        \n"
        "   5.   |                    |<-- Result Dictionary-|                      |        \n"
        "   6.   |                    |-- INSERT INTO posts ----------------------->|        \n"
        "        |                    |   (user_id, text, sentiment, polarity, conf)|        \n"
        "   7.   |                    |<-- Commit Confirmation ---------------------|        \n"
        "   8.   |<-- Render Response-|                                                      \n"
        "        |    (Colored bars,  |                                                      \n"
        "        |     Cleaned vs Raw)|                                                      \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.3b — Sequence Diagram: Political Text Ingestion and Sentiment Analysis", seq_nlp_ascii)

    add_section_h2(doc, "4.3.3", "Sequence Diagram 3: Multi-Dimensional History Search & Filtering")
    seq_filter_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|              SEQUENCE: MULTI-DIMENSIONAL HISTORY SEARCH & FILTERING                |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  User (Browser)          Flask Controller (app.py)          MySQL Database (posts) \n"
        "        |                            |                                 |            \n"
        "   1.   |-- GET /results?st=Pos&q=w->|                                 |            \n"
        "   2.   |                            |-- Verify session['user_id']     |            \n"
        "   3.   |                            |-- Construct Dynamic SQL Query:  |            \n"
        "        |                            |   WHERE user_id = %s            |            \n"
        "        |                            |   AND sentiment = %s            |            \n"
        "        |                            |   AND text_content LIKE %s ---->|            \n"
        "   4.   |                            |<-- Return Filtered Row Set -----|            \n"
        "   5.   |<-- Render results.html ----|                                 |            \n"
        "        |    (Filtered Table rows)   |                                 |            \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.3c — Sequence Diagram: Multi-Dimensional History Search & Filtering", seq_filter_ascii)

    add_section_h2(doc, "4.3.4", "Sequence Diagram 4: Administrator Content Moderation & Account Deletion")
    seq_admin_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|         SEQUENCE: ADMINISTRATOR CONTENT MODERATION & ACCOUNT DELETION             |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  Administrator (Browser)    Flask Controller (app.py)         MySQL Database (users)\n"
        "        |                            |                                 |            \n"
        "   1.   |-- POST /admin/delete-user->|                                 |            \n"
        "        |    (target user_id = 4)    |-- Check session['is_admin'] == 1|            \n"
        "   2.   |                            |-- Validate target != self       |            \n"
        "   3.   |                            |-- DELETE FROM users WHERE id=%s>|            \n"
        "   4.   |                            |   (MySQL cascades to posts)     |            \n"
        "   5.   |                            |<-- Confirm Rows Affected -------|            \n"
        "   6.   |<-- Flash & Redirect Admin -|                                 |            \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.3d — Sequence Diagram: Administrator Moderation and Account Deletion", seq_admin_ascii)

    add_section_h1(doc, "4.4", "Activity Diagram")
    add_body_p(doc, "The Activity Diagram visualizes the complete procedural workflow executed when a user enters political commentary into the SentixAI web application:")

    activity_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                       END-TO-END SYSTEM ACTIVITY WORKFLOW                         |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "                                       ( * )                                        \n"
        "                                         |                                          \n"
        "                                         v                                          \n"
        "                             [ User Navigates to /analyze ]                         \n"
        "                                         |                                          \n"
        "                                         v                                          \n"
        "                              < Is User Authenticated? >                            \n"
        "                                    /          \\                                    \n"
        "                           [No]    /            \\   [Yes]                           \n"
        "                                  v              v                                  \n"
        "                       [ Redirect to /login ]  [ Display Input Form & Demo Cards ]  \n"
        "                                                 |                                  \n"
        "                                                 v                                  \n"
        "                                       [ User Enters Text ]                         \n"
        "                                                 |                                  \n"
        "                                                 v                                  \n"
        "                                      < Text Length Valid? >                        \n"
        "                                     /                    \\                         \n"
        "                            [Empty] /                      \\  [Valid Text]          \n"
        "                                   v                        v                       \n"
        "                          [ Trigger Flash Alert ]  [ Execute clean_text() ]         \n"
        "                                                   (Strip URLs, @mentions, #tags)   \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                [ Extract TextBlob Polarity ]       \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                [ Calculate 3-Way Distribution ]    \n"
        "                                                (pos_pct, neu_pct, neg_pct)         \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                [ Determine Dominant Stance ]       \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                [ Persist in MySQL 'posts' ]        \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                [ Render Diagnostics Panel ]        \n"
        "                                                (Badge, Bars, Cleaned Comparison)   \n"
        "                                                            |                       \n"
        "                                                            v                       \n"
        "                                                          ( O )                     \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.4 — End-to-End System Activity Diagram", activity_ascii)

    add_section_h1(doc, "4.5", "Entity-Relationship (ER) Diagram")
    add_body_p(doc, "The Entity-Relationship Diagram documents the formal data architecture of the system. In strict adherence to the implemented codebase, the relational schema consists of exactly two normalized entities: 'users' and 'posts', connected by a 1:M relationship with cascading referential integrity:")

    erd_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                    ENTITY-RELATIONSHIP (ER) DIAGRAM — SENTIXAI                    |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  +-----------------------------------+         +-----------------------------------+\n"
        "  |               USERS               |         |               POSTS               |\n"
        "  +-----------------------------------+         +-----------------------------------+\n"
        "  | PK  id: INT AUTO_INCREMENT        | 1     M | PK  id: INT AUTO_INCREMENT        |\n"
        "  |     username: VARCHAR(50) UNIQUE  |---------| FK  user_id: INT NOT NULL         |\n"
        "  |     email: VARCHAR(100) UNIQUE    | submits |     text_content: TEXT NOT NULL   |\n"
        "  |     password: VARCHAR(255) NOT NULL|        |     sentiment: VARCHAR(20) NOT NULL|\n"
        "  |     is_admin: TINYINT(1) DEFAULT 0|         |     polarity: FLOAT NOT NULL      |\n"
        "  |     created_at: TIMESTAMP DEFAULT |         |     subjectivity: FLOAT NOT NULL  |\n"
        "  +-----------------------------------+         |     confidence: FLOAT NOT NULL    |\n"
        "                                                |     created_at: TIMESTAMP DEFAULT |\n"
        "                                                +-----------------------------------+\n"
        "  FOREIGN KEY CONSTRAINT: posts.user_id REFERENCES users(id) ON DELETE CASCADE       \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.5 — Entity-Relationship (ER) Diagram (users 1:M posts)", erd_ascii)

    add_section_h1(doc, "4.6", "Deployment Diagram")
    add_body_p(doc, "The Deployment Diagram depicts the physical execution architecture of the system across client user devices, cloud web servers, and the relational database daemon:")

    deploy_ascii = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                     PHYSICAL 3-TIER DEPLOYMENT TOPOLOGY                           |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "  +-------------------------------------------------------------+                    \n"
        "  | <<device>> Client User Device (Workstation / Mobile Phone)  |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  |   | <<executionEnvironment>> Web Browser (Chrome/Edge)  |   |                    \n"
        "  |   |   - HTML5 / CSS3 Responsive Presentation Engine     |   |                    \n"
        "  |   |   - Vanilla JavaScript Client-Side Validation       |   |                    \n"
        "  |   |   - Chart.js Dynamic HTML5 Canvas Chart Rendering   |   |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  +-------------------------------------------------------------+                    \n"
        "                                 |                                                   \n"
        "                                 | HTTPS / TLS 1.3 (Port 443)                        \n"
        "                                 v                                                   \n"
        "  +-------------------------------------------------------------+                    \n"
        "  | <<server>> PythonAnywhere Cloud Web Host (Linux Container)  |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  |   | <<webServer>> Gunicorn 21.2 / uWSGI Web Daemon      |   |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  |                              | internal WSGI interface                           \n"
        "  |                              v                                                   \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  |   | <<application>> Python 3.10+ Virtual Environment    |   |                    \n"
        "  |   |   - Flask 3.0.0 Microframework (app.py)             |   |                    \n"
        "  |   |   - Regex Preprocessing Engine (sentiment.py)       |   |                    \n"
        "  |   |   - TextBlob NLP & NLTK Lexicon                     |   |                    \n"
        "  |   |   - Werkzeug Cryptographic Security Hashing         |   |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  +-------------------------------------------------------------+                    \n"
        "                                 |                                                   \n"
        "                                 | MySQL TCP/IP Protocol (Port 3306)                 \n"
        "                                 v                                                   \n"
        "  +-------------------------------------------------------------+                    \n"
        "  | <<databaseServer>> Dedicated MySQL Server Instance (v8.0)  |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  |   | <<databaseSystem>> MySQL RDBMS Daemon (mysqld)      |   |                    \n"
        "  |   |   - Database: sentiment_analysis                    |   |                    \n"
        "  |   |   - Table: users (accounts, credentials, roles)     |   |                    \n"
        "  |   |   - Table: posts (inferences, polarity, metrics)    |   |                    \n"
        "  |   +-----------------------------------------------------+   |                    \n"
        "  +-------------------------------------------------------------+                    \n"
        "+-----------------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 4.6 — Physical Deployment Diagram (3-Tier Topology)", deploy_ascii)

    print("[+] Chapter 4 constructed.")
