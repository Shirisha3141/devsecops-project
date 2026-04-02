import os
from flask import Flask, render_template

app = Flask(__name__)

# --- THE FACULTY DEMO SWITCH ---
# To trigger a RED FAIL: Keep the line below active.
# To trigger a GREEN SUCCESS: Put a '#' in front of the line below.
ADMIN_PASSWORD = "AKIA5S6D7F8G9H0J1K2L_SECRET_KEY_EXPOSED" 

@app.route('/')
def home():
    # Safe check using globals()
    if globals().get('ADMIN_PASSWORD'):
        return render_template('index.html', vulnerable=True, error="CRITICAL: Hardcoded AWS Credential Detected!")
    
    return render_template('index.html', vulnerable=False)

if __name__ == "__main__":
    # We removed # nosec here so Bandit flags the host binding too
    app.run(host='0.0.0.0', port=8080)