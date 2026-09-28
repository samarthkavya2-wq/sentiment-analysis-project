-- ============================================
-- Database Setup for Sentiment Analysis Project
-- ============================================

-- Step 1: Create the database
-- A database is like a folder that holds all your tables
CREATE DATABASE IF NOT EXISTS sentiment_analysis;

-- Step 2: Tell MySQL to use this database
USE sentiment_analysis;

-- Step 3: Create the 'users' table
-- This table stores information about registered users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each user (auto-increments: 1, 2, 3...)
    username VARCHAR(50) UNIQUE NOT NULL,     -- Username (max 50 characters, must be unique)
    email VARCHAR(100) UNIQUE NOT NULL,       -- Email (max 100 characters, must be unique)
    password VARCHAR(255) NOT NULL,           -- Hashed password (NOT plain text!)
    is_admin TINYINT(1) DEFAULT 0,            -- 0 = Standard User, 1 = Administrator
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date/time when user registered (auto-filled)
);

-- Step 4: Create the 'posts' table
-- This table stores all the text that users submit for analysis
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each post
    user_id INT NOT NULL,                    -- Which user submitted this post (links to users table)
    text_content TEXT NOT NULL,              -- The actual text that was analyzed
    sentiment VARCHAR(20) NOT NULL,          -- Result: 'Positive', 'Negative', or 'Neutral'
    polarity FLOAT NOT NULL,                 -- Sentiment score: -1.0 (very negative) to +1.0 (very positive)
    subjectivity FLOAT NOT NULL,             -- How subjective the text is: 0.0 (fact) to 1.0 (opinion)
    confidence FLOAT NOT NULL,               -- How confident the analysis is (percentage)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the analysis was done
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    -- FOREIGN KEY means: user_id must match an id in the users table
    -- ON DELETE CASCADE means: if a user is deleted, their posts are also deleted
);
