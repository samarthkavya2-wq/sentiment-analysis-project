# SentixAI — Political Sentiment Analysis System

A web-based system for **sentiment analysis and filtering of political social media text** using Python, Flask, and MySQL.

Built as an academic project to demonstrate NLP-based text classification, relational database design, and full-stack web development.

---

## Features

- **User Authentication** — Secure registration and login with hashed passwords
- **Sentiment Analysis** — Analyze political text and classify as Positive, Neutral, or Negative
- **3-Way Distribution** — Shows percentage breakdown (e.g., 12% Positive, 50% Neutral, 38% Negative)
- **Text Preprocessing** — Automatically removes URLs, @mentions, and #hashtags using regex
- **Search & Filter** — Search analyzed posts by keyword and filter by sentiment category
- **Dashboard** — Personal statistics with Chart.js doughnut chart and KPI cards
- **Analysis History** — Full table of all past analyses with polarity, confidence, and timestamps
- **Admin Panel** — Manage user accounts and moderate posts across the platform (RBAC)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript, Jinja2 Templates |
| Backend | Python 3, Flask 3.0 |
| Database | MySQL |
| NLP Engine | TextBlob (NLTK) |
| Charts | Chart.js |
| Icons | Font Awesome 6.5.1 |
| Typography | Google Fonts (Plus Jakarta Sans, Space Grotesk) |

---

## Screenshots

### Home Page
The landing page introduces the system workflow — Text Ingestion → Pre-Processing → NLP Classification → Relational Archival.

### Sentiment Analysis
Users enter political text, and the system displays a 3-way sentiment breakdown with colored progress bars and a before/after text comparison showing what was cleaned by regex.

### Dashboard
Personal statistics with KPI cards (total posts, positive/negative/neutral counts), a doughnut chart, and a recent classifications table.

### Admin Panel
Administrators can view all registered users, their post counts, and moderate content across the platform.

---

## Project Structure

```
sentiment-analysis-project/
├── app.py                # Flask application (routes, auth, sessions)
├── database.py           # MySQL connection module
├── sentiment.py          # Text preprocessing + TextBlob analysis
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── database/
│   └── setup.sql         # Database schema (CREATE TABLE statements)
├── static/
│   ├── css/style.css     # Complete custom CSS (~1480 lines)
│   └── js/script.js      # Client-side validation & interactivity
└── templates/
    ├── base.html          # Base template (navbar, footer)
    ├── index.html         # Home page
    ├── login.html         # Login page
    ├── register.html      # Registration page
    ├── analyze.html       # Text analysis + results page
    ├── dashboard.html     # Statistics dashboard
    ├── results.html       # History & filtering page
    └── admin.html         # Admin management panel
```

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- MySQL Server
- pip (Python package manager)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sentiment-analysis-project.git
cd sentiment-analysis-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the database
Open MySQL and run:
```sql
source database/setup.sql;
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_NAME=sentiment_analysis
```

### 5. Download NLTK data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('brown')"
```

### 6. Run the application
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

### 7. Create admin account
```sql
-- Run in MySQL after hashing the password via Python
INSERT INTO users (username, email, password, is_admin) 
VALUES ('admin', 'admin@sentix.ai', '<hashed-password>', 1);
```

---

## Database Schema

### users
| Column | Type | Description |
|---|---|---|
| id | INT (PK) | Auto-increment user ID |
| username | VARCHAR(50) | Unique username |
| email | VARCHAR(100) | Unique email |
| password | VARCHAR(255) | Werkzeug hashed password |
| is_admin | TINYINT(1) | 0 = User, 1 = Admin |
| created_at | TIMESTAMP | Registration timestamp |

### posts
| Column | Type | Description |
|---|---|---|
| id | INT (PK) | Auto-increment post ID |
| user_id | INT (FK) | References users.id (CASCADE) |
| text_content | TEXT | Original submitted text |
| sentiment | VARCHAR(20) | Positive / Negative / Neutral |
| polarity | FLOAT | TextBlob polarity (-1.0 to +1.0) |
| subjectivity | FLOAT | TextBlob subjectivity (0.0 to 1.0) |
| confidence | FLOAT | Confidence percentage |
| created_at | TIMESTAMP | Analysis timestamp |

---

## How It Works

1. User enters political/social media text
2. **Preprocessing:** Regex removes URLs, @mentions, #hashtags, extra whitespace
3. **Analysis:** TextBlob computes polarity (-1.0 to +1.0) and subjectivity (0.0 to 1.0)
4. **Distribution:** Custom algorithm converts polarity into a 3-way percentage split (Positive %, Neutral %, Negative %) summing to 100%
5. **Classification:** Dominant percentage determines the label (Positive, Neutral, or Negative)
6. **Storage:** Result is saved to MySQL with user association
7. **Display:** Result shown with colored progress bars and text comparison

---

## License

This project was developed for academic purposes.

---

*Developed as a college project — September 2026*
