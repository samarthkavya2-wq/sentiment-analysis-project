"""
sentiment.py — Sentiment Analysis Module

This file contains the "brain" of the project.
It takes text as input, cleans it, analyzes the sentiment,
and returns a result (Positive, Negative, or Neutral).

We use a library called TextBlob which has a pre-trained model
that can understand English text sentiment.
"""

from textblob import TextBlob  # The library that does sentiment analysis
import re  # 're' stands for Regular Expressions — used for text cleaning


def clean_text(text):
    """
    Clean the text before analyzing it.
    
    Why? Social media text contains URLs, @mentions, #hashtags,
    and extra spaces that confuse the sentiment analyzer.
    We remove them to get cleaner results.
    
    Example:
        Input:  "Check this out @PM_India https://example.com #politics   Great work!"
        Output: "Check this out Great work!"
    """
    # Remove URLs (links starting with http or www)
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove @mentions (like @username)
    text = re.sub(r'@\w+', '', text)
    
    # Remove #hashtags (like #politics)
    # We remove the # symbol but could keep the word — here we remove entirely
    text = re.sub(r'#\w+', '', text)
    
    # Remove extra spaces and trim whitespace from start/end
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def analyze_sentiment(text):
    """
    Analyze the sentiment of given text.
    
    How it works:
    1. Clean the text (remove URLs, mentions, etc.)
    2. Pass cleaned text to TextBlob
    3. TextBlob returns two scores:
       - Polarity: -1.0 (very negative) to +1.0 (very positive)
       - Subjectivity: 0.0 (objective/factual) to 1.0 (subjective/opinion)
    4. Based on the polarity score, classify as Positive/Negative/Neutral
    5. Calculate a confidence percentage
    
    Parameters:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary containing analysis results
    """
    # Step 1: Clean the text
    cleaned_text = clean_text(text)
    
    # Step 2: Create a TextBlob object — this analyzes the text
    blob = TextBlob(cleaned_text)
    
    # Step 3: Get the polarity and subjectivity scores
    polarity = blob.sentiment.polarity        # Range: -1.0 to +1.0
    subjectivity = blob.sentiment.subjectivity  # Range: 0.0 to 1.0
    
    # Step 4: Classify the sentiment based on polarity
    # We calculate fine-grained 3-way distribution percentages summing to 100%
    # Polarity ranges from -1.0 to +1.0
    # Subjectivity (0.0 to 1.0) reflects opinion intensity
    intensity = max(abs(polarity), 0.05)
    
    if polarity > 0:
        # Positive leaning
        raw_pos = 0.20 + (polarity * 0.70)
        raw_neg = max(0.05, 0.15 - (polarity * 0.12))
        raw_neu = max(0.10, 1.0 - (raw_pos + raw_neg))
    elif polarity < 0:
        # Negative leaning
        raw_neg = 0.20 + (abs(polarity) * 0.70)
        raw_pos = max(0.05, 0.15 - (abs(polarity) * 0.12))
        raw_neu = max(0.10, 1.0 - (raw_neg + raw_pos))
    else:
        # Completely neutral
        raw_pos = 0.10
        raw_neg = 0.10
        raw_neu = 0.80

    total_weight = raw_pos + raw_neu + raw_neg
    pos_pct = round((raw_pos / total_weight) * 100)
    neg_pct = round((raw_neg / total_weight) * 100)
    neu_pct = 100 - (pos_pct + neg_pct)  # Guarantee sum to exactly 100%

    # Determine dominant sentiment category
    if pos_pct > neu_pct and pos_pct > neg_pct:
        sentiment = 'Positive'
    elif neg_pct > neu_pct and neg_pct > pos_pct:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    # Step 5: Calculate confidence as a percentage (dominant class percentage)
    confidence = max(pos_pct, neu_pct, neg_pct)
    
    # Step 6: Return all results as a dictionary
    return {
        'original_text': text,          # The original text entered by user
        'cleaned_text': cleaned_text,    # Text after cleaning
        'sentiment': sentiment,          # 'Positive', 'Negative', or 'Neutral'
        'polarity': round(polarity, 4),  # The raw polarity score
        'subjectivity': round(subjectivity, 4),  # How opinionated the text is
        'confidence': confidence,        # Confidence percentage
        'pos_pct': pos_pct,              # Positive percentage (0-100)
        'neu_pct': neu_pct,              # Neutral percentage (0-100)
        'neg_pct': neg_pct               # Negative percentage (0-100)
    }


# ============================================
# QUICK EXPLANATION OF SENTIMENT SCORES:
# ============================================
# 
# Polarity Examples:
#   "I love this government policy!"        → polarity ≈ +0.5 (Positive)
#   "This is the worst decision ever."      → polarity ≈ -0.6 (Negative)
#   "The government announced a new policy." → polarity ≈ 0.0 (Neutral)
#
# Subjectivity Examples:
#   "The election is on Monday."            → subjectivity ≈ 0.0 (Fact)
#   "I think this leader is amazing."       → subjectivity ≈ 0.8 (Opinion)
#
# ============================================
