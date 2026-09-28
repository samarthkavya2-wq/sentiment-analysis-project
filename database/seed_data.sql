-- ============================================
-- Seed Data for Sentiment Analysis Project
-- Matches Architecture Design Document Wireframes & Test Data
-- ============================================

USE sentiment_analysis;

-- 1. Insert Users (Admin + Demo Student Accounts)
-- Admin: username 'admin', password 'admin123'
INSERT INTO users (id, username, email, password, is_admin, created_at) VALUES
(1, 'KAVYA', 'samarthkavya2@gmail.com', 'scrypt:32768:8:1$K8mAAGwb7HkuW8GT$1fa7f2f5394dc97931b39fe6c331e0b278070660a8173820ddc9650b625c287e292c9a27340d657631aff4922414dc2506edeb9ba230e1ce956e054b975dd54b', 0, '2026-09-05 10:00:00'),
(2, 'krish', 'krishshinde@gmail.com', 'scrypt:32768:8:1$6oWvsQWytxXjlLO3$aca1dd9deef1ee6903d5e3a81dc0d07ecf2d3248ebb38fa2c3d5e7759454815edaf398af231d9a90b5dbf6d52b71a62aa4b8f7f238660192bad8a13cfce38425', 0, '2026-09-07 10:00:00'),
(3, 'kavya', 'kavya@gmail.com', 'scrypt:32768:8:1$7iYa9b5HsQDJ8jZ0$ce61ed4bb10f29fd6ce2ec8fdb2f73eeb6618d2776e0d89de198c538c957563b12f974821b44415d73150a731b27f724c1fd1b17f9497111ef07610734898a5a', 0, '2026-09-07 10:30:00'),
(4, 'nirbhay', 'nirbhayshinde@gmail.com', 'scrypt:32768:8:1$AuM38lyeOoKVYGww$d6f0131822f7f5ae2235446b401fc6ee2782e11878ebff235edf0a75d27ba7b0bd0fa918a4700759acc0577ae9a7a5b9ae7b89a5a3a528e75de1f8f9d40e434d', 0, '2026-09-07 11:00:00'),
(7, 'admin', 'admin@sentix.ai', 'scrypt:32768:8:1$DwkOn76BkPQcWDYT$fa3dd32db66a23a5604e72b09938f215d42edcbd28def9dc739c9062d41589d18ec38976e501c8ad025e1a4d28cee7c10b96da323c9c7c138f963c9d0cdd2ed4', 1, '2026-09-10 09:00:00')
ON DUPLICATE KEY UPDATE is_admin=VALUES(is_admin);

-- 2. Insert 9 Sample Political Posts (Analyzed by user nirbhay, user_id=4)
INSERT INTO posts (id, user_id, text_content, sentiment, polarity, subjectivity, confidence, created_at) VALUES
(1, 4, 'The newly announced economic welfare initiative is exceptional. Thousands of low-income families will receive direct support and healthcare subsidies. A truly transformative policy!', 'Positive', 0.282, 0.5136, 28.2, '2026-09-07 13:18:52'),
(2, 4, 'The legislative assembly convened at 10 AM to discuss proposed amendments to the trade bill. Delegates from multiple parties submitted written remarks.', 'Neutral', 0.0, 0.0, 50.0, '2026-09-07 13:19:05'),
(3, 4, 'The state administration has utterly failed to regulate price spikes on essentials. Rampant inflation and broken campaign pledges have severely harmed citizens.', 'Negative', -0.45, 0.35, 45.0, '2026-09-07 13:19:14'),
(4, 4, 'The newly announced economic welfare initiative is exceptional. Thousands of low-income families will receive direct support and healthcare subsidies. A truly transformative policy!', 'Positive', 0.282, 0.5136, 28.2, '2026-09-07 13:25:35'),
(5, 4, 'The newly announced economic welfare initiative is exceptional. Thousands of low-income families will receive direct support and healthcare subsidies. A truly transformative policy!', 'Positive', 0.282, 0.5136, 28.2, '2026-09-07 13:26:08'),
(6, 4, 'Israel PM Netanyahu plans quick 24-hour trip to New York as Mayor Zohran Mamdani calls for his arrest', 'Positive', 0.1399, 0.3182, 13.99, '2026-09-10 01:15:30'),
(7, 4, 'If Iran wants to fight, that will be the official end of Iran. Never threaten the United States again!', 'Positive', 0.25, 0.1, 25.0, '2026-09-10 01:47:16'),
(8, 4, 'If Iran wants to fight, that will be the official end of Iran. Never threaten the United States again!', 'Neutral', 0.25, 0.1, 50.0, '2026-09-10 01:58:52'),
(9, 4, 'PM @narendramodi Ji with the ultimate "Angry Phuphaji" reference', 'Neutral', -0.25, 1.0, 50.0, '2026-09-11 05:40:17')
ON DUPLICATE KEY UPDATE sentiment=VALUES(sentiment);
