"""
app.py — The Main Application File

This is the HEART of the project. It:
1. Creates the Flask web server
2. Defines all the ROUTES (URLs/pages of the website)
3. Handles user requests (login, register, analyze, etc.)
4. Connects the frontend (HTML pages) with the backend (Python) and database (MySQL)

WHAT IS A ROUTE?
A route is a URL path that the user visits. For example:
- "/" means the homepage (http://localhost:5000/)
- "/login" means the login page (http://localhost:5000/login)
- "/dashboard" means the dashboard (http://localhost:5000/dashboard)

Each route has a Python function that decides what to show or do.
"""

# ============================================
# STEP 1: Import required libraries
# ============================================
from flask import Flask, render_template, request, redirect, url_for, session, flash
# Flask         — creates the web server
# render_template — loads and shows HTML files from the 'templates' folder
# request       — gets data that the user sends (form inputs, URL parameters)
# redirect      — sends the user to a different page
# url_for       — generates a URL for a route by its function name
# session       — stores user data temporarily (like "who is logged in")
# flash         — shows one-time messages to the user (like "Login successful!")

from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash — converts a plain password into an encrypted hash
# check_password_hash    — checks if a password matches its hash

from dotenv import load_dotenv  # Loads environment variables from .env file
load_dotenv()  # Read .env file if it exists (for local development)

from database import get_db_connection  # Our database connection function
from sentiment import analyze_sentiment  # Our sentiment analysis function
import os  # Used to generate a random secret key
from flask_cors import CORS  # Enables Cross-Origin Resource Sharing for production API calls


# ============================================
# STEP 2: Create the Flask application
# ============================================
app = Flask(__name__)

# Secret key is needed for sessions (login system) and flash messages
# Think of it as a "password" that Flask uses internally to keep data secure
app.secret_key = os.environ.get('SECRET_KEY', 'sentiment_analysis_secret_key_2024')

# Enable CORS for API routes so external clients and frontends can connect
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Cookie security settings for production
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


# ============================================
# STEP 3: Define Routes (Pages)
# ============================================

# --- HOME PAGE ---
@app.route('/')
def index():
    """
    The homepage of the website.
    When someone visits http://localhost:5000/, this function runs.
    It loads and shows the 'index.html' template.
    """
    return render_template('index.html')


# --- REGISTER PAGE ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    The registration page.
    
    GET request: When user visits the page → show the registration form
    POST request: When user submits the form → create their account
    
    What is GET vs POST?
    - GET: "I want to SEE something" (loading a page)
    - POST: "I want to SEND something" (submitting a form)
    """
    if request.method == 'POST':
        # User submitted the registration form
        # Get the data they typed into the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Validate: check if fields are not empty
        if not username or not email or not password:
            flash('All fields are required!', 'error')
            return render_template('register.html')
        
        # Hash the password (NEVER store plain text passwords!)
        # Example: "mypassword" becomes "$2b$12$LJ3m5..." (unreadable)
        hashed_password = generate_password_hash(password)
        
        # Connect to database and insert the new user
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                (username, email, hashed_password)
            )
            conn.commit()  # Save the changes to the database
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))  # Send user to login page
        except Exception as e:
            # If username or email already exists, MySQL will throw an error
            flash('Username or email already exists. Please try different ones.', 'error')
        finally:
            cursor.close()
            conn.close()
    
    # GET request: just show the registration form
    return render_template('register.html')


# --- LOGIN PAGE ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    The login page.
    
    POST: Check if username and password match a record in the database.
    If yes: store user info in session and redirect to dashboard.
    If no: show an error message.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate
        if not username or not password:
            flash('Please enter both username and password.', 'error')
            return render_template('login.html')
        
        # Look up the user in the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # dictionary=True returns results as dicts
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()  # Get one result (or None if not found)
        cursor.close()
        conn.close()
        
        # Check if user exists AND password matches
        if user and check_password_hash(user['password'], password):
            # Login successful! Store user info in session
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['is_admin'] = bool(user.get('is_admin', 0))
            flash('Login successful! Welcome, ' + user['username'] + '!', 'success')
            if session['is_admin']:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')


# --- LOGOUT ---
@app.route('/logout')
def logout():
    """
    Log the user out.
    Clears the session (removes stored user info) and redirects to homepage.
    """
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


# --- ANALYZE TEXT PAGE ---
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """
    The main feature page — where users submit text for sentiment analysis.
    
    POST: 
    1. Get the text from the form
    2. Analyze its sentiment using our sentiment.py module
    3. Store the result in MySQL
    4. Show the result on the page
    """
    # Check if user is logged in
    if 'user_id' not in session:
        flash('Please login first to analyze text.', 'error')
        return redirect(url_for('login'))
    
    result = None  # Will hold the analysis result
    
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        
        if not text:
            flash('Please enter some text to analyze.', 'error')
        else:
            # Analyze the sentiment
            result = analyze_sentiment(text)
            
            # Store in database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO posts 
                   (user_id, text_content, sentiment, polarity, subjectivity, confidence) 
                   VALUES (%s, %s, %s, %s, %s, %s)''',
                (session['user_id'], text, result['sentiment'], 
                 result['polarity'], result['subjectivity'], result['confidence'])
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash('Text analyzed and saved successfully!', 'success')
    
    return render_template('analyze.html', result=result)


# --- RESULTS PAGE ---
@app.route('/results')
def results():
    """
    Shows all analyzed posts with filtering and search capabilities.
    
    Users can:
    - View all their analyzed posts
    - Filter by sentiment (Positive/Negative/Neutral)
    - Search posts by keywords
    """
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Get filter and search from URL parameters
    # Example URL: /results?sentiment=Positive&search=government
    sentiment_filter = request.args.get('sentiment', '')
    search_query = request.args.get('search', '')
    
    # Build the SQL query dynamically based on filters
    query = 'SELECT * FROM posts WHERE user_id = %s'
    params = [session['user_id']]
    
    if sentiment_filter:
        query += ' AND sentiment = %s'
        params.append(sentiment_filter)
    
    if search_query:
        query += ' AND text_content LIKE %s'
        params.append(f'%{search_query}%')  # % means "anything before/after"
    
    query += ' ORDER BY created_at DESC'  # Newest first
    
    cursor.execute(query, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('results.html', posts=posts,
                         current_filter=sentiment_filter,
                         search_query=search_query)


# --- DASHBOARD PAGE ---
@app.route('/dashboard')
def dashboard():
    """
    The dashboard shows statistics and summary of all analyzed posts.
    
    It queries the database to get:
    - Total number of posts
    - Count of Positive, Negative, Neutral posts
    - 5 most recent posts
    """
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Get total number of posts
    cursor.execute('SELECT COUNT(*) as total FROM posts WHERE user_id = %s',
                   (session['user_id'],))
    total = cursor.fetchone()['total']
    
    # Get count of each sentiment type using GROUP BY
    # GROUP BY groups rows with the same sentiment together and counts them
    cursor.execute(
        'SELECT sentiment, COUNT(*) as count FROM posts WHERE user_id = %s GROUP BY sentiment',
        (session['user_id'],)
    )
    sentiment_counts = {row['sentiment']: row['count'] for row in cursor.fetchall()}
    
    positive = sentiment_counts.get('Positive', 0)
    negative = sentiment_counts.get('Negative', 0)
    neutral = sentiment_counts.get('Neutral', 0)
    
    # Get 5 most recent posts
    cursor.execute(
        'SELECT * FROM posts WHERE user_id = %s ORDER BY created_at DESC LIMIT 5',
        (session['user_id'],)
    )
    recent_posts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('dashboard.html',
                         total=total,
                         positive=positive,
                         negative=negative,
                         neutral=neutral,
                         recent_posts=recent_posts)


# --- DELETE POST ---
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    """
    Delete a specific post.
    
    <int:post_id> means the URL contains a number (the post's ID).
    Example: /delete/5 would delete the post with id=5
    
    Security: We also check user_id to make sure users can only delete their own posts.
    """
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    # Delete only if BOTH the post_id AND user_id match (security!)
    cursor.execute('DELETE FROM posts WHERE id = %s AND user_id = %s',
                   (post_id, session['user_id']))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Post deleted successfully.', 'success')
    return redirect(url_for('results'))


# ============================================
# ADMIN PANEL ROUTES (Role-Based Access Control)
# ============================================

@app.route('/admin')
def admin_dashboard():
    """
    Admin Management Dashboard:
    Accessible only to users with is_admin = 1.
    Provides global system analytics, total registered accounts,
    and moderation control across all submitted posts.
    """
    # Authorization check
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Access restricted. Administrator privileges required.', 'error')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # 1. Total registered accounts
    cursor.execute('SELECT COUNT(*) AS total_users FROM users')
    total_users = cursor.fetchone()['total_users']
    
    # 2. Total posts analyzed globally
    cursor.execute('SELECT COUNT(*) AS total_posts FROM posts')
    total_posts = cursor.fetchone()['total_posts']
    
    # 3. Global sentiment distribution
    cursor.execute('SELECT sentiment, COUNT(*) AS count FROM posts GROUP BY sentiment')
    global_counts = {row['sentiment']: row['count'] for row in cursor.fetchall()}
    pos_count = global_counts.get('Positive', 0)
    neg_count = global_counts.get('Negative', 0)
    neu_count = global_counts.get('Neutral', 0)
    
    # 4. Fetch all registered users with post counts
    cursor.execute('''
        SELECT u.id, u.username, u.email, u.is_admin, u.created_at, COUNT(p.id) AS post_count
        FROM users u
        LEFT JOIN posts p ON u.id = p.user_id
        GROUP BY u.id, u.username, u.email, u.is_admin, u.created_at
        ORDER BY u.created_at DESC
    ''')
    all_users = cursor.fetchall()
    
    # 5. Fetch all posts with author username for moderation
    cursor.execute('''
        SELECT p.id, p.user_id, p.text_content, p.sentiment, p.confidence, p.polarity, p.created_at, u.username
        FROM posts p
        JOIN users u ON p.user_id = u.id
        ORDER BY p.created_at DESC
        LIMIT 50
    ''')
    all_posts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('admin.html',
                           total_users=total_users,
                           total_posts=total_posts,
                           pos_count=pos_count,
                           neg_count=neg_count,
                           neu_count=neu_count,
                           all_users=all_users,
                           all_posts=all_posts)


@app.route('/admin/delete-post/<int:post_id>', methods=['POST'])
def admin_delete_post(post_id):
    """Admin moderation endpoint: delete any inappropriate post across the platform."""
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Unauthorized access.', 'error')
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Post deleted by administrator.', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/delete-user/<int:user_id>', methods=['POST'])
def admin_delete_user(user_id):
    """Admin moderation endpoint: delete user account (and cascading posts)."""
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Unauthorized access.', 'error')
        return redirect(url_for('login'))
    
    # Prevent self-deletion
    if user_id == session.get('user_id'):
        flash('You cannot delete your own active administrator account.', 'error')
        return redirect(url_for('admin_dashboard'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('User account and associated posts removed.', 'success')
    return redirect(url_for('admin_dashboard'))


# ============================================
# PRODUCTION HEALTH & API ENDPOINTS
# ============================================

@app.route('/health')
def health():
    """
    Production health-check endpoint.
    Used by cloud platforms (Render, Railway, etc.) and evaluators to verify
    the application and database connection are working.
    """
    db_status = "connected"
    try:
        conn = get_db_connection()
        if not conn.is_connected():
            db_status = "disconnected"
        conn.close()
    except Exception as err:
        db_status = f"error: {str(err)}"

    status_code = 200 if db_status == "connected" else 503
    return {
        "status": "healthy" if db_status == "connected" else "unhealthy",
        "database": db_status,
        "app": "SentixAI - Political Sentiment Analysis"
    }, status_code


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """
    REST API endpoint for programmatic text sentiment analysis.
    Accepts JSON: {"text": "political statement"}
    Returns JSON: Full sentiment classification and distribution
    """
    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()

    if not text:
        return {"error": "Please provide a 'text' field in JSON payload."}, 400

    result = analyze_sentiment(text)
    return {
        "success": True,
        "result": result
    }, 200


# ============================================
# STEP 4: Run the application
# ============================================
if __name__ == '__main__':
    # Cloud environments set the PORT environment variable dynamically
    port = int(os.environ.get('PORT', 5000))
    # debug mode can be enabled with FLASK_DEBUG=1 in .env
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1')

    print("=" * 50)
    print("  Sentiment Analysis Web Application")
    print(f"  Starting server on http://0.0.0.0:{port}")
    print(f"  Debug mode: {debug_mode}")
    print("=" * 50)
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
