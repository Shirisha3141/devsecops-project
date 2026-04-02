import os
from flask import Flask, render_template

app = Flask(__name__)

# FACULTY DEMO: The Vulnerability
# To show a "Clean" site, comment out the line below.
ADMIN_PASSWORD = "Sreenidhi_Admin_123" 

@app.route('/')
def home():
    # We check if the dangerous variable exists
    has_vulnerability = False
    error_msg = ""
    
    if 'ADMIN_PASSWORD' in globals() and ADMIN_PASSWORD:
        has_vulnerability = True
        error_msg = f"CRITICAL: Hardcoded Credential Detected ('{ADMIN_PASSWORD}')"

    return render_template('index.html', 
                           vulnerable=has_vulnerability, 
                           error=error_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)