/*
 * script.js — Main JavaScript File
 *
 * This file adds INTERACTIVITY to the website.
 * HTML = structure, CSS = appearance, JavaScript = behavior
 *
 * What this file does:
 * 1. Auto-dismiss flash messages after a few seconds
 * 2. Form validation before submission
 * 3. Confirm before deleting posts
 */

// ============================================
// AUTO-DISMISS FLASH MESSAGES
// ============================================
// Flash messages (success/error notifications) will automatically
// fade away after 5 seconds instead of staying forever

document.addEventListener('DOMContentLoaded', function() {
    // 'DOMContentLoaded' fires when the HTML page has fully loaded
    // We put our code inside this to make sure all elements exist first
    
    // Find all alert messages on the page
    var alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(function(alert) {
        // After 5000 milliseconds (5 seconds), fade out and remove
        setTimeout(function() {
            alert.style.transition = 'opacity 0.5s';   // Smooth fade
            alert.style.opacity = '0';                   // Make invisible
            
            // After the fade animation (500ms), remove from page completely
            setTimeout(function() {
                alert.remove();
            }, 500);
        }, 5000);  // 5000ms = 5 seconds
    });
});


// ============================================
// FORM VALIDATION
// ============================================
// Check that the text area is not empty before submitting

document.addEventListener('DOMContentLoaded', function() {
    var analyzeForm = document.querySelector('.analyze-form');
    
    if (analyzeForm) {
        analyzeForm.addEventListener('submit', function(event) {
            var textArea = document.getElementById('text');
            
            if (textArea && textArea.value.trim() === '') {
                // Prevent the form from submitting
                event.preventDefault();
                alert('Please enter some text to analyze!');
                textArea.focus();  // Put cursor back in the text area
            }
        });
    }
});


// ============================================
// CHARACTER COUNTER (for analyze page)
// ============================================
// Shows how many characters the user has typed

document.addEventListener('DOMContentLoaded', function() {
    var textArea = document.getElementById('text');
    
    if (textArea) {
        // Create a counter element below the textarea
        var counter = document.createElement('small');
        counter.style.color = '#7f8c8d';
        counter.style.display = 'block';
        counter.style.marginTop = '0.3rem';
        counter.textContent = '0 characters';
        textArea.parentNode.appendChild(counter);
        
        // Update counter when user types
        textArea.addEventListener('input', function() {
            var length = textArea.value.length;
            counter.textContent = length + ' characters';
            
            // Change color if too short
            if (length < 10 && length > 0) {
                counter.style.color = '#e74c3c';  // Red = too short
            } else {
                counter.style.color = '#7f8c8d';  // Grey = normal
            }
        });
    }
});
