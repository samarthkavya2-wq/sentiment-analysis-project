"""
build_full_academic_report.py
Master runner to build the complete, authoritative academic project report:
"A Web-Based System for Sentiment Analysis and Filtering of Political Social Media Text Using Python and MySQL"
(SentixAI)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Ensure current folder is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from report_builder.common import add_page_number_to_footer
from report_builder.preliminary import build_preliminary_pages
from report_builder.ch1_feasibility import build_chapter_1
from report_builder.ch2_requirements import build_chapter_2
from report_builder.ch3_sdlc import build_chapter_3
from report_builder.ch4_uml import build_chapter_4
from report_builder.ch5_architecture import build_chapter_5
from report_builder.ch6_development import build_chapter_6
from report_builder.ch7_testing import build_chapter_7
from report_builder.ch8_deployment import build_chapter_8
from report_builder.ch9_performance_security import build_chapter_9
from report_builder.ch10_results import build_chapter_10
from report_builder.post_content import build_post_content

def build_academic_report():
    print("=" * 70)
    print("  SENTIXAI ACADEMIC FINAL PROJECT REPORT GENERATOR")
    print("  Degree: T.Y.B.Sc. Computer Science (Academic Year 2026-2027)")
    print("  Student: Kavya Samarth (Roll No: 9122)")
    print("=" * 70)

    doc = docx.Document()

    # 1. Academic Page Margins: Left = 1.25 inch (binding), Right/Top/Bottom = 1.0 inch
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.25)   # 1.25" Left binding margin
        section.right_margin = Inches(1.0)
        # Add page numbers to footer
        add_page_number_to_footer(section.footer)

    # 2. Base Typography: Times New Roman, 12pt, 1.5 line spacing, Justified
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0x21, 0x25, 0x29)

    print("\n[*] Step 1/12: Building Preliminary Pages...")
    build_preliminary_pages(doc)

    print("[*] Step 2/12: Building Chapter 1 (Identification & Feasibility Study)...")
    build_chapter_1(doc)

    print("[*] Step 3/12: Building Chapter 2 (Requirement Engineering)...")
    build_chapter_2(doc)

    print("[*] Step 4/12: Building Chapter 3 (Software Development Life Cycle)...")
    build_chapter_3(doc)

    print("[*] Step 5/12: Building Chapter 4 (System Modeling Using UML)...")
    build_chapter_4(doc)

    print("[*] Step 6/12: Building Chapter 5 (Architecture Design)...")
    build_chapter_5(doc)

    print("[*] Step 7/12: Building Chapter 6 (Application Development)...")
    build_chapter_6(doc)

    print("[*] Step 8/12: Building Chapter 7 (Integration & System Testing)...")
    build_chapter_7(doc)

    print("[*] Step 9/12: Building Chapter 8 (Deployment)...")
    build_chapter_8(doc)

    print("[*] Step 10/12: Building Chapter 9 (Performance & Security Testing)...")
    build_chapter_9(doc)

    print("[*] Step 11/12: Building Chapter 10 (Result & Discussion)...")
    build_chapter_10(doc)

    print("[*] Step 12/12: Building References & Appendix...")
    build_post_content(doc)

    # Output paths
    proj_out = os.path.join(current_dir, "SentixAI_Final_Project_Report.docx")
    desktop_out = r"C:\Users\Kavya\Desktop\SentixAI_Final_Project_Report.docx"

    print("\n[*] Saving documents to disk...")
    doc.save(proj_out)
    doc.save(desktop_out)

    print("=" * 70)
    print("  [SUCCESS] Project Report generated successfully!")
    print(f"  1. Project Path: {proj_out}")
    print(f"  2. Desktop Path: {desktop_out}")
    print("=" * 70)

if __name__ == '__main__':
    build_academic_report()
