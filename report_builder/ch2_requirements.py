"""
report_builder/ch2_requirements.py
Chapter 2: Requirement Engineering for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption
)

def build_chapter_2(doc):
    add_chapter_title(doc, "2", "Requirement Engineering", is_first=False)

    add_section_h1(doc, "2.1", "Stakeholder Requirements")
    add_body_p(doc, "Requirement Engineering establishes the functional capabilities and behavioral constraints demanded by end users, researchers, and system administrators. Through systematic domain analysis and consultation with project stakeholders, user requirements were decomposed into operational software specifications:")
    add_bullet_item(doc, "Users require an unencumbered registration and authentication flow ensuring privacy, session longevity, and protected access to individual analytical records.", "Authentication & Data Isolation: ")
    add_bullet_item(doc, "Researchers need an instantaneous NLP pipeline capable of parsing raw political text, showing both raw and cleansed representations, and outputting transparent percentage breakdowns.", "Analytical Transparency: ")
    add_bullet_item(doc, "Analysts demand multi-criteria filtering tools to query archived political remarks by sentiment stance or topical keywords without navigating complex database interfaces.", "Search & Archival Retrieval: ")
    add_bullet_item(doc, "Administrators require centralized visibility over total registered user accounts, system-wide submission volumes, and the power to purge non-compliant records.", "Governance & Moderation: ")

    add_section_h1(doc, "2.2", "Functional Requirements (FR-01 to FR-15)")
    add_body_p(doc, "The functional requirements define the explicit calculations, database interactions, interface views, and administrative workflows that the system must execute. Every functional requirement has been verified against the production codebase:")

    fr_headers = ["Requirement ID", "Functional Module", "Detailed Requirement Specification", "Priority"]
    fr_rows = [
        ["FR-01", "User Authentication", "The system shall permit guest visitors to register an account with a unique username, unique email, and password (minimum 4 characters).", "High"],
        ["FR-02", "Password Security", "The system shall hash passwords using Werkzeug PBKDF2 SHA-256 before persisting records in the MySQL users table.", "High"],
        ["FR-03", "Login Authentication", "The system shall verify user credentials against hashed database records and establish secure server-side sessions upon successful match.", "High"],
        ["FR-04", "Role-Based Access", "The system shall inspect user authority (is_admin = 1 vs 0) and route administrators to the Admin Panel and standard users to the Dashboard.", "High"],
        ["FR-05", "Text Ingestion", "The system shall provide a multi-line text input panel supporting arbitrary political statements, debate remarks, or social media commentary.", "High"],
        ["FR-06", "Regex Preprocessing", "The system shall execute regex routines to purge HTTP/HTTPS links, user @mentions, #hashtags, and normalize whitespace before sentiment scoring.", "High"],
        ["FR-07", "Lexical Polarity Scoring", "The system shall process cleaned text through TextBlob to compute polarity (-1.0 to +1.0) and subjectivity (0.0 to 1.0).", "High"],
        ["FR-08", "3-Way Distribution", "The system shall compute a fine-grained 3-way distribution (pos_pct, neu_pct, neg_pct) whose integer percentages strictly sum to exactly 100%.", "High"],
        ["FR-09", "Stance Classification", "The system shall assign a dominant sentiment label ('Positive', 'Neutral', or 'Negative') based on the highest percentage category.", "High"],
        ["FR-10", "Relational Storage", "The system shall insert the analyzed text, computed scores, sentiment label, and foreign key user_id into the MySQL posts table.", "High"],
        ["FR-11", "Comparative Diagnostics", "The system shall render a side-by-side comparison of original text versus regex-sanitized text alongside colored progress bars.", "Medium"],
        ["FR-12", "Analytics Dashboard", "The system shall calculate aggregate user statistics (total posts, positive %, negative %, neutral %) and render a dynamic Chart.js doughnut chart.", "High"],
        ["FR-13", "Multi-Criteria Filter", "The system shall filter archived records dynamically by sentiment category and execute SQL LIKE substring matching for keyword search.", "High"],
        ["FR-14", "Scoped Post Deletion", "The system shall allow users to delete their own analysis records while preventing unauthorized deletion of posts owned by others.", "High"],
        ["FR-15", "Admin Moderation Audit", "The system shall provide administrators with global oversight, platform-wide user account management, and content moderation deletion.", "High"]
    ]
    add_table_with_caption(doc, "Table 2.1 — Functional Requirements Specification (FR-01 to FR-15)", fr_headers, fr_rows, [1.1, 1.4, 3.1, 0.9])

    add_section_h1(doc, "2.3", "Non-Functional Requirements")
    add_body_p(doc, "Non-functional requirements specify the operational qualities, architectural constraints, and security behaviors required to ensure production robustness:")

    nfr_headers = ["Attribute", "Quality Objective", "Implementation Mechanism", "Verification Metric"]
    nfr_rows = [
        ["Performance & Latency", "Sub-second inference and page delivery under standard web loads.", "Lightweight TextBlob pattern analyzer; connection pooling and indexed queries.", "Mean inference latency < 250ms per post; page render < 500ms."],
        ["Security & Integrity", "Prevent unauthorized data access, credential leakage, and SQL injection.", "PBKDF2 SHA-256 hashing; parameterized SQL queries (%s); server-side session checks.", "Zero plain-text password storage; immune to basic SQL injection attempts."],
        ["Usability & UX", "Intuitive, self-explanatory responsive web interface accessible across devices.", "CSS3 glassmorphism, responsive grid, dynamic character counter, auto-dismiss alerts.", "Zero client-side installation; 100% usable on mobile and desktop browsers."],
        ["Reliability & Resilience", "Graceful degradation upon erroneous or empty user inputs.", "Client-side JS validation; server-side flash error messaging; try-finally DB closing.", "Zero unhandled 500 exceptions during invalid form submissions."],
        ["Maintainability", "Modular Three-Tier codebase with clean separation of concerns.", "Decoupled modules: app.py (controller), sentiment.py (NLP), database.py (connector).", "High code readability; documented docstrings across all modules."],
        ["Portability", "Cross-platform runtime capability across Windows and Linux cloud hosts.", "Pure Python implementation; WSGI Gunicorn support; environment-driven .env config.", "Seamless execution on Windows local dev and PythonAnywhere cloud Linux."]
    ]
    add_table_with_caption(doc, "Table 2.2 — Non-Functional Requirements Specification", nfr_headers, nfr_rows, [1.4, 1.5, 2.0, 1.6])

    add_section_h1(doc, "2.4", "Use Case Analysis")
    add_body_p(doc, "The system architecture partitions operational interactions into two primary user actors:")

    add_section_h2(doc, "2.4.1", "Actor 1: Standard User (Student / Researcher)")
    add_bullet_item(doc, "UC-01: Register New Account (provides unique username, email, password).")
    add_bullet_item(doc, "UC-02: Authenticate & Log In (creates secure session).")
    add_bullet_item(doc, "UC-03: Ingest Political Text (enters arbitrary text or selects quick demo card).")
    add_bullet_item(doc, "UC-04: View Diagnostic Inference (inspects polarity score, 3-way bars, and cleaned text).")
    add_bullet_item(doc, "UC-05: Inspect Analytics Dashboard (reviews KPI metrics and interactive Chart.js doughnut chart).")
    add_bullet_item(doc, "UC-06: Browse & Filter Analysis Archive (filters by stance and searches by keyword).")
    add_bullet_item(doc, "UC-07: Delete Own Analysis Record (scoped deletion restricted to user's user_id).")
    add_bullet_item(doc, "UC-08: Log Out (terminates session).")

    add_section_h2(doc, "2.4.2", "Actor 2: System Administrator")
    add_bullet_item(doc, "UC-09: Authenticate as Administrator (requires is_admin = 1 flag in database).")
    add_bullet_item(doc, "UC-10: Access Admin Moderation Console (restricted route /admin).")
    add_bullet_item(doc, "UC-11: Review Global Platform Statistics (total users, global ingestions, sentiment split).")
    add_bullet_item(doc, "UC-12: Manage User Accounts (views all registered users and deletes accounts with cascading removal).")
    add_bullet_item(doc, "UC-13: Moderate Global Posts (audits and deletes defamatory or non-compliant posts platform-wide).")

    add_section_h1(doc, "2.5", "Requirement Prioritization")
    add_body_p(doc, "Requirements were prioritized using the MoSCoW framework to ensure core academic milestones were achieved within the project timeline:")

    moscow_headers = ["Category", "Requirements Included", "Justification & Academic Impact"]
    moscow_rows = [
        ["Must Have (High)", "FR-01 to FR-10, FR-12, FR-14, FR-15", "Critical core features: authentication, NLP pipeline, database persistence, dashboard KPIs, and admin oversight."],
        ["Should Have (High)", "FR-11, FR-13", "Key usability features: side-by-side regex comparison and keyword search with stance filtering."],
        ["Could Have (Medium)", "Pre-seeded demonstration presets, REST API endpoint (/api/analyze), auto-dismissing flash alerts.", "Value-added features enhancing viva demonstration and external programmatic testing."],
        ["Won't Have (Deferred)", "Deep transformer models (BERT), live Twitter streaming API, automated sarcasm detection.", "Deferred to future scope due to computational hardware constraints and API monetization limits."]
    ]
    add_table_with_caption(doc, "Table 2.3 — Requirement Prioritization Matrix (MoSCoW)", moscow_headers, moscow_rows, [1.5, 2.0, 3.0])

    add_section_h1(doc, "2.6", "System Constraints")
    add_body_p(doc, "The technical development was subject to the following real-world engineering constraints:")
    add_bullet_item(doc, "Development and evaluation are conducted within the academic timeline of Semester-V (2026–2027).", "Academic Timeline Constraint: ")
    add_bullet_item(doc, "The model relies on lexical dictionary NLP (TextBlob), designed for lightweight CPU architectures rather than GPU clusters.", "Computational Constraints: ")
    add_bullet_item(doc, "Textual pre-processing and classification algorithms are trained for standard English grammatical structures.", "Linguistic Constraint: ")
    add_bullet_item(doc, "External visualization libraries (Chart.js, Font Awesome) are fetched via secure public CDNs, requiring internet connectivity for initial browser caching.", "Network Dependency: ")

    add_section_h1(doc, "2.7", "Project Assumptions")
    add_body_p(doc, "The system architecture relies on the following operational assumptions:")
    add_bullet_item(doc, "Input statements submitted for analysis represent coherent textual political discourse rather than random character noise.")
    add_bullet_item(doc, "The target deployment environment (PythonAnywhere) provides a stable Python 3 runtime and an accessible MySQL 8.0 server instance.")
    add_bullet_item(doc, "End users interact with the system using modern standards-compliant web browsers supporting HTML5 canvas and JavaScript ES6.")

    print("[+] Chapter 2 constructed.")
