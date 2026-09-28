-- ============================================
-- Database Setup for Sentiment Analysis Project
-- Project: Filtering Political Sentiment in Social Media
-- ============================================

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS sentiment_analysis;

-- Step 2: Use the database
USE sentiment_analysis;

-- Step 3: Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin TINYINT(1) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 4: Create the 'posts' table
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    text_content TEXT NOT NULL,
    sentiment VARCHAR(20) NOT NULL,
    polarity FLOAT NOT NULL,
    subjectivity FLOAT NOT NULL,
    confidence FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Step 5: Seed default Administrator Account
-- Username: admin
-- Password: admin123
INSERT INTO users (id, username, email, password, is_admin)
VALUES (
    7,
    'admin',
    'admin@sentix.ai',
    'scrypt:32768:8:1$DwkOn76BkPQcWDYT$fa3dd32db66a23a5604e72b09938f215d42edcbd28def9dc739c9062d41589d18ec38976e501c8ad025e1a4d28cee7c10b96da323c9c7c138f963c9d0cdd2ed4',
    1
)
ON DUPLICATE KEY UPDATE is_admin=1;
