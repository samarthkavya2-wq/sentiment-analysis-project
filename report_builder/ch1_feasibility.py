"""
report_builder/ch1_feasibility.py
Chapter 1: Identification & Feasibility Study for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption
)

def build_chapter_1(doc):
    add_chapter_title(doc, "1", "Identification & Feasibility Study", is_first=False)

    add_section_h1(doc, "1.1", "Introduction / Background")
    add_body_p(doc, "In the modern digital era, social media platforms including X (formerly Twitter), Reddit, Facebook, and public news forums have emerged as the primary digital arenas for political dialogue, policy deliberation, and electoral campaign debate. Millions of citizens, journalists, and public officials articulate their stances on legislative bills, economic welfare measures, diplomatic decisions, and institutional governance on a daily basis. The digital footprint created by this discourse reflects shifting public sentiments, community polarization, and the emerging reception of government initiatives in near real-time.")
    add_body_p(doc, "However, social media discourse is intrinsically unstructured, informal, and volatile. It is characterized by noisy linguistic features including irregular capitalization, internet slang, abbreviations, contextual hashtags, user handle mentions, and hyperlinks. The sheer volume and velocity of incoming textual posts make manual human evaluation, qualitative coding, and opinion tabulation completely unscalable, economically unsustainable, and heavily prone to subjective cognitive biases.")
    add_body_p(doc, "The SentixAI platform—entitled 'Filtering Political Sentiment in Social Media from Textual Information Using MySQL'—addresses this technical challenge by designing and implementing an automated, web-based Natural Language Processing (NLP) system. Built using Python, the Flask web framework, and a normalized MySQL relational database, SentixAI accepts raw political statements, systematically purges noise via regular expression pipelines, extracts mathematical polarity and subjectivity scores using TextBlob, computes a fine-grained 3-way distribution (Positive, Neutral, and Negative), and records the inferences within an auditable, relational archive.")

    add_section_h1(doc, "1.2", "Problem Identification")
    add_body_p(doc, "Contemporary political analysts, democratic institutions, academic researchers, and news organizations encounter severe methodological bottlenecks when attempting to track public sentiment across digital media channels. The fundamental problems identified include:")
    add_bullet_item(doc, "Manual Review Inefficiency: Human categorization of thousands of daily political statements requires extensive labor, incurs significant recurring costs, and introduces unavoidable latency, preventing real-time sentiment tracking.", "Volume and Velocity: ")
    add_bullet_item(doc, "Linguistic Noise and Formatting Irregularities: Social media posts contain high densities of non-semantic noise—specifically embedded URLs, Twitter-style @mentions, and campaign #hashtags—that distort standard text parsers and induce false-positive sentiment classifications.", "Textual Distortion: ")
    add_bullet_item(doc, "Overly Coarse Binary Classification: Conventional binary models (Positive vs. Negative) fail to capture neutral, factual, or balanced political reporting, forcing objective news statements into artificial polar categories.", "Taxonomic Limitation: ")
    add_bullet_item(doc, "Lack of Relational Persistence and Auditability: Many lightweight text analysis scripts evaluate sentiment in memory but lack persistent relational archiving, historical longitudinal filtering, and multi-user access controls.", "Data Isolation: ")
    add_bullet_item(doc, "Absence of Role-Based Governance: Public political analytics platforms require strict governance mechanisms to prevent malicious injection of defamatory commentary and ensure that standard researchers cannot alter platform-wide records.", "Administrative Void: ")

    add_section_h1(doc, "1.3", "Problem Justification")
    add_body_p(doc, "Automating political sentiment analysis through a disciplined three-tier web application architecture directly overcomes the documented limitations of manual observation and unanchored script tools. By offloading tokenization, lexical polarity computation, and noise elimination to automated server-side algorithms, sentiment can be extracted and classified in sub-second intervals.")
    add_body_p(doc, "Furthermore, utilizing a normalized relational database (MySQL) guarantees ACID transactional integrity, enabling multi-user concurrency, indexed historical search, and longitudinal aggregation of public stances across diverse political themes. Establishing a formal web-based platform with Role-Based Access Control (RBAC) ensures transparency, data safety, and reproducibility—essential pillars for computational social science and democratic policy evaluation.")

    add_section_h1(doc, "1.4", "Objectives")
    add_body_p(doc, "The core engineering objectives established for the SentixAI project are formulated as follows:")
    add_bullet_item(doc, "To architect and implement an intuitive, responsive web interface allowing registered users to submit unstructured political discourse and view immediate classification metrics.", "User Interaction: ")
    add_bullet_item(doc, "To construct an automated server-side regular expression (regex) text pre-processing pipeline capable of isolating and stripping URLs, @mentions, and #hashtags while preserving semantic meaning.", "Linguistic Sanitization: ")
    add_bullet_item(doc, "To integrate the TextBlob NLP engine to compute continuous lexical polarity scores (-1.0 to +1.0) and subjectivity indices (0.0 to 1.0).", "Sentiment Modeling: ")
    add_bullet_item(doc, "To design an algorithmic 3-way proportional normalization engine generating exact integer distributions of Positive, Neutral, and Negative stance summing to 100%.", "Proportional Classification: ")
    add_bullet_item(doc, "To design and deploy a normalized relational MySQL database schema featuring 'users' and 'posts' tables linked via foreign key constraints with ON DELETE CASCADE.", "Relational Archival: ")
    add_bullet_item(doc, "To construct an interactive personal analytics dashboard incorporating real-time KPI metrics and dynamic Chart.js visualizations.", "Visual Intelligence: ")
    add_bullet_item(doc, "To provide an administrative moderation console enabling user management, platform-wide metric auditing, and inappropriate post deletion.", "Administrative Oversight: ")

    add_section_h1(doc, "1.5", "Scope & Limitations")
    add_section_h2(doc, "1.5.1", "Functional Scope")
    add_body_p(doc, "The project scope encompasses user registration with PBKDF2 password hashing, secure credential verification, session management, multi-lingual text normalization for English discourse, real-time sentiment scoring, database persistence, multi-criteria historical filtering (by sentiment category and SQL LIKE keyword search), scoped record deletion, and administrator oversight.")

    add_section_h2(doc, "1.5.2", "System Limitations")
    add_body_p(doc, "To maintain absolute academic integrity, the following limitations are formally acknowledged:")
    add_bullet_item(doc, "Lexical Model Horizon: TextBlob relies on a curated pattern lexicon. While highly accurate on explicit sentiment adjectives and adverbs, it cannot reliably decode complex political sarcasm, irony, or double entendres.", "Sarcasm and Subtlety: ")
    add_bullet_item(doc, "Linguistic Scope: The current implementation focuses exclusively on English textual discourse. Multilingual or vernacular code-switched text (e.g., Hinglish) is outside the immediate scope.", "Language Support: ")
    add_bullet_item(doc, "Discourse vs. Voter Intent: The system explicitly analyzes the emotional polarity expressed in a specific text statement; it does not claim to diagnose the internal political voting allegiance or psychological profile of a human voter.", "Scope of Inference: ")

    add_section_h1(doc, "1.6", "Stakeholder Identification")
    add_body_p(doc, "The system architecture is engineered to serve four primary categories of stakeholders:")
    add_bullet_item(doc, "Citizens seeking to evaluate the objectivity, sentiment bias, and public reception of debated policies and legislative announcements.", "Citizens and Voters: ")
    add_bullet_item(doc, "Academic researchers and political scientists tracking macro-level shifts in public approval, campaign narrative reception, and community polarization over time.", "Political Analysts & Researchers: ")
    add_bullet_item(doc, "Journalists and editorial fact-checkers auditing political discourse for polarized rhetoric and verifying the balance of quoted remarks.", "Media Monitors & Journalists: ")
    add_bullet_item(doc, "Platform moderators tasked with managing registered student/researcher credentials, maintaining relational integrity, and purging toxic content.", "System Administrators: ")

    add_section_h1(doc, "1.7", "Technical Feasibility")
    add_body_p(doc, "The technological stack selected for SentixAI demonstrates exceptionally high technical feasibility:")
    add_bullet_item(doc, "Python 3 is the recognized gold standard for data engineering and natural language processing. Flask 3.0 provides a lightweight, modular, and unopinionated WSGI framework optimal for academic web architectures.", "Backend Architecture: ")
    add_bullet_item(doc, "TextBlob is a well-established, pre-trained lexical NLP library built upon NLTK corpora, eliminating the heavy GPU computational requirements of deep transformer neural networks while providing deterministic, sub-second inference.", "NLP Engine: ")
    add_bullet_item(doc, "MySQL 8.0 is a battle-tested relational database management system supporting robust concurrency, ACID transactions, B-tree indexing, and relational foreign key constraints.", "Database Tier: ")
    add_bullet_item(doc, "Vanilla JavaScript, CSS3 variables, and Chart.js ensure modern, responsive interactivity without bulky client-side build steps or framework version churn.", "Frontend Presentation: ")

    add_section_h1(doc, "1.8", "Economic Feasibility")
    add_body_p(doc, "Economic feasibility evaluates whether the financial expenditure required for software acquisition, infrastructure, and maintenance justifies the operational value delivered. SentixAI is built exclusively upon open-source software licenses, resulting in zero software acquisition expense.")

    econ_headers = ["Resource Component", "Selected Technology", "Licensing Model", "Academic Cost (INR)"]
    econ_rows = [
        ["Programming Language & Runtime", "Python 3.10+ / 3.14", "Python Software Foundation (Open Source)", "Rs. 0.00"],
        ["Web Framework & WSGI Server", "Flask 3.0.0 / Gunicorn 21.2", "BSD 3-Clause License", "Rs. 0.00"],
        ["Natural Language Processing", "TextBlob 0.18.0 / NLTK 3.8.1", "MIT / Apache 2.0 License", "Rs. 0.00"],
        ["Relational Database Management", "MySQL Community Server 8.0", "GPL v2 License", "Rs. 0.00"],
        ["Frontend UI & Charting CDN", "Chart.js / Font Awesome 6.5.1", "MIT / SIL OFL License", "Rs. 0.00"],
        ["Cloud Production Hosting", "PythonAnywhere Free Tier", "Free Academic Quota", "Rs. 0.00"],
        ["Development Environment", "Visual Studio Code / Git", "MIT License", "Rs. 0.00"],
        ["Total Direct Capital Expenditure", "All Open-Source Stack", "100% Free / Academic", "Rs. 0.00"]
    ]
    add_table_with_caption(doc, "Table 1.1 — Economic Feasibility and Open-Source Cost Analysis", econ_headers, econ_rows, [1.8, 1.8, 1.8, 1.1])

    add_section_h1(doc, "1.9", "Operational Feasibility")
    add_body_p(doc, "Operational feasibility assesses how effectively the proposed system integrates into the everyday workflow of academic researchers, students, and evaluators. SentixAI requires zero client-side installation: the entire application is delivered via standard web browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari) across desktop and mobile form factors.")
    add_body_p(doc, "The user interface incorporates intuitive design patterns—standardized form fields, immediate client-side character counters, pre-loaded demonstration dataset buttons, color-coded visual badges (Green for Positive, Grey for Neutral, Red for Negative), and animated progress bars. Consequently, no specialized user training is necessary, confirming outstanding operational feasibility.")

    print("[+] Chapter 1 constructed.")
