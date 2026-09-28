"""
report_builder/ch3_sdlc.py
Chapter 3: Software Development Life Cycle for SentixAI
"""

from report_builder.common import (
    add_chapter_title, add_section_h1, add_section_h2,
    add_body_p, add_bullet_item, add_table_with_caption,
    add_figure_with_caption
)

def build_chapter_3(doc):
    add_chapter_title(doc, "3", "Software Development Life Cycle", is_first=False)

    add_section_h1(doc, "3.1", "SDLC Methodology (Waterfall Model)")
    add_body_p(doc, "The Software Development Life Cycle (SDLC) provides a disciplined, structured framework for orchestrating the engineering phases of a software system from initial conception to final deployment. For the SentixAI project, the classical Linear Sequential Model (commonly known as the Waterfall Model) was adopted as the foundational development methodology.")
    add_body_p(doc, "The Waterfall Model was selected due to its systematic, phase-gated progression, making it ideally aligned with undergraduate academic research requirements. Under this model, each phase possesses explicit entrance and exit criteria, generating formal documentation deliverables before the subsequent engineering phase commences:")
    add_bullet_item(doc, "Comprehensive gathering and specification of stakeholder requirements, domain problem analysis, and feasibility study, culminating in the formal Software Requirements Specification (SRS).", "Phase 1 — Requirement Analysis: ")
    add_bullet_item(doc, "High-level and low-level architectural modeling, database schema normalization, UML structural and behavioral diagrams, and UI wireframing, formalizing the Architecture Design Document.", "Phase 2 — System Design: ")
    add_bullet_item(doc, "Translation of design models into executable code, encompassing the Flask web controller (app.py), regular expression text pre-processing routines and TextBlob NLP engine (sentiment.py), and relational database connectors (database.py).", "Phase 3 — Implementation & Coding: ")
    add_bullet_item(doc, "Rigorous verification encompassing unit testing of regex filters, integration testing of Flask-to-MySQL pipelines, system validation, and security testing of SQL injection resistance and authentication mechanisms.", "Phase 4 — Integration & System Testing: ")
    add_bullet_item(doc, "Hardening the application for production, managing environment variables, initializing cloud schemas on PythonAnywhere, configuring WSGI process management, and establishing public access.", "Phase 5 — Deployment: ")
    add_bullet_item(doc, "Post-deployment operational audits, bug logging, database integrity monitoring, and documentation finalization for viva defense.", "Phase 6 — Review & Maintenance: ")

    # ASCII Waterfall Diagram
    waterfall_diagram = (
        "+-------------------------------------------------------------------------+\n"
        "|                 WATERFALL SOFTWARE DEVELOPMENT PHASES                   |\n"
        "+-------------------------------------------------------------------------+\n"
        "  [ Phase 1: Requirement Analysis ]\n"
        "            |  (Deliverables: Problem Definition, Objectives, SRS)\n"
        "            v\n"
        "  [ Phase 2: System Design & UML ]\n"
        "            |  (Deliverables: ERD, Schema, Class/Sequence Diagrams, Wireframes)\n"
        "            v\n"
        "  [ Phase 3: Implementation & Coding ]\n"
        "            |  (Deliverables: Flask app.py, sentiment.py, setup.sql, HTML/CSS)\n"
        "            v\n"
        "  [ Phase 4: Integration & Testing ]\n"
        "            |  (Deliverables: Unit Tests, Integration Tests, Bug Resolution)\n"
        "            v\n"
        "  [ Phase 5: Production Deployment ]\n"
        "            |  (Deliverables: PythonAnywhere Cloud Hosting, WSGI, Live Public URL)\n"
        "            v\n"
        "  [ Phase 6: Academic Viva & Defense ]\n"
        "               (Deliverables: Final Documentation, Demonstration, Review)\n"
        "+-------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 3.1 — Waterfall Software Development Life Cycle Phases", waterfall_diagram)

    add_section_h1(doc, "3.2", "Project Phases and Timeline")
    add_body_p(doc, "The project lifecycle spanned Semester-V of the academic year 2026–2027. Each milestone was rigorously planned and executed in accordance with institutional guidelines:")

    phase_headers = ["Milestone / Deliverable", "Start Date", "Target Completion", "Key Engineering Artifacts Produced"]
    phase_rows = [
        ["Project Synopsis", "30 Jul 2026", "01 Aug 2026", "Topic selection, initial problem statement, objective definition."],
        ["Project Proposal", "02 Aug 2026", "08 Aug 2026", "Literature review, feasibility analysis, methodology formulation."],
        ["SRS & UML Modeling", "10 Aug 2026", "24 Aug 2026", "Use case diagrams, sequence diagrams, class models, ER diagrams."],
        ["Architecture Design Document", "26 Aug 2026", "03 Sep 2026", "Three-tier architecture specification, UI wireframes, DB normalization."],
        ["Working Application", "05 Sep 2026", "15 Sep 2026", "Flask backend, TextBlob NLP pipeline, MySQL schema, frontend UI."],
        ["GitHub Repo & Final Report", "16 Sep 2026", "21 Sep 2026", "Git version control, deployment hardening, comprehensive academic report."],
        ["Presentation & Demonstration", "22 Sep 2026", "24 Sep 2026", "Live system demonstration, evaluation walkthrough, viva defense."]
    ]
    add_table_with_caption(doc, "Table 3.1 — Waterfall Project Lifecycle Timeline and Milestones", phase_headers, phase_rows, [1.6, 1.1, 1.1, 2.7])

    add_section_h1(doc, "3.3", "Gantt Chart Representation")
    add_body_p(doc, "The temporal allocation and overlapping task dependencies across the academic semester are modeled in the project Gantt Chart:")

    gantt_ascii = (
        "+-------------------------------------------------------------------------+\n"
        "|          PROJECT GANTT CHART — SEMESTER-V (ACADEMIC YEAR 2026-27)       |\n"
        "+-------------------------------------------------------------------------+\n"
        " Deliverables / Dates:     30 Jul  05 Aug  12 Aug  19 Aug  26 Aug  02 Sep  09 Sep  16 Sep  23 Sep\n"
        " -------------------------------------------------------------------------\n"
        " Synopsis (01 Aug)        [===]\n"
        " Proposal (08 Aug)              [====]\n"
        " SRS & UML (24 Aug)                    [============]\n"
        " Arch. Design (03 Sep)                                [======]\n"
        " Working App (15 Sep)                                        [==========]\n"
        " GitHub & Report (21 Sep)                                               [====]\n"
        " Presentation (24 Sep)                                                       [==]\n"
        " -------------------------------------------------------------------------\n"
        " Status: ALL MILESTONES COMPLETED ON SCHEDULE | REPOSITORY CODE: VERIFIED\n"
        "+-------------------------------------------------------------------------+"
    )
    add_figure_with_caption(doc, "Figure 3.2 — Project Gantt Chart Timeline (Semester-V 2026-27)", gantt_ascii)

    print("[+] Chapter 3 constructed.")
